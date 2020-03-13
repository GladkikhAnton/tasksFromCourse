import os.path

os.chdir("main 2")
a = []
with open("../file.txt", "w") as w:
    for current_dir, dirs, files in os.walk("."):
        for file in files:
            if file[-3:] == ".py":
                a.append("main"+current_dir[1:])
                break
    a.sort()
    w.write("\n".join(a))
