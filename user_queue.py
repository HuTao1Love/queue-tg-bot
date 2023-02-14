from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str


@dataclass
class Admin:
    user_id: int
    name: str
    description: str


class Queue:
    users: list[User]
    buttons: list[InlineKeyboardButton]
    reset_button: InlineKeyboardMarkup
    stop_button: InlineKeyboardMarkup
    creator: int
    size: int

    def __init__(self, creator, keyboard, size=25):
        self.users = [User(0, "-") for i in range(size)]
        self.buttons, self.reset_button, self.stop_button = keyboard
        self.creator = creator
        self.size = size

    def get_keyboard(self):
        keyboard = InlineKeyboardMarkup(5)
        keyboard.add(*self.buttons).row()
        keyboard.add(self.reset_button, self.stop_button)
        return keyboard

    def get_print(self, full=True):
        text = ""
        for num, value in enumerate(self.users, 1):
            if value.user_id != 0 or full:
                text += f"{num}) {value.name}\n"
        return text

    def set(self, num: int, user_id: int, value: str):
        if self.users[num].user_id not in [user_id, 0]:
            return "На это место уже записан другой человек", False

        if self.users[num].user_id == user_id:
            self.users[num].user_id = 0
            self.users[num].name = "-"
            self.buttons[num].text = self.buttons[num].text[:-1]
            self.buttons[num].text += "🟢"
            return "Успешно отписался{ась}", True

        for i in range(len(self.users)):
            if self.users[i].user_id == user_id:
                self.users[i].name = value
                return "Уже в очереди", False

        self.users[num].user_id = user_id
        self.users[num].name = value
        self.buttons[num].text = self.buttons[num].text[:-1]
        self.buttons[num].text += "🔴"
        return "Успешная запись", True

    def reset(self):
        is_modified = False
        for user in range(len(self.users)):
            if self.users[user].user_id != 0:
                is_modified = True
            self.users[user].user_id = 0
            self.users[user].name = "-"
            self.buttons[user].text = str(user + 1) + "🟢"
        return is_modified
