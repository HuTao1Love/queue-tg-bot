from user_queue import Admin
from load_env import GOOGLE_TOKEN

__all__ = ["BOT_CREATOR", "CAN_CREATE_QUEUES", "CHAT_IDS", "URLS"]

BOT_CREATOR = 751586125

CAN_CREATE_QUEUES: dict[int, Admin] = {
    751586125: Admin(751586125, "Hu Tao", "Hu Tao"),
    731492287: Admin(731492287, "Masha", "🥰🥰староста🥰🥰"),
    406495448: Admin(406495448, "Egor", "Злобный клоун"),
    656638834: Admin(656638834, "Vika Nemolyaeva", "Lisa Malyaeva"),
    409428213: Admin(409428213, "Sergey Papikyan", "Ser Gey Papik(yan)"),
    433013981: Admin(433013981, "Danya", "Сахарный человек 🍭"),
    601351747: Admin(601351747, "Сергей Бородавко", "Боба"),
    344909548: Admin(344909548, "??", "??"),
}

CHAT_IDS = {-1001584422120: "03у26", -1001602645423: "04у26"}


def create_url(num: str): return f"https://sheets.googleapis.com/v4/spreadsheets/" \
    f"1RDy1Fs8YmFQ7siXtub1wGKU5nnHTwHn6soBA4FvtPno/values/" \
    f"Очередь ({num})!A:D?" \
    f"key={GOOGLE_TOKEN}"

URLS = {-1001584422120: create_url("03"), -1001602645423: create_url("04")}
