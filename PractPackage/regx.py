import re
s = input("Enter string to be matched : \n")
str = "efi qeifqwpr'tuqwptuwpo wefowepf w eif efig4y83495 al qp9ty IT P94YT"

matcher = re.finditer("^"+s, str)
for match in matcher:
    print(match.start())