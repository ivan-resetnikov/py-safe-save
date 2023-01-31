# pySaveSafe
pySaveSafe is a python module to encrypt and safely store files

> See at [PyPi](https://pypi.org/project/pySafeSave/)

> See at [GitHub](https://github.com/ivan-resetnikov-a/py-safe-save)

> Author [GitHub](https://github.com/ivan-resetnikov-a/)

> Author Email: ivan.resetnikov.alpha@gmail.com



# Documentation

    # How to encrypt and store file:

    <key> = pyss.dump(<file path>, <data>)

    # How to decrypt and read from file:

    <data> = pyss.load(<file path>, <key>)


##### example:

    import pyss

    text = input('Enter text to encrypt > ')

    # write text to file and storing key to later open and read file
    key = pyss.dump('test.bin', text)

    # decrypting file with key and reading from it
    print(pyss.load('test.bin', key))


# Licence
pySaveSafe - python module to encrypt and store files

Copyright (C) 2023  LowRezCat (Ivan Resetnikov)

Read licence for more