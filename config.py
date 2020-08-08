from getpass import getpass

uname = input("Username: ")
pword = getpass("Password: ")
if uname and pword:
    f = open(".env", "w")
    f.write("UNAME={}\n".format(uname))
    f.write("PWORD={}".format(pword))
    f.close()