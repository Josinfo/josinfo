#!/usr/bin/python
aclNum = (input("What is the IPv4 ACL number? "))

if not aclNum.isnumeric():
    print("Valor precisa ser numerico")

elif int(aclNum) >= 1 and int(aclNum) <= 99:
    print("This is a standard IPv4 ACL.")
elif int(aclNum) >=100 and int(aclNum) <= 199:
    print("This is an extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")
