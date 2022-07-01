from cloudscraper import create_scraper
from bs4 import BeautifulSoup
from functools import lru_cache
from datetime import date
from asyncio import run as arun



__version__ = "v0.0.1-dev"

class Simplaza:
    """Unofficial Simplaza API\n
    by @skyline69"""
    
    def __init__(self):
        self.version = __version__


    @lru_cache(maxsize=2, typed=True)
    async def data() -> str: 
        scraper = create_scraper()
        return scraper.get("https://simplaza.org/").text

    soup = BeautifulSoup(arun(data()), features="html.parser")


    postdivs = soup.findAll("article", id=lambda value: value and value.startswith("post-"))
    current_year = date.today().year


    def get_homepage(DATATYPE:str=None, length:int=0, list_len:bool=False) -> (str | int | dict[int, str]):   # use "print(Simplaza.get_homepage.__doc__)" to get more information about this Function
        
        """Function: get_homepage()\nCurrently available datatypes: json, format\nArguments: *DATATYPE(str), length(int), list_len(bool)\n\n* = required\n"""
        if DATATYPE == "format":
            posts = Simplaza.postdivs[length].findAll("h2", class_="blog-entry-title entry-title")

            #posts_meta_date = posts_meta_list[e].findAll("time", class_="entry-date published")  <-- Experimental
            link_post = posts[0].find("a",href=True)["href"]
            return ("\033[93m%i. \033[36m%s\033[0m\nLink: \033[34m%s\n" % (length+1, (posts[0].find("a").text), (link_post)) + "\033[90m="*len("Link: "+link_post)+"\033[0m")

        elif list_len: return len(Simplaza.postdivs)

        elif DATATYPE == "json":
            if isinstance(length,str): raise(TypeError("Length must be a number!(int)"))
            elif isinstance(length,float): raise(TypeError("Length must be a whole number!(int)"))

            posts = Simplaza.postdivs[length].findAll("h2", class_="blog-entry-title entry-title")

            return ({length:str(posts[0].find("a").text)})


        else: raise(TypeError("Unvalid datatype at get_homepage()"))
        
        
