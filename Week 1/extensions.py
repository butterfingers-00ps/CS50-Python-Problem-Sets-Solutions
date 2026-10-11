file_name = input("File name: ").strip().lower()



if file_name.endswith((".gif", ".jpg", ".jpeg", ".png")):
    ext = file_name.rpartition(".")[2]

    if ext == "jpg":
        ext = "jpeg"

    print(f"image/{ext}")

elif file_name.endswith((".pdf", ".zip")):
    ext = file_name.rpartition(".")[2]

    print(f"application/{ext}")

elif file_name.endswith((".txt")):
    ext = file_name.rpartition(".")[2]

    print("text/plain")

else:

    print("application/octet-stream")


