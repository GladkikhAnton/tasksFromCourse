import simplecrypt
with open("encrypted.bin", "rb") as inp, open("passwords.txt") as dec:
    encrypted = inp.read()
    x = dec.read().rsplit()
    for item in x:
        print(item)
        try:
            test = simplecrypt.decrypt(item, encrypted)
            print(test)
            print(x)
        except:
            pass
    print(x)
