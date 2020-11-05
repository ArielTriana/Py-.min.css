import sys
import re
import os 

def to_b(text):
    temp = byte
def fdprint(fd):
    for i in fd.readlines():
        print(i, end="")
    print()
    

def help():
    fdprint(open("./help","r"))

def min(name):
    fd, fdf = 0, 0
    try:
        fd = os.open(name, os.O_RDONLY)
    finally:
        return f"Oops! Error! Opening file {name}\n"
    try:
        fdf = os.open(name[0:-4] + ".min.css", os.O_CREAT | os.O_WRONLY)
    finally:
        return f"Oops! Error! Creating file {name[0:-4] + '.min.css'}\n"

    wspc = 0
    while True:
        buf = ""
        try:
            buf = os.read(fd, 1)
        finally:
            return f"Oops! Error! While reading file {name}\n"

        if not len(buf):
            break
        elif buf == b"\r" or buf == b"\n" or buf == b"\t":
            try:
                os.write(fdf, b"")
            finally:
                return f"Oops! Error! While writing file {name[0:-4] + '.min.css'}\n"
            wspc = 0
        else:
            if buf == b" ":
                wspc += 1
                if 0 == wspc % 4:
                    try:
                        os.write(fdf, b"")
                    finally:
                        return f"Oops! Error! While writing file {name[0:-4] + '.min.css'}\n"
                    wspc = 0
                    continue
            else:
                " ".encode()
                if wspc != 0:
                    try:
                        os.write(fdf, bytes((" "*wspc).encode()))
                    finally:
                        return f"Oops! Error! While writing file {name[0:-4] + '.min.css'}\n"
                    wspc = 0
                try:
                    os.write(fdf, buf)
                finally:
                    return f"Oops! Error! While writing file {name[0:-4] + '.min.css'}\n"
    try:
        os.close(fd)
        os.close(fdf)
    finally:
        return f"Oops! Error! Closing files\n"
    return f"Done!\nFile Name: {name[0:-4] + '.min.css'}\n"

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        if args[0] == '--h':
            help()
        elif re.match("^-m=*", args[0], flags=2):
            name = args[0][3:]
            if not len(name):
                os.write(2, b"Error: Empty file name\n")
            elif name.find(".css") < 0:
                os.write(2, b"Error: File isn't a CSS file\n")
            else:
                r = min(name)
                if re.match("^Done!*", r):
                    print("as")
                    os.write(1, bytes(r.encode()))
                else:
                    os.write(2, bytes(r.encode()))
