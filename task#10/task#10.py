with open("../dataset_24465_4.txt") as r, open("../file1.txt", "w") as w:
    for item in reversed(r.readlines()):
        w.write(item.rsplit()[0]+"\n")
        print(repr(item.rsplit()))