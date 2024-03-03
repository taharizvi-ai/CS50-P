name=input("File name:")
name=name.lower().strip()
if '.' in name:
    name=name.split(".")
    typ=name[-1]
    match typ:
        case 'gif'|'png':
            print(f"image/{typ}")
        case 'jpg'|'jpeg':
             print("image/jpeg")
        case 'pdf'|'zip':
            print(f"application/{typ}")
        case 'txt':
            print("text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")