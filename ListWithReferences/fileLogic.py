
import json

def rozdenienegpa(messange):
    json_str = json.dumps(messange)  # dumps
    with open('storage', 'w') as f:
        f.write(json_str)

def rozdenienegpa2():
    str = ""
    with open('storage', 'r') as f:
        str = f.read()
        try:
            str = json.loads(str)
        except:
            str = "file is empty"
    return str

