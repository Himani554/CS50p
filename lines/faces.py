#main()

def main():
    emoji = convert()
    print(emoji)
#convert()

def convert():
    face = str(input())
    faces = face.replace(":)","🙂").replace(":(","🙁")
    return faces

main()
