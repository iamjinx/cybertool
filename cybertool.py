# - > CYBERTOOL is a Password Generating and converting tool.
# - > This tool also can check pwned / leaked passwords using an API.
# - > Created by @iamjinx

import os, random, string, requests, hashlib

os.system('cls||clear')

List = (('s', '$'), ('S', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('O', '0'),
        ('i', '1'), ('I', '|'), ('A', '4'), ('H', '#'), ('h', '#'), ('r', '₹'), ('R', '₹'), ('E', '3'))

# - > USED COLORS
RESET = "\033[0m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
WHITE = "\033[1;37m"
SUC = "\033[0;37m" + "\033[42m"
ERR = "\033[0;37m" + "\033[41m"
THANKS = "\033[0;37m" + "\033[44m"


def passgen():
    chars = (string.ascii_letters + string.digits + string.punctuation)
    charslist = [i for i in chars]
    genlist = []
    random.shuffle(charslist)
    print(f"{ERR}\n›› Enter the length of password : {RESET}", end=' ')
    pwlen = int(input())

    for i in range(pwlen):
        x = random.choice(charslist)
        genlist.append(x)

    random.shuffle(genlist)
    generatedpassword = ''.join(genlist)

    return generatedpassword


def consecpass(data):
    x = random.randint(100, 1000)
    for (i, j) in List:
        data = data.replace(i, j)
    return data + str(x)

def chkpwnedpw(password):
    NOL = 0
    HASHEDPASS = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    F5C , END = HASHEDPASS[:5], HASHEDPASS[5:]
    URL = "https://api.pwnedpasswords.com/range/" + F5C

    RES = requests.get(URL)
    if RES.status_code != 200:
        print(f"Error Fetching : {RES.status_code} ! Check the API & try again...")

    HASHLIST = (line.split(':') for line in RES.text.splitlines())
    for hash, count in HASHLIST:
        if hash == END:
            NOL = count

    if NOL:
        print(f"\n{WHITE}{password} {RED}has pwned {WHITE}{NOL} {RED}times. Change your password ASAP !{RESET}")
    else:
        print(f"\n{WHITE}{password} {GREEN}is not leaked yet.{RESET}")


HEADER = r"""
  _______  __ ___   ____ ___  ______ ____   ____   __ 
 / ___/\ \/ // _ ) / __// _ \/_  __// __ \ / __ \ / / 
/ /__   \  // _  |/ _/ / , _/ / /  / /_/ // /_/ // /__
\___/   /_//____//___//_/|_| /_/   \____/ \____//____/
"""

if __name__ == '__main__':
    print(f"{GREEN}{HEADER}")
    print(f"{WHITE}1. Generate password ")
    print(f"{WHITE}2. Convert to strong password  ")
    print(f"{WHITE}3. Check pwned passwords ")

    print(f"{SUC}\n›› Choose an option {RESET}", end=' ')
    user_opt = input()
    if  user_opt == '1':
        x = passgen()
        print(
            f"{SUC}\n›› Your generated password : {RESET}", end=' ')
        print(f"{WHITE}{x}\n")
        print(f"{THANKS}\n›› THANKS FOR USING OUR TOOL {RESET}\n\n")
    elif  user_opt == '2':
        print(f"{ERR}\n›› Enter password : {RESET}", end=' ')
        user = input()
        secpass = consecpass(user)
        print(f"{SUC}\n›› Your Secured Password : {RESET}", end=' ')
        print(f"{WHITE}{secpass}\n")
        print(f"{THANKS}\n›› THANKS FOR USING OUR TOOL {RESET}\n\n")
    elif  user_opt == '3':
        print(f"{ERR}\n›› Enter password : {RESET}", end=' ')
        pw = input()
        try:
            chkpwnedpw(pw)
            print(f"{THANKS}\n›› THANKS FOR USING OUR TOOL {RESET}\n\n")
        except:
            print(f"{ERR}\n Internet Connection Failed ! \n\n{RESET}")
    else:
        print(f'{ERR}\n›› Invalid Option {RESET}\n')