aclNum = input("Qual é o numero da acl IPv4?: ")
if not aclNum.isnumeric():
    print("ENTRADA INVALIDA")
elif int (aclNum) >=1 and int(aclNum) <=99:
    print("Essa é uma acl Standard IPv4")
elif int(aclNum) >= 100 and int(aclNum) <=199:
    print("Essa é uma acl Extended IPv4")
else:
    print("Isso nao e ACL")