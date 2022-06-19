# This code is slightly broke, need to go back over it at some point

def main():
    file = input("File name:")
    try:
        if not image(file) and not application(file):
            raise Exception('application/octet-stream')
    except Exception as E:
        print(E.args[0])


def image(s):
    image_e = ['jpg', 'gif', 'jpeg', 'png']
    ext = s.split(".")[1]
    if ext in image_e:
        print("Image/"+ext)
        return True
    return False


def application(s):
    split = (s.split("."))
    join_s = (''.join(split[1]))
    ext = ['pdf', 'txt', 'zip']
    for i in ext:
        if join_s in ext:
            print("Application/"+join_s)
            return True


main()
