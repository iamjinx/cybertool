import random
import string
import colorama
from colorama import *
colorama.init(autoreset=True)

List = (('s', '$'), ('S', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('O', '0'),
        ('i', '1'), ('I', '|'), ('A', '4'), ('H', '#'), ('h', '#'), ('r', '₹'), ('R', '₹'))


def passgen():
    chars = (string.ascii_letters + string.digits + string.punctuation)
    charslist = [i for i in chars]
    genlist = []
    random.shuffle(charslist)
    print(Fore.WHITE+Back.RED+"\n›› Enter the length of password : ", end=' ')
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


if __name__ == '__main__':
    print(Style.BRIGHT+Fore.RED +
          "  _______  __ ___   ____ ___  ______ ____   ____   __ ")
    print(Style.BRIGHT+Fore.RED +
          " / ___/\ \/ // _ ) / __// _ \/_  __// __ \ / __ \ / / ")
    print(Style.BRIGHT+Fore.BLUE +
          "/ /__   \  // _  |/ _/ / , _/ / /  / /_/ // /_/ // /__")
    print(Style.BRIGHT+Fore.BLUE +
          "\___/   /_//____//___//_/|_| /_/   \____/ \____//____/")
    print(Style.BRIGHT+Fore.WHITE +
          "\n1. Generate password          ")
    print(Style.BRIGHT+Fore.WHITE+"2. Convert to strong password ")
    print(Style.BRIGHT+Fore.WHITE+"X. Exit                       ")

    print(f"{Fore.WHITE+Back.GREEN}\n›› Choose an option ", end=' ')
    user_opt = input()
    try:
        if int(user_opt) == 1:
            x = passgen()
            print(
                f"{Fore.WHITE+Back.GREEN}\n›› Your generated password : ", end=' ')
            print(f"{Style.BRIGHT}{x}\n")
        elif int(user_opt) == 2:
            print(Fore.WHITE+Back.RED+"\n›› Enter password : ", end=' ')
            user = input()
            secpass = consecpass(user)
            print(f"{Fore.WHITE+Back.GREEN}\n›› Your Secured Password : ", end=' ')
            print(f"{Style.BRIGHT}{secpass}\n")
        elif (user_opt == 'x') or (user_opt == 'X'):
            exit()
        else:
            print(f'{Fore.WHITE+Back.RED}›› Invalid Option \n')
            exit()
    except ValueError:
        print(f'{Fore.WHITE+Back.RED}›› Invalid Input! \n')
