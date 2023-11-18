from core.funcs import get_page, soup_maker
from tests.test_data import TEST_URLS_CODE, TEST_URLS_PARSE, TEST_URLS_SOUP


def test_get_page_req():
    for resp, link in TEST_URLS_CODE.items():
        assert (
            resp
        ) == f"{(get_page(link)['code'])}", f"{link} вернул не {resp}"


def test_get_page_soup():
    for link, soup in TEST_URLS_SOUP.items():
        assert (soup) == bool(
            (get_page(link)["soup"])
        ), "Суп оказался там, где не должен был. Или не оказался..."


def test_soup_maker():
    for link, data in TEST_URLS_PARSE.items():
        for field, value in data.items():
            assert (value) == soup_maker(
                link, field
            ), f"Неправильное значение og или meta {field}"
