
#   Developer:  Cheng, Jeff
#   Date:       10/31/2022
#   Version:    1.1

import array as arr
import random as rng
from pathlib import Path as path

#   reference
#   https://www.pythonpip.com/python-tutorials/python-create-file-if-not-exists/

PASSWD_LENGTH = 12;

DIGITS = [ 
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 
            ]
UPPERS = [ 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z'
            ]
LOWERS = [ 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z'
            ]
SYMBOLS = [
            '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<'
           ]
WORDBANK = DIGITS + UPPERS + LOWERS + SYMBOLS

myfile = path( 'output.txt' )
myfile.touch( exist_ok=True )
file = open( myfile, 'w' )

init_passwd = rng.choice( DIGITS ) + rng.choice( UPPERS ) + rng.choice( LOWERS ) + rng.choice( SYMBOLS )

for unicode in range( PASSWD_LENGTH - 4 ):
    init_passwd = init_passwd + rng.choice( WORDBANK )
    init_password_list = arr.array( 'u', init_passwd )
    rng.shuffle( init_password_list )    

passwd = ""
for unicode in init_password_list:
    passwd += unicode
    
file.write( passwd )
file.close()