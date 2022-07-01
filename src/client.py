from simplaza import Simplaza

# custom process class that auto starts the process



def get_list() -> list[str]: return [Simplaza.get_homepage(DATATYPE="format", length=e) for e in range(Simplaza.get_homepage(list_len=True))]




if __name__ == "__main__":
    print(Simplaza.__name__)
    for e in range(Simplaza.get_homepage(list_len=True)):
        print(str(get_list()[e]))

    print(Simplaza().version)