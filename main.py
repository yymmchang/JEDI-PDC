from unicodedata import name
from xml.dom.expatbuilder import InternalSubsetExtractor
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
from phe import paillier
import hashlib

from GBF import gbf_gen, BF,hashs, size
from PPDI import gbf_merge, compare, verify


app = Flask(__name__)
ALLOWED_EXTENSIONS = set(['txt', 'jpg'])
UPLOAD_FOLDER = 'C:\\Users\\CISLAB\\Desktop\\web'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB


pk, sk = paillier.generate_paillier_keypair()
filenamesss = []
files = {}
ma = {}
aa = {}
gbf = {}
c = {}
mergegbf = [0] * size
mergec = [0] * size


def import_data(filename):
    f = open(filename, 'r')
    r = f.readlines()
    f.close()
    return r


def preprocess(filename):
    print(f'preprocess___{filename}')
    tmp = []
    tmp1 = []
    for i in files[filename]:
        tmp.append(i.strip().split(',')[0])
        tmp1.append(i.strip().split(',')[1])
    ma[filename] = tmp
    aa[filename] = tmp1
    gbf1, c1 = gbf_gen(ma[filename], pk)
    gbf[filename] = gbf1
    c[filename] = c1 


def checkans(dec_message,cname):
    ans_verify = 0
    namec = cname
    for i in range(len(ma[namec])):
        data = ma[namec][i]
        data1 = data.encode('utf-8')
        ans_verify += int(hashlib.md5(data1).hexdigest(), 16)
    #print(f'ans_verify: {ans_verify}')
    if ans_verify == dec_message//len(filenamesss):
        #print('Verify result: Succeed')
        return 'Verify result: Succeed'
    else:
        #print('Verify result: Failed')
        return 'Verify result: Failed'

def PPDImain(cname):
    global mergegbf, mergec
    for i in range(len(filenamesss)):
        tmp = filenamesss[i]
        mergegbf, mergec = gbf_merge(mergegbf, gbf[tmp], mergec, c[tmp])
    global comparec 
    comparec = compare(mergec, c[filenamesss[-1]])  # (,bf)
    enc_massage = verify(mergegbf, comparec)
    dec_message = sk.decrypt(enc_massage)
    # print(dec_message)
    check_ans = checkans(dec_message,cname)
    return check_ans

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def checkintersection():
    intersection = []
    for data in ma[filenamesss[0]]:     
        data1 = data.encode('utf-8')
        check = 0
        for hash_func in hashs:
            idx = int(hash_func(data1).hexdigest(), 16) % size
            if comparec[idx] ==0:
                check+=1
                break
        if check == 0:
            intersection.append(data)
    print(f'intersection: {intersection}')
    return intersection



@app.route('/')
def index():
    return render_template('index.html', template_folder='./')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    tmp = []
    filenames = []
    if request.method == 'POST':
        uploaded_files = request.files.getlist("file[]")
        tmp = uploaded_files

    for file in tmp:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
            tmp_filename = filename.replace('.txt', '')
            filenamesss.append(tmp_filename)
            data = import_data(filename)
            files[tmp_filename] = data
            preprocess(tmp_filename)
    return render_template('result.html', filenames=filenames)


@app.route('/upload/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/validate', methods=["POST"])
def validate():
    print(request.form.getlist('file'))
    cname = request.form.getlist('file')[0].replace('.txt', '')
    #filenamesss.remove(cname)

    check_ans = PPDImain(cname)
    print(check_ans)
    intersection = checkintersection()

    final_ans = {}
    print(aa)
    for k in intersection: 
        tmp = []
        for i in range(len(filenamesss)):
            idx = ma[filenamesss[i]].index(k)
            tmp.append(aa[filenamesss[i]][idx])
        final_ans[k]= tmp
    print(final_ans)
    return render_template('validate.html', final_ans= final_ans, filenames=filenamesss)
    #return intersection

if __name__ == '__main__':
    app.run()
