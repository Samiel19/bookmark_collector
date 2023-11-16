from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from .text import TextConst


def get_page(URL):
    req = Request(URL, headers=TextConst.HEADERS)
    con = urlopen(req)
    soup = BeautifulSoup(
        con, "html.parser", from_encoding=con.info().get_param("charset")
    )
    return soup


def soup_maker(URL, field):
    soup = get_page(URL)
    if soup.findAll("meta", property=f"og:{field}"):
        field = soup.find("meta", property=f"og:{field}")["content"]
    else:
        if field == "title" and soup.title:
            field = soup.find("title").text
        elif (
            field == "description"
            and soup.find(attrs={"name": "description"})["content"]
        ):
            field = soup.find(attrs={"name": "description"})["content"]
        else:
            field = f"no_{field}"
    return field
