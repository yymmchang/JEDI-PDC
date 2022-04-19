from GBF import gbf_gen, BF,show

import hashlib
import random
import time
from phe import paillier


class Server:
    def __init__(self,data):
        self.data=data
    
class Party:
    def __init__(self,data):
        self.data=data  

class Client:
    def __init__(self,data):
        self.data=data
        

def import_data(filename):
    f = open(filename,'r')
    r = f.readlines()
    f.close()
    return r

def gbf_merge(gbf1,gbf2,c1,c2):
    gbf_1n2 =  [0] * len(gbf1)
    c_1n2 = [0] * len(gbf1)
    for i in range(len(gbf1)):
        if c1[i]!=0 and c2[i]!=0:
            gbf_1n2[i] = gbf1[i]+gbf2[i]
            c_1n2[i] = c1[i]+c2[i]
        elif c1[i]==0 and c2[i]!=0:
            gbf_1n2[i] = gbf2[i]
            c_1n2[i] = c2[i]
        elif c1[i]!=0 and c2[i]==0:
            gbf_1n2[i] = gbf1[i]
            c_1n2[i] = c1[i]
        else:
            gbf_1n2[i] = random.randint(0,9999)
    return gbf_1n2 ,c_1n2

def compare(c_1n2,bf):
    c_1n2nu = [0] *len(c_1n2)
    for i in range(len(c_1n2)):
        if bf[i] >= 1 and c_1n2[i] >= bf[i]:
            c_1n2nu[i]=1
    return c_1n2nu

def verify(gbf_1n2,c_1n2nu):
    tmp = 0
    for i in range(len(c_1n2nu)):
        if c_1n2nu[i] == 1:
            tmp += gbf_1n2[i]
    #print(f'tmp: {tmp}')
    #print(type(tmp))
    return tmp

if __name__ == '__main__':
    time_start = time.time()
    party = 0

    ## Party_one
    one_data = import_data('name1.txt')
    one = Party(one_data)
    party+=1
    #print(f'one.data: {one.data}')
    ma_1 = []
    for i in one.data:
        ma_1.append(i.strip().split(',')[0])
    print(f'ma_1: {ma_1}         ma_num: {len(ma_1)}')
    pk1,sk1 = paillier.generate_paillier_keypair()
    gbf1,c1 = gbf_gen(ma_1,pk1)
    #print(f'gbf1: {gbf1}')
    #print(f'c1: {c1}')

    ## Party_two
    two_data = import_data('name2.txt')
    two = Party(two_data)
    party+=1
    #print(f'two.data: {two.data}')
    ma_2 = []
    for i in two.data:
        ma_2.append(i.strip().split(',')[0])
    print(f'ma_2: {ma_2}         ma_num: {len(ma_2)}')
    gbf2,c2 = gbf_gen(ma_2,pk1)
    #print(f'gbf2: {gbf2}')
    #print(f'c2: {c2}')

    ## Party_three
    three_data = import_data('name3.txt')
    three = Party(three_data)
    party+=1
    #print(f'three.data: {three.data}')
    ma_3 = []
    for i in three.data:
        ma_3.append(i.strip().split(',')[0])
    print(f'ma_3: {ma_3}         ma_num: {len(ma_3)}')
    gbf3,c3 = gbf_gen(ma_3,pk1)
    #print(f'gbf3: {gbf3}')
    #print(f'c3: {c3}')


    ## Client
    c_data = import_data('namec.txt')
    client = Client(c_data)
    #print(f'client.data: {client.data}')
    ma_c = []
    for i in client.data:
        ma_c.append(i.strip().split(',')[0])
    print(f'ma_c: {ma_c}         ma_num: {len(ma_c)}')
    bf = BF(ma_c)
    #print(f'bf: {bf}')

    ## Merge
    gbf_1n2 ,c_1n2 = gbf_merge(gbf1,gbf2,c1,c2)
    gbf_1n2 ,c_1n2 = gbf_merge(gbf_1n2,gbf3,c_1n2,c3)
    #print(f'gbf_1n2: {gbf_1n2}')
    #print(f'c_1n2: {c_1n2}')

    ## Compare
    c_1n2nu = compare(c_1n2,bf)
    #print(f'c_1n2nu: {c_1n2nu}')


    enc_massage = verify(gbf_1n2, c_1n2nu)
    
    dec_message = sk1.decrypt(enc_massage)

    #print("dec_message: ",dec_message/party)

    time_end = time.time()
    print(f'Time: {time_end-time_start}')


    ans_verify = 0
    for i in range(len(ma_c)):
        data = ma_c[i]
        data1 = data.encode('utf-8')
        ans_verify += int(hashlib.md5(data1).hexdigest(), 16)
    #print(f'ans_verify: {ans_verify}')
    if ans_verify == dec_message//party:
        print('Verify result: Succeed')
    else:
        print('Verify result: Failed')

    print(f'Party number: {party}')
    show()