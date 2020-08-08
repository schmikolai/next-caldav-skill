import os
from getpass import getpass

host = input("CalDAV Adress: ")
uname = input("Username: ")
pword = getpass("Password: ")
if uname and pword and host:
    dirname = os.path.dirname(__file__)
    f = open(os.path.join(dirname, ".env"), "w")
    f.write("CALDAV_ADRESS={}\n".format(host))
    f.write("UNAME={}\n".format(uname))
    f.write("PWORD={}".format(pword))
    f.close()