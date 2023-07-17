MINIMUM = 0
password = input("Password: ")

while password <= MINIMUM:
    print("Invalid password")
    password = input("Password: ")

print(len(password) * "*")