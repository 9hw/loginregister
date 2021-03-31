#start
 
users = {}
status = ""
 
def displayMenu():
    status = input("[Login & Register] Are you registered user? yes/no?")
    if status == "yes":
        oldUser()
    elif status == "no":
        newUser()
 
def newUser():
    createLogin = input("[Login & Register] Create your username!: ")
 
    if createLogin in users:
        print("[Login & Register] Login name already exist!")
    else:
        createPassw = input("[Login & Register] Create password: ")
        users[createLogin] = createPassw
        print("[Login & Register] User created")
 
def oldUser():
    login = input("[Login & Register] Enter login name: ")
    passw = input("[Login & Register] Enter password: ")
 
    if login in users and users[login] == passw:
        print("[Login & Register] Login successful!")
    else:
        print("[Login & Register] User doesn't exist or wrong password!")
 
while status != "q":
    displayMenu()
    
#end


#By Weez [github.com/9hw]
