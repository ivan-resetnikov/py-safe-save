from pickle import dumps as stringToBytes, loads as bytesToString, dump as writeToFile, load as readFromFile
from random import randint

from json import dumps as dataToString, loads as stringToData



def encode (data, key) :
	encoded = ''

	for char in dataToString(data) :
		encoded += chr(ord(char) + key)

	return encoded


def decode (data, key) :
	decoded = ''

	for char in data :
		decoded += chr(ord(char) - key)

	return stringToData(decoded)



def load (path, key) :
	with open(path, 'rb') as file :
		return decode(readFromFile(file), key)


def dump (path, content) :
	key = randint(0, 100)

	with open(path, 'wb') as file :
		writeToFile(encode(content, key), file)

	return key