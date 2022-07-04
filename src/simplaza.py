from typing import Literal
from cloudscraper import create_scraper
from bs4 import BeautifulSoup
from functools import lru_cache
from datetime import date
from asyncio import run as arun
from ping3 import ping
from os.path import exists
from json import dump, loads
from json.decoder import JSONDecodeError
from threading import Thread
from time import sleep as tsleep


__version__ = "v0.0.1-dev"

class Simplaza:
    """Unofficial Simplaza API\n
    by @skyline69"""
    
    def __init__(self):
        self.version = __version__
        self.logo = f"""\033[92m
\033[94m   _____  _                    _                     \033[92m _____  _       _____ 
\033[94m  / ____|(_)                  | |                   \033[92m / ____|| |     |_   _|
\033[94m | (___   _  _ __ ___   _ __  | |  __ _  ____ __ _  \033[92m| |     | |       | |  
\033[94m  \___ \ | || '_ ` _ \ | '_ \ | | / _` ||_  // _` | \033[92m| |     | |       | |  
\033[94m  ____) || || | | | | || |_) || || (_| | / /| (_| | \033[92m| |____ | |____  _| |_ 
\033[94m |_____/ |_||_| |_| |_|| .__/ |_| \__,_|/___|\__,_|  \033[92m\_____||______||_____|\033[0m
                      \033[94m | |                                                 
                     \033[94m  |_|      \033[0m                                \033[90m{self.version}\033[0m       
    """

    if not exists("./config.json"):
        with open("config.json", "w+") as f_:

            CONIGDATA:dict[str,str] = {
                "path":"here comes the path for the community folder"
            }
            dump(CONIGDATA, f_)
        print("\n- config.json was not found so a new config.json file was created")
        tsleep(2)
    
    def check_create_config() -> None:
        if not exists("./config.json"):
            with open("config.json", "w+") as f_:

                CONIGDATA:dict[str,str] = {
                    "path":"here comes the path for the community folder"
                }
                dump(CONIGDATA, f_)

    def create_config() -> None:
        with open("config.json", "w+") as f_:
            CONIGDATA:dict[str,str] = {
                "path":"here comes the path for the community folder"
            }
            dump(CONIGDATA, f_)


    @lru_cache(maxsize=2, typed=True)
    async def data() -> str: 
        scraper = create_scraper()
        return scraper.get("https://simplaza.org/").text

    soup = BeautifulSoup(arun(data(), debug=False), features="html.parser")


    postdivs = soup.findAll("article", id=lambda value: value and value.startswith("post-"))
    current_year = date.today().year
    def ping() -> str: return "Time: \033[93m{:.2f}s\033[0m".format(ping("simplaza.org"))

    def get_homepage(DATATYPE:str=None, length:int=0, list_len:bool=False) -> (str | int | dict[int, str]):   # use "print(Simplaza.get_homepage.__doc__)" to get more information about this Function
        
        """Function: get_homepage()\nCurrently available datatypes: json, format\nArguments: *DATATYPE(str), length(int), list_len(bool)\n\n* = required\n"""
        if DATATYPE == "format":
            posts = Simplaza.postdivs[length].findAll("h2", class_="blog-entry-title entry-title")
            posts_meta_list = Simplaza.postdivs[length].find("ul", class_="nv-meta-list").find("li", class_="meta date posted-on")
            posts_date = posts_meta_list.find("time", class_="entry-date published").text

            link_post = posts[0].find("a",href=True)["href"]
            return ("\033[93m%i. \033[36m%s\033[0m  •  \033[90m%s\033[0m\nLink: \033[34m%s\n" % (length+1, (posts[0].find("a").text), 
            (posts_date), ( link_post)) + "\033[90m="*len("Link: "+link_post)+"\033[0m")

        elif list_len: return len(Simplaza.postdivs)

        elif DATATYPE == "json":
            if isinstance(length,str): raise(TypeError("Length must be a number!(int)"))
            elif isinstance(length,float): raise(TypeError("Length must be a whole number!(int)"))

            posts = Simplaza.postdivs[length].findAll("h2", class_="blog-entry-title entry-title")

            return ({length:str(posts[0].find("a").text)})

        else: raise(TypeError("Unvalid datatype at get_homepage()"))

    def check_community() -> (Literal["new-file-created","broken-file"] | None):
        try:
            with open("config.json", "r") as f:
                CONFIG_DATA:str = loads(f.read())["path"]

            return CONFIG_DATA

        except FileNotFoundError: 
            Thread(target=Simplaza.check_create_config, args=()).start()
            return "new-file-created"

        except JSONDecodeError:
            Thread(target=Simplaza.create_config, args=()).start()
            return "broken-file"
