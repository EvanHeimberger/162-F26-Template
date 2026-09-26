print("Hello! Welcome to the password strength test!")

user_password = input("Please Enter Your Password!")

score = 0
digits = any(char.isdigit) for char in user_password # any() If at least one character is a digit, returns True
special = any(char in string.punctuation for char in user_password) # Checks for special characters. Any() is checking against string.punctuation

if user_password != user_password.upper() #!= means "not equal to"
       score = score + 10

if user_password != user_password.lower()
       score = score + 10

if digits:
       score = score + 10

if special:
       score = score + 10
