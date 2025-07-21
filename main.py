# main.py（已整合 binary mode 支援）
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from phe import paillier
import hashlib

from GBF import gbf_gen, BF, hashs, size
from PPDI import gbf_merge, compare, verify

# === Global Parameters ===
MAX_PREFIX_LEN = 32      # prefix 拆分最大長度 ℓ
BINARY_PREFIX_MODE = True  # 是否使用 binary 編碼

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'txt'}
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

pk, sk = paillier.generate_paillier_keypair()
files = {}
ma = {}
aa = {}
gbf = {}
c = {}
mergegbf = [0] * size
mergec = [0] * size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def import_data(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def get_prefixes(label, max_prefix_len=None, binary_mode=False):
    if binary_mode:
        bin_label = ''.join(format(ord(c), '08b') for c in label)
        L = len(bin_label)
        ℓ = min(L, max_prefix_len) if max_prefix_len else L
        return [bin_label[:i] for i in range(1, ℓ + 1)]
    else:
        L = len(label)
        ℓ = min(L, max_prefix_len) if max_prefix_len else L
        return [label[:i] for i in range(1, ℓ + 1)]

def flip_last_bit(s):
    return s[:-1] + ('1' if s[-1] == '0' else '0')

def preprocess(filename, cname, max_prefix_len=MAX_PREFIX_LEN, binary_mode=BINARY_PREFIX_MODE):
    tmp, tmp1 = [], []
    for line in files[filename]:
        x, label = line.strip().split(',')
        prefixes = get_prefixes(label, max_prefix_len, binary_mode)
        if filename == cname:
            for p in prefixes:
                tmp.append(f"{x}||{p}")
        else:
            for p in prefixes:
                tmp.append(f"{x}||{flip_last_bit(p)}")
        tmp1.extend([label]*len(prefixes))
    ma[filename] = tmp
    aa[filename] = tmp1
    gbf1, c1 = gbf_gen(tmp, pk)
    gbf[filename] = gbf1
    c[filename] = c1

def PPDImain(cname, sender_name):
    global mergegbf, mergec
    mergegbf, mergec = gbf_merge(gbf[sender_name], gbf[cname], c[sender_name], c[cname])
    comparec = compare(mergec, c[cname])
    enc_message = verify(mergegbf, comparec)
    dec_message = sk.decrypt(enc_message)
    return comparec

def checkintersection(comparec, cname):
    intersection = []
    for data in ma[cname]:
        data1 = data.encode('utf-8')
        if all(comparec[int(hash_func(data1).hexdigest(), 16) % size] == 1 for hash_func in hashs):
            intersection.append(data.split('||')[0])
    return list(set(intersection))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    filenames = []
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
        if len(uploaded_files) != 2:
            return "Please upload exactly two files."
        for file in uploaded_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filenames.append(filename)
        return render_template('result.html', filenames=filenames)
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    filenames = request.form.getlist('file')
    client_name = request.form.get('client')
    if len(filenames) != 2 or not client_name:
        return "Error: Two files and one client must be selected."

    fname1, fname2 = filenames[0].replace('.txt', ''), filenames[1].replace('.txt', '')
    sender_name = fname2 if client_name == fname1 else fname1

    for fname in [client_name, sender_name]:
        files[fname] = import_data(fname + '.txt')
        preprocess(fname, client_name, max_prefix_len=MAX_PREFIX_LEN, binary_mode=BINARY_PREFIX_MODE)

    comparec = PPDImain(client_name, sender_name)
    intersection = checkintersection(comparec, client_name)

    final_ans = {}
    for x in intersection:
        label_map = {}
        label_set = set()
        for fname in [client_name, sender_name]:
            for j, data in enumerate(ma[fname]):
                if data.startswith(f"{x}||"):
                    label = aa[fname][j]
                    label_map[fname] = label
                    label_set.add(label)
                    break
        if len(label_set) > 1:
            final_ans[x] = label_map

    return render_template('validate.html', final_ans=final_ans, filenames=[sender_name, client_name])

if __name__ == '__main__':
    app.run(debug=True)
