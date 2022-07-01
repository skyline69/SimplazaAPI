from time import sleep
from sys import stdout

for x in "loading...":
    print(x, end='')
    stdout.flush()
    sleep(.05)



from simplaza import Simplaza
from os import name as osname
from subprocess import call as spcall
from ctypes import windll

windll.kernel32.SetConsoleTitleW("SimplazaCLI by @skyline69")

def shell_logo(): return Simplaza().logo+'\n\033[90mTip: type "help" to see a list of features.\033[0m\n\n'
print(shell_logo())

def get_list() -> list[str]: return [Simplaza.get_homepage(DATATYPE="format", length=e) for e in range(Simplaza.get_homepage(list_len=True))]
def clear() -> str | None:
    if osname == "posix": spcall(["clear"],shell=True)
    else: spcall(["cls"],shell=True)
    print(shell_logo())

clear()

def help_msg():
    return """
//==========[]=====================================\\
|| \033[92mCommand\033[0m  ||               \033[93mAction\033[0m                ||
|]==========[]=====================================[|
|| help     || display this message                ||
|| homepage || display the homepage in the console ||                                                               
|| ping     || show ping of the simplaza website   ||
|| clear    || clear shell screen                  ||
\\\==========[]=====================================//  
                                                      \033[93m__\033[0m
                                                    \033[93m<(o )___\033[0m
                                                     \033[93m( ._> /\033[0m
                                                      \033[93m`---'\033[0m   
    """
def unknown_cmd(COMMAND:str) -> str: return '\033[91mUnknown command:\033[0m \033[01m"%s"\033[0m'% COMMAND



try:
    while True:
        shell_inp:str = str(input("\033[94m>>\033[0m "))

        if shell_inp == "clear": clear()


        elif shell_inp == "homepage":
            print("\n", end=None)
            for e in range(Simplaza.get_homepage(list_len=True)):
                print(get_list()[e])

        elif shell_inp == "ping":
            print(Simplaza.ping())

        elif shell_inp == "help": print(help_msg())

        else: print(unknown_cmd(shell_inp))

        print("\033[0m",end="")

except KeyboardInterrupt:
    print("\n\ngoodbye! \033[93m:)\033[0m")
    exit()

except EOFError:
    print("\n\ngoodbye! \033[93m:)\033[0m")
    exit()