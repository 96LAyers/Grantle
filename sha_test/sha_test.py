import wget
from zipfile import ZipFile
import os
import shutil
import hashlib

'''
url = 'https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Algorithm-Validation-Program/documents/shs/shabytetestvectors.zip'
sha = wget.download(url)

zipfile = ZipFile('./shabytetestvectors.zip')
zipfile.extractall(path='./scratch')
'''
hash_list = []
el = {}

# Parse lines of file into dict
file = open('./scratch/shabytetestvectors/SHA256ShortMsg.rsp', 'r')
for line in file.readlines():
    if 'Len' in line.strip():
        el['Len'] = line[len('Len = '):-1]
    elif 'Msg' in line.strip():
        el['Msg'] = line[len('Msg = '):-1]
    elif 'MD' in line.strip():
        el['MD'] = line[len('MD = '):-1]
        hash_list.append(el)
        el = {}
        

# check digest is the same as hashed message
count = 0
for entry in hash_list:
    msg = entry['Msg']
    digest = hashlib.sha256(msg.encode('utf-8')).hexdigest()
    print(digest)
    count += 1
    if digest != entry['MD']:
        print('Hash not a match at pos: {}'.format(count))


print(hash_list[56])

'''
os.remove('shabytetestvectors.zip')
shutil.rmtree('./scratch/shabytetestvectors')

'''