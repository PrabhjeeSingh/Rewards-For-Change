import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
from random import randint


# To create a qrcode
def createQrCode1():
    qr = pyqrcode.create("match")
    return qr


def createQrCode2():
    qr = pyqrcode.create("no match")
    return qr


# To read a qr code
def readQrCode(name):
    name += ".png"
    read = decode(Image.open(name))
    score = read[0].data.decode("ascii")
    return score


def win(Dict: dict, name, qr):
    if qr == "match":
        Dict[name][0] += 1


def reward(Dict: dict, name):
    if Dict[name][0] >= 50:
        Dict[name][1] = "$25 Gift card"
    elif Dict[name][0] >= 40:
        Dict[name][1] = "$20 Gift card"
    elif Dict[name][0] >= 20:
        Dict[name][1] = "$10 Gift card"


def createDict(name, Dict: dict):
    Dict.update({name: [0, "No Prize"]})
