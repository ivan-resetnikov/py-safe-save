from pickle import dumps as stringToBytes, loads as bytesToString, dump, load
from random import randint

from .encrypt import encode, decode



def readFromFile (path, key) :
	with open(path, 'rb') as file :
		return decode(load(file), key)


def writeToFile (path, content) :
	key = randint(0, 100)

	with open(path, 'wb') as file :
		dump(encode(content, key), file)

	return key