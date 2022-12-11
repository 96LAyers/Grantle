import wget
from zipfile import ZipFile
import os
import shutil
import hashlib


url = 'https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Algorithm-Validation-Program/documents/shs/shabytetestvectors.zip'
sha = wget.download(url)

zipfile = ZipFile('./shabytetestvectors.zip')
zipfile.extractall(path='./scratch')

hash_list = []

def removeprefix(string, prefix):
    if prefix in string:
        return string[len(prefix):]
    else:
        return LookupError

# Parse lines of file into dict
file = open('./scratch/shabytetestvectors/SHA256ShortMsg.rsp', 'r')
lines = file.readlines()
for line in lines:
    if 'Len' in line.strip():
        el={}
        index = lines.index(line)
        el['Len'] = int(removeprefix(line,'Len = '))
        print(el['Len'])
        if el['Len'] == 0:
            el['Msg'] = ''
        else:
            el['Msg'] = removeprefix(lines[index+1].strip(),'Msg = ')
        el['MD'] = removeprefix(lines[index+2].strip(),'MD = ')
        hash_list.append(el)

print(hash_list)
# check digest is the same as hashed message
count = 0
for entry in hash_list:
    msg = entry['Msg']
    msg = bytes.fromhex(msg)
    digest = hashlib.sha256(msg).hexdigest()
    digest = digest
    print(digest)
    print(entry['MD'])
    count += 1
    md = entry['MD']
    assert digest in entry['MD'], f'Hash not a match at pos: {count}, expected {digest}, returned {md}'


print(hash_list[56])

os.remove('shabytetestvectors.zip')
shutil.rmtree('./scratch/shabytetestvectors')
