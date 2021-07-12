import re

valid_m = re.compile(r"(\w+)@(\w+\.\w{2,})")


def email_parse(mail: str):
    try:
        find_email = valid_m.findall(mail)
        for i in find_email:
            result = {'username': i[0], 'domain': i[1]}
        return print(result)
    except BaseException:
        print('ValueError: wrong email: ', name)


if __name__ == '__main__':
    name = input()
    email_parse(name)

