str=input("What is the Answer to the great Question of the Life, the Universe, and Everything?" )
str=str.lower().strip()
match str:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")