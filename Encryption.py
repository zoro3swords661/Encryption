try:
    import bcrypt
except ImportError:
    print("Missing required module: bcrypt")
    print("Install it with: python -m pip install bcrypt")
    raise

print("1. Generate salt hash and check password")
print("2. Exit Program")

while True:
    user_choice = input("Choose a option: ")

    if user_choice == "1":
        input_user = input("Enter your username: ")
        input_passwd = input("Enter your password: ")

        password = input_passwd.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        print("The salted hash is:", hashed_password)

        check_password = input("Re-enter the password to check: ")
        check_password = check_password.encode('utf-8')

        if bcrypt.checkpw(check_password, hashed_password):
            print("Login success")
        else:
            print("Incorrect password")

    elif user_choice == "2":
        print("Quitting the Program...")
        break

    else:
        print("Please choose a correct option")