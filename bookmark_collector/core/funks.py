from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def get_page(URL):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    req = Request(URL, headers=headers)
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
        field = f"no_{field}"
    return field
