
import hashlib
import binascii
import sys

starting = 'cxdnnyjw'
#input = "abc"

password = list("********")
idx = -1
found = 0
while True:
    idx += 1

    hash_input = '{}{}'.format(starting, idx)

    hashed_bin = hashlib.md5(hash_input).digest()

    hex = binascii.hexlify(hashed_bin)

    if hex[:5] == '00000':
        print hex

        try:
            pos = int(hex[5])
        except:
            continue
        if pos > 7:
            continue
        
        if password[pos] == '*':
            password[pos] = hex[6]
            found += 1
            print password

    if found == 8:
        break


print "".join(password)
