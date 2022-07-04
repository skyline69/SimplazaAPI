from functools import lru_cache
from time import sleep
from sys import stdout
from typing import NoReturn
from os import name as osname
from warnings import filterwarnings
from subprocess import call as spcall
from ctypes import windll


filterwarnings("ignore")

if osname == "posix": spcall(["clear"],shell=True)
else: spcall(["cls"],shell=True)


for x in "\033[01m\033[07m\033[36mloading...\033[0m":
    print(x, end='')
    stdout.flush()
    sleep(.01)

from simplaza import Simplaza

def clear() -> str | None:
    if osname == "posix": spcall(["clear"],shell=True)
    else: spcall(["cls"],shell=True)
    print(shell_logo())

windll.kernel32.SetConsoleTitleW("SimplazaCLI by @skyline69")

def shell_logo(): return Simplaza().logo+'\n\033[90mTip: type "help" to see a list of features.\033[0m\n\n'
print(shell_logo())


@lru_cache(maxsize=32)
def get_list() -> list[str]: return [Simplaza.get_homepage(DATATYPE="format", length=e) for e in range(Simplaza.get_homepage(list_len=True))]


clear()

def help_msg():
    return """
//=================[]=================================================\\\\
||     \033[92mCommand\033[0m     ||                      \033[93mAction\033[0m                     ||
|]=================[]=================================================[|
|| help            || display this message                            ||
|| homepage        || display the homepage in the console             ||
|| ping            || show ping of the simplaza website               ||
|| path            || show given community path in config.json file   ||
|| exit            || exit this program                               ||
|| clear           || clear shell screen                              ||
|| checkupdates    || check simplaza plane updates                    ||
\\\=================[]=================================================//  
  
  \033[04m\033[37mContacts\033[0m
                                     \033[93m__\033[0m       
  \033[35mGithub: skyline69\033[0m                \033[93m<(o )___\033[0m  
  \033[95mInstagram: @skyline.rno263\033[0m        \033[93m( ._> /\033[0m              
                                     \033[93m`---'\033[0m
                                                                     
"""
def unknown_cmd(COMMAND:str) -> str: return '\033[91mUnknown command:\033[0m \033[01m"%s"\033[0m'% COMMAND

def exit_prog() -> NoReturn:
    print("\ngoodbye! \033[93m:)\033[0m")
    exit()


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

        elif shell_inp == "path": 
            if Simplaza.check_community() == "new-file-created": 
                print("\033[93m- Config file not found.\n- Created new config.json file.\nUse 'path' command again to check community path.\033[0m")

            elif Simplaza.check_community() == "broken-file":
                print("\033[93m- Config file is corrupt.\n- Created new config.json file.\nUse 'path' command again to check community path.\033[0m")
            else: 
                if Simplaza.check_community() == "here comes the path for the community folder" or Simplaza.check_community().startswith("here"): 
                    print("\033[31mno community path given!\033[0m")

                else: print("Path: %s" % Simplaza.check_community())

        elif shell_inp == "exit": exit_prog()
        
        elif shell_inp == "checkupdates": print("coming soon...")
        elif shell_inp == "help": print(help_msg())

        else: print(unknown_cmd(shell_inp))

        print("\033[0m",end="")

except KeyboardInterrupt: exit_prog()
except EOFError: exit_prog()
