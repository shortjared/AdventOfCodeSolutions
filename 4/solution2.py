import hashlib

INPUT = 'bgvyzdsv'

md5_hash = 'H0H0H0'
MERRY_CHISTMAS = '00000'
MORE_MERRINESS = '0'

MERRIER_CHISTMAS = MERRY_CHISTMAS + MORE_MERRINESS

current_key = -1
while md5_hash[0:6] != MERRIER_CHISTMAS:
    current_key += 1
    md5_hash = hashlib.md5(INPUT + str(current_key)).hexdigest()

print(current_key)
