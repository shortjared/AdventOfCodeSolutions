import hashlib

INPUT = 'bgvyzdsv'

md5_hash = 'H0H0H0'
MERRY_CHISTMAS = '00000'

current_key = -1
while md5_hash[0:5] != MERRY_CHISTMAS:
    current_key += 1
    md5_hash = hashlib.md5(INPUT + str(current_key)).hexdigest()

print(current_key)
