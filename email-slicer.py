user_email = input("Please enter your email: ")

user_email = user_email.split("@")

username = user_email[0]
domain = user_email[1]

print("Your username is " + username + " & domain is " + domain)