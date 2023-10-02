password = input("Make a password    >   ")

if len(password) < 8:
    print("Your password is too short")

else:
    print(f"{password}")

