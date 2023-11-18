from enum import IntEnum


class Limits(IntEnum):
    EMAIL_MAX_LEN = 254
    USER_MODEL_MAX_LEN = 150
    TEXT_MAX_LEN = 500
    URL_LEN = 2000
    URL_TIMEOUT = 5
