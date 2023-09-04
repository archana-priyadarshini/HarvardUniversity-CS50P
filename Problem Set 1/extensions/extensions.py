# Problem statement: https://cs50.harvard.edu/python/2022/psets/1/extensions/
ext_full=input("File name: ").lower().strip()
ext=ext_full[ext_full.rfind(".")+1:]
match ext:
    case "gif" | "jpeg" | "png":
        print(f"image/{ext}")
    case "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print(f"application/{ext}")
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")