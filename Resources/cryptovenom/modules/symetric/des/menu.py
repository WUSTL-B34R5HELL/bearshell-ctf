#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#     | ATTENTION!: THIS SOFTWARE IS PART OF THE "CRYPTOVENOM FRAMEWORK" |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               / CREATED BY LOCKEDBYTE /
#
#                  [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ]
#                  [ CONTACT => @LockedByte (Twitter) ]
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#

from main import *
from bruteforce import *
import random

def stringRandom(lenght):
    out = ''
    for i in range(0, lenght):
        out = out + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890=)(/&%$#@!|\-+}{][+*_:;.,<>')
    return out

print('''

-=[OPTIONS]=-

   1) Encrypt
   2) Decrypt
   3) Brute Force
   
''')

opt = input('\033[1;34m[=]\033[0m Option: ')


if opt == '1':


    opt2 = input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
    
        importx = 'file'
        exportx = 'file'
        
        raw = ''
        
        infile = input('\033[1;34m[=]\033[0m Input file path: ')
        outfile = input('\033[1;34m[=]\033[0m Output file path: ')
    
    
    elif opt2 == 't' or opt2 == 'T':
    
        importx = 'print'
        exportx = 'print'
        infile = ''
        outfile = ''
        
        raw = input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    type1 = input('\033[1;34m[=]\033[0m Encryption Type (eg.: ebc): ')
        
    
    print('''
    
-=[OPTIONS]=-
    
   1) Random IV (First Bytes)
   2) Random IV (Last Bytes)
   3) Custom IV
   4) No IV
   
   ''')
    
    ivtype = input('\033[1;34m[=]\033[0m Option: ')
    
    if ivtype == '1':
    
        ivtype = 'randomstart'
        iv = stringRandom(16)
    
    elif ivtype == '2':
    
        ivtype = 'randomend'
        
        iv = stringRandom(16)
    
    elif ivtype == '3':
    
        ivtype = 'custom'
        iv = input('\033[1;34m[=]\033[0m Custom IV: ')
    
    elif ivtype == '4':
    
        ivtype = 'noiv'
        iv = ''
   
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
    
    keyimport = input('\033[1;34m[=]\033[0m Key Encoding Import (eg.: raw or base64): ')
    

    passwd = input('\033[1;34m[=]\033[0m Key: ')
    
    format1 = input('\033[1;34m[=]\033[0m Output encoding (eg.: raw or base64): ')

    out = encryptDes(type1, importx, infile, exportx, outfile, format1, ivtype, iv, passwd, raw, keyimport)
    
    print('\033[1;32m[+]\033[0m Out = ' + str(out))
    print('\033[1;32m[+]\033[0m All done!')


elif opt == '2':


    opt2 = input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
    
        importx = 'file'
        exportx = 'file'
        
        raw = ''
        
        infile = input('\033[1;34m[=]\033[0m Input file path: ')
        outfile = input('\033[1;34m[=]\033[0m Output file path: ')
    
    
    elif opt2 == 't' or opt2 == 'T':
    
        importx = 'print'
        exportx = 'print'
        infile = ''
        outfile = ''
        
        raw = input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    type1 = input('\033[1;34m[=]\033[0m Encryption Type (eg.: ebc): ')
        
    format1 = input('\033[1;34m[=]\033[0m Input format (Eg.: raw or base64): ')
    
    print('''
    
-=[OPTIONS]=-
    
   1) Random IV (First Bytes)
   2) Random IV (Last Bytes)
   3) Custom IV
   4) No IV
   
   ''')
    
    ivtype = input('\033[1;34m[=]\033[0m Option: ')
    
    if ivtype == '1':
    
        ivtype = 'randomstart'
        iv = stringRandom(16)
    
    elif ivtype == '2':
    
        ivtype = 'randomend'
        
        iv = stringRandom(16)
    
    elif ivtype == '3':
    
        ivtype = 'custom'
        iv = input('\033[1;34m[=]\033[0m Custom IV: ')
    
    elif ivtype == '4':
    
        ivtype = 'noiv'
        iv = ''
   
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
    

    passwd = input('\033[1;34m[=]\033[0m Key: ')

    out = decryptDes(type1, importx, infile, exportx, outfile, format1, ivtype, iv, passwd, raw)
    
    print('\033[1;32m[+]\033[0m Out = ' + str(out))
    print('\033[1;32m[+]\033[0m All done!')
    
elif opt == '3':

    print('NOT YET')
    exit()

    opt2 = input('\033[1;34m[=]\033[0m [F]ile or [T]ext: ')
    
    if opt2 == 'f' or opt2 == 'F':
    
        importx = 'file'
        exportx = 'file'
        
        text = ''
        
        infile = input('\033[1;34m[=]\033[0m Input file path: ')
        outfile = input('\033[1;34m[=]\033[0m Output file path: ')
    
    
    elif opt2 == 't' or opt2 == 'T':
    
        importx = 'print'
        exportx = 'print'
        infile = ''
        outfile = ''
        
        text = input('\033[1;34m[=]\033[0m Text: ')
    
    
    else:
    
        print('\033[1;31m[-]\033[0m Unknown option')
        exit()
        
    dic = input('\033[1;34m[=]\033[0m Dictionary path: ')

    bf(ct, dic) # REVISAR ESTO ----------------------------------------------------------------------------------

else:

    print('\033[1;31m[-]\033[0m Unknown option')
    exit()
