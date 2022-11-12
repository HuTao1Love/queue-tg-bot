from aiogram.types import InlineKeyboardMarkup


class Queue:
    def __init__(self, creator, keyboard, size=25):
        self.users = ["-" for i in range(size)]
        self.buttons, self.reset_button, self.stop_button = keyboard
        self.creator = creator
        self.size = size

    def get_keyboard(self):
        keyboard = InlineKeyboardMarkup(5)
        keyboard.add(*self.buttons).row()
        keyboard.add(self.reset_button, self.stop_button)
        return keyboard

    def get_print(self):
        text = ""
        for num, value in enumerate(self.users, 1):
            text += f"{num}) {value.replace('NO_VALUE', '-')}\n"
        return text

    def set(self, num: int, value: str):
        if self.users[num] not in [value, "-"]:
            return "На это место уже записан другой человек", False

        if self.users[num] == value:
            self.users[num] = '-'
            self.buttons[num].text = self.buttons[num].text[:-1]
            self.buttons[num].text += "🟢"
            return "Успешно отписался{ась}", True

        try:
            self.users.index(value)
            return "Уже в очереди", False
        except ValueError:
            self.users[num] = value
            self.buttons[num].text = self.buttons[num].text[:-1]
            self.buttons[num].text += "🔴"
            return "Успешная запись", True

    def reset(self):
        is_modifed = False
        for user in range(len(self.users)):
            if self.users[user] != "-":
                is_modifed = True
            self.users[user] = "-"
            self.buttons[user].text = str(user + 1) + "🟢"
        return is_modifed
