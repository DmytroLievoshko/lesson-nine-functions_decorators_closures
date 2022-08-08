import re
from typing import Tuple

ADDRESSBOOK = {}


def input_error(func):
    def iner(*args: str):
        try:
            return func(*args)
        except ValueError as ex:
            return ex

    return iner


@input_error
def handler_hello(args):
    if args != "":
        raise ValueError(
            f"How can I help you? But I don't know what means '{args}'")

    return "How can I help you?"


@input_error
def handler_exit(args):
    if args != "":
        raise ValueError(
            f"Good bye! But I don't know what means '{args}'")

    return "Good bye!"


@input_error
def handler_add(args):
    global ADDRESSBOOK

    name, phone = parse_args(args)
    if not name:
        raise ValueError("Enter user name")
    if not phone:
        raise ValueError("Give me phone please")

    ADDRESSBOOK[name] = [phone]

    return "done"


@input_error
def handler_change(args):
    global ADDRESSBOOK

    name, phone = parse_args(args)
    if not name:
        raise ValueError("Enter user name")
    if not phone:
        raise ValueError("Give me phone please'")

    result = ADDRESSBOOK.get(name)
    if not result:
        raise ValueError(f"no key information {name}")

    result.append(phone)
    ADDRESSBOOK[name] = result

    return "done"


@input_error
def handler_phone(args):
    global ADDRESSBOOK

    name = args
    if not name:
        raise ValueError("Enter user name")

    result = ADDRESSBOOK.get(name)
    if not result:
        raise ValueError(f"no key information {name}")

    phone = "; ".join(result)
    return f"{name} {phone}"


@input_error
def handler_show_all(args):
    global ADDRESSBOOK

    result = "*" * 15 + "\n"
    for name, phones in ADDRESSBOOK.items():
        phone = "; ".join(phones)
        result += f"{name} {phone}\n"

    result += "*" * 15
    return result


DICT_COMMAND = {"hello": handler_hello,
                "exit": handler_exit,
                "close": handler_exit,
                "good bye": handler_exit,
                "add": handler_add,
                "change": handler_change,
                "phone": handler_phone,
                "show all": handler_show_all}


def get_handler(command: str):
    return DICT_COMMAND.get(command)


KEYWORDS_pattern = r"|".join(DICT_COMMAND.keys())


def parse_user_input(user_input: str):
    user_input = user_input.strip()
    user_input_lower = user_input.lower()
    command = ""
    args = ""

    result = re.match(KEYWORDS_pattern, user_input_lower)
    if result:
        command = result.group()
        args = user_input[result.end():].strip()

    return command, args


def parse_args(args: str) -> Tuple[str]:
    name = ""
    phone = ""
    phone_pattern = r"\+?\d+\(?\d+\)?\d+\-?\d+\-?\d+"
    result = re.search(phone_pattern, args)
    if result:
        phone = result.group()

    name = args.removesuffix(phone).strip()

    return name, phone


def main():

    while True:
        user_input = input(">>> ")

        command, args = parse_user_input(user_input)

        handler = get_handler(command)
        if handler:
            result = handler(args)
        else:
            result = f"I don't know what means '{user_input}'"

        print(result)

        if handler == handler_exit:
            break


def print_help():
    print("""'add ...' Команда сохраняет новый контакт. Вместо ... нужно вводить имя и номер телефона, обязательно через пробел.
'change ...' Команда сохраняет в памяти новый номер телефона для существующего контакта. Вместо ... нужно вводить имя и номер телефона, обязательно через пробел.
'phone ...' Команда выводит в консоль номер телефона для указанного контакта. Вместо ... нужно вводить имя контакта, чей номер нужно показать.
'show all". Команда выводит все сохраненные контакты с номерами телефонов в консоль.
'good bye', 'close', 'exit' По любой из этих команд робота завершается""")


if __name__ == '__main__':
    main()
