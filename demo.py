import pyss

text = input('Enter text to encrypt > ')

key = pyss.dump('test.bin', text)
print(pyss.load('test.bin', key))