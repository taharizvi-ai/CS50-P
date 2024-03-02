def convert(str):
    string = str.replace(":)","🙂")
    string = string.replace(":(","🙁")
    return string

def main():
    str=input("Enter your text:")
    print(convert(str))

main()