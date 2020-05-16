import sys
from DH import DH
from random import randint

a = DH(sys.maxsize - 1, 5).setPrivateKey(randint(0, 99999))
b = DH(sys.maxsize - 1, 5).setPrivateKey(randint(0, 88888))

a.setForeignKey(b.sharedKey)
b.setForeignKey(a.sharedKey)

print(a.sessionKey)
print(b.sessionKey)
