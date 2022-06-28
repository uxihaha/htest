import base64


def generateBase64(file_in, file_out):
    with open(file_in, "rb") as fin:
        with open(file_out, "wb") as fout:
            fout.write(base64.b64encode(fin.read()))
            fout.close()
        fin.close()


if __name__ == '__main__':
    generateBase64("app.py", "ap.py")
    generateBase64("myapp", "v.py")
