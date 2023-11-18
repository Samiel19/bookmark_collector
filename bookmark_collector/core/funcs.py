from socket import timeout
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from .enums import Limits
from .text import TextConst


def get_page(URL):
    req = Request(URL, headers=TextConst.HEADERS)
    try:
        with urlopen(req, timeout=Limits.URL_TIMEOUT.value) as resp:
            code = resp.code
            soup = BeautifulSoup(
                resp,
                "html.parser",
                from_encoding=resp.info().get_param("charset"),
            )
    except (URLError, HTTPError) as e:
        soup = False
        code = e.reason
    except timeout:
        soup = False
        code = "timeout"
    return {"soup": soup, "code": code}


def soup_maker(URL, field):
    page = get_page(URL)
    soup = page["soup"]
    code = page["code"]
    if soup and code == 200:
        if soup.findAll(TextConst.META_TAG_NAME, property=f"og:{field}"):
            field_value = soup.find(
                TextConst.META_TAG_NAME, property=f"og:{field}"
            )["content"]
        else:
            if field == "title" and soup.title:
                field_value = soup.find("title").text
            elif field == "description" and soup.find(
                attrs={"name": "description"}
            ):
                field_value = soup.find(attrs={"name": "description"})[
                    "content"
                ]
            else:
                field_value = ""
    else:
        field_value = ""
    if field == "type" and not field_value:
        field_value = "website"
    return field_value
