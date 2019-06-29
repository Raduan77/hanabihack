import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class Forkwell_parser:
    def __init__(self, login):

        HEADERS = {"User-Agent": "Mozilla/5.0"}

        self.user_name = login
        self.user_languages = dict()
        self.all_languages = {
            "c++",
            "python",
            "c",
            "javascript",
            "java",
            "go",
            "c#",
            "ruby",
            "shell",
            "php",
            "css",
            "logos",
            "racket",
        }
        self.path = f"https://portfolio.forkwell.com/@{self.user_name}"
        req = Request(self.path, headers=HEADERS)
        resp = requests.get(self.path)
        self.webpage = resp.text
        self.soup = BeautifulSoup(self.webpage, "html.parser")

    def get_user_info(self):
        all_strong = self.soup.findAll("strong")
        for name in all_strong:
            text = name.text
            if len(text.split()) == 2:
                language, skill = text.split()
                if language.lower() in self.all_languages:
                    self.user_languages[language.lower()] = int(
                        skill[skill.find("Lv") + 2 :]
                    )
        return self.user_languages


if __name__ == "__main__":

    f = Forkwell_parser(login="diedino")
    print(f.get_user_info())
