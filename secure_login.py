import getpass

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

if username == "admin" and password == "12345":
    print("Login Successful")
else:
    print("Login Failed")