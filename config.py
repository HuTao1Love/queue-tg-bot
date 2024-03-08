from user_queue import Admin

__all__ = ["BOT_CREATOR", "CAN_CREATE_QUEUES", "CHAT_IDS", "MAX_QUEUE_SIZE"]

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

MAX_QUEUE_SIZE = 98 # why 98?

DEFAULT_QUEUE_SIZE = 25

MAX_QUEUE_NAME_LENGTH = 30