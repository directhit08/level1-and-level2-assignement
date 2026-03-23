username = input("Enter your username: ")
password = input("Enter your password: ")

Admin = "adminKE"
passwordAdmin = "254Secure"

if username != Admin and password != passwordAdmin:
    print("Access granted!")
else:    
    print("Invalid Credentials!")