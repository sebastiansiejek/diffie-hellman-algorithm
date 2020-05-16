from DH import DH

a = DH(23, 5).setPrivateKey(6)
b = DH(23, 5).setPrivateKey(15)

a.setForeignKey(b.sharedKey)
b.setForeignKey(a.sharedKey)

print(a.sessionKey)
print(b.sessionKey)
