def main():
    emoji = convert()
    print(emoji)

def convert():
    face = str(input())
    faces = face.replace(":)","🙂").replace(":(","🙁")
    return faces

main()





