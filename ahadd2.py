import hashlib
import requests

the_password = input("Enter your password :")

def check_password(password):
    sha = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    passchr5 = sha[:5] 
    bakpass = sha[5:]
    resp = requests.get(f"https://api.pwnedpasswords.com/range/{passchr5}")
    resp.raise_for_status()
    for line in resp.text.splitlines():
        offcpass, count = line.split(':')
        if offcpass == bakpass:
            return int(count)
    return 0

times = check_password(the_password)

if times:
    print(f"Don't Use it Leaked {times} times")
else:
    print("strong password and not leaked :)")

#عهد عماد جابر
