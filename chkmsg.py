import logging

loggers: dict[str, logging.Logger] = {}


def check_message(message):
    if message.chat.id not in loggers.keys():
        loggers[message.chat.id] = logging.getLogger(str(message.chat.id))
        loggers[message.chat.id].setLevel(logging.INFO)
        file_handler = logging.FileHandler(
            filename=f"logs/{message.chat.id}.log")
        file_handler.setLevel(logging.INFO)
        loggers[message.chat.id].addHandler(file_handler)
    loggers[message.chat.id].info(
        f"{message.from_user.id} {message.from_user.first_name} {message.from_user.last_name}: {message.text} \n ({repr(message)})")
    return True
