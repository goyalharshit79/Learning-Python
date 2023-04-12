extensions = {"jpg": "image/jpg",
"jpeg": "image/jpeg",
"gif": "image/gif",
"png": "image/png",
"pdf": "application/pdf",
"txt": "text/plain",
"zip": "application/zip"
}

name = input("Enter the name of the file : ").lower().strip()

ext = name.split(sep = ".")
#the next step is used to account for names that might be more than a single words, bcz in any case the last letter will be the extension
ext = ext[::-1]

if ext[0] in extensions:
    print(extensions[ext[0]])
else:
    print("application/octet-stream")
