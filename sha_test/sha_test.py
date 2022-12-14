import wget
from zipfile import ZipFile
import os
import shutil
import hashlib

# Define removeprefix function
def removeprefix(string, prefix):
            if prefix in string:
                return string[len(prefix):]
            else:
                return LookupError
'''
# Download zip file from internet                
url = 'https://csrc.nist.gov/CSRC/media/Projects/Cryptographic-Algorithm-Validation-Program/documents/shs/shabytetestvectors.zip'
sha = wget.download(url)

# Unzip zip file to scratch folder
zipfile = ZipFile('./shabytetestvectors.zip')
zipfile.extractall(path='./scratch')
'''
# rsp_parser class
class rsp_parser:
    
    def __init__(self, rsp_test):

        self.rsp_test = rsp_test     
        
    # Define parse method
    def parse(self):
    # Parse lines of file into dict
        hash_list = []
        file = open(f'./scratch/shabytetestvectors/{self.rsp_test}', 'r')
        lines = file.readlines()
        for line in lines:
            if 'Len' in line.strip():
                el={}
                index = lines.index(line)
                el['Len'] = int(removeprefix(line,'Len = '))
                # Check for first Len 
                if el['Len'] == 0:
                    el['Msg'] = ''
                else:
                    el['Msg'] = removeprefix(lines[index+1].strip(),'Msg = ')
                el['MD'] = removeprefix(lines[index+2].strip(),'MD = ')
                hash_list.append(el)

            # check digest is the same as hashed message
            count = 0
            for entry in hash_list:
                msg = entry['Msg']
                msg = bytes.fromhex(msg)
                digest = hashlib.sha256(msg).hexdigest()
                digest = digest
                count += 1
                md = entry['MD']
                assert digest in entry['MD'], f'Hash not a match at pos: {count}, expected {digest}, returned {md}'


sha_short256 = rsp_parser('SHA256ShortMsg.rsp')
sha_short256.parse()

sha_long256 = rsp_parser('SHA256LongMsg.rsp')
sha_long256.parse()
'''
os.remove('shabytetestvectors.zip')
shutil.rmtree('./scratch/shabytetestvectors')
'''