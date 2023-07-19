user_login = "mudamuda"
user_pass = "qwerty"

login = input("Login: ")
password = input("Password: ")

if (login == user_login) and (password == user_pass):
    print("Alahamora")
else:
    print("UHODI")

crit1 = "red"
crit2 = "lock"
color = input("Color: ")
feature = input("Feature: ")

if (color == crit1) or (feature == crit2):
    print("Buy it!")
else:
    print("Adios")
