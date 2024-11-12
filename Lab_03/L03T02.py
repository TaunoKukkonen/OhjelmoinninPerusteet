#Tee ohjelma, joka kysyy käyttäjältä 3 kokonaislukua ja tulostaa niistä suurimman.

num1=int(input("Anna kokoluku "))

num2=int(input("Anna kokoluku "))

num3=int(input("Anna kokoluku "))


if num1>num2 and num1>num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)