# This is just a test file to see if I can implement a salted hash using the given Python libraries.

import hashlib
import os
import getpass

p1= getpass.getuser()
p = getpass.getpass()
salt = os.urandom(16)

m = hashlib.md5()
m.update(salt + p)
m.hexdigest()
