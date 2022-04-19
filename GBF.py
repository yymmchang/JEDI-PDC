from array import array
import hashlib
import string
import random
import time
from phe import paillier


size = 1024
hash = 12
hashs = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384,hashlib.sha512,hashlib.blake2b,hashlib.blake2s,hashlib.sha3_224,hashlib.sha3_256,hashlib.sha3_384,hashlib.sha3_512]
hashs = hashs[:hash]

def show():
    print(f'BF size: {size}')
    print(f'Hash function number: {hash}')


def BF(dataset):
    array = [0] * size
    for data in dataset:
        data1 = data.encode('utf-8')
        secret = int(hashlib.md5(data1).hexdigest(), 16)
        #print(f'secret: {secret}')

        for hash_func in hashs:
            idx = int(hash_func(data1).hexdigest(), 16) % size
            array[idx] += 1
    return array

  
def secret_sahring(secret,share_num):
    share = []
    for i in range(share_num-1):
        a = random.randint(0,secret//share_num)
        share.append(a)
        secret -= a
    share.append(secret)
    return share


  # to convert data with hash functions and set the filter.
def gbf_gen(dataset,pk):
    array = [0] * size
    gbf = [0] * size
    for data in dataset:
        data1 = data.encode('utf-8')
        secret = int(hashlib.md5(data1).hexdigest(), 16)
        #print(f'secret: {secret}')

        emptybit = -1
        finalshare = secret
        for hash_func in hashs:
            idx = int(hash_func(data1).hexdigest(), 16) % size
            if(array[idx]==0):
                if emptybit == -1:
                    emptybit = idx
                    array[idx] +=1
                else:    
                    gbf[idx] = random.randint(0,secret//len(hashs))
                    finalshare -= gbf[idx]
                    array[idx] +=1
            else:
                array[idx] += 1 
                finalshare -= gbf[idx]
        gbf[emptybit] = finalshare
    
    for i in range(size):
        if array[i] == 0:
            gbf[i] = random.randint(0,secret)
        else:
            gbf[i] = pk.encrypt(gbf[i])
    return gbf,array


""" 
data = ['Alice','Bob']
pk,sk = paillier.generate_paillier_keypair()
a, b=gbf_gen(data,pk)
print(a)
print()
print(b)
"""