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