TEST_URLS_CODE = {
    "200": "https://www.imdb.com/title/tt0117500/",
    "timed out": "https://www.instagram.com",
    "[Errno 11001] getaddrinfo failed": "https://www.youtdfdsube.com/",
    "Not Found": "https://www.cyberforum.ru/dsfsdfsdf",
}

TEST_URLS_SOUP = {
    "https://www.imdb.com/title/tt0117500/": True,
    "https://www.imdb.com/title/tt0117500/": True,
    "https://www.instagram.com": False,
    "https://www.youtdfdsube.com/": False,
    "https://www.cyberforum.ru/dsfsdfsdf": False,
}


TEST_URLS_SOUP = {
    "https://www.imdb.com/title/tt0117500/": True,
    "https://docs.djangoproject.com/en/4.2/ref/forms/validation/": True,
    "https://www.instagram.com": False,
    "https://www.youtdfdsube.com/": False,
    "https://www.cyberforum.ru/dsfsdfsdf": False,
}


TEST_URLS_PARSE = {
    "https://www.imdb.com/title/tt0117500/": {
        "title": "Скала (1996) ⭐ 7.4 | Action, Adventure, Thriller",
        "type": "video.movie",
        "description": "2h 16m | 16+",
        "image": "https://m.media-amazon.com/images/"
        "M/MV5BZDJjOTE0N2EtMmRlZS00NzU0LWE0Z"
        "WQtM2Q3MWMxNjcwZjBhXkEyXkFqcGdeQXVyN"
        "Dk3NzU2MTQ@._V1_FMjpg_UX1000_.jpg",
    },
    "https://www.youtube.com/": {
        "title": "YouTube",
        "type": "website",
        "description": "Смотрите любимые видео, слушайте "
        "любимые песни, загружайте собственные "
        "ролики и делитесь ими с друзьями, близкими "
        "и целым миром.",
        "image": "https://www.youtube.com/img/desktop/yt_1200.png",
    },
    "https://www.instagram.com": {
        "title": "",
        "type": "website",
        "description": "",
        "image": "",
    },
    "https://www.youtdfdsube.com/": {
        "title": "",
        "type": "website",
        "description": "",
        "image": "",
    },
    "https://www.cyberforum.ru/dsfsdfsdf": {
        "title": "",
        "type": "website",
        "description": "",
        "image": "",
    },
    "https://vk.com/audio-2001810472_7810472": {
        "title": "Placebo: English Summer Rain: слушать онлайн",
        "type": "music.song",
        "description": "",
    },
    "https://lenta.ru/news/2023/08/11/pitt_jolie_divorce/": {
        "title": "Почему распался брак Джоли и Питта:"
        " актеры развелись спустя 7 лет судов",
        "type": "article",
        "description": "Брэд Питт и Анджелина Джоли развелись спустя "
        "семь лет судебных разбирательств. Сообщается, "
        "что пара пришла к соглашению и урегулировала "
        "беспокоящие их вопросы: по предварительным данным, "
        "артистка получит опеку над их тремя несовершенноле"
        "тними детьми, а актер — "
        "полный контроль над их общей винодельней во Франции. ",
        "image": "https://icdn.lenta.ru/images/2023/08/11/16/20230811162921817/"
        "share_c9945c4721c04b6ad7e7cd59d40ba9b5.jpg",
    },
}
