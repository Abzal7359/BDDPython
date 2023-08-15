from datetime import datetime


def automail():  # this is for  generating random mails
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "abzal" + timestamp + "@gmail.com"
