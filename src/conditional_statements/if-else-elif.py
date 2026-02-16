def login(role):
    if role=="Admin":
        print("Admin Logged in")
    elif role=="DE-Intern":
        print("Data Engineering Intern Logged in")
    elif role=="Associate":
        print("Associate Logged In")
    else:
        print("Guest Logged In")

login("Admin")
