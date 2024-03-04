import random
chars="ZXCVBNMLKJHGFDSAQWERTYUIOPqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_<>,.:"

while 1:
    password_len = int(input("Enter the length of password:"))
    password_count = int(input("Enter the passwords would you like:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      =  password + password_char
        print("Here is Your Password : " ,password)
        