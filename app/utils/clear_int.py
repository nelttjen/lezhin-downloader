import string


def get_clear_int(stri: str):
    ret = ''
    for i in stri:
        if i in string.digits:
            ret += i
    return ret