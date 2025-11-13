from fastapi import FastAPI
import uvicorn
from utils import caesar_encrypt, caesar_decrypt, fence_encryption, fence_decryption


app = FastAPI()


@app.get("/test")
def test_get():
    return {"msg":"hi from test"}

@app.get("/test/{name}")
def test_qwary_get(name):
    with open("names.txt", "a")as n:
        n.write(f"{name} \n")
    return {"msg":"saved user"}

@app.post("/caesar")
def caesar_encryption(item:dict):
    if item["mode"] ==  "encrypt":
        data_to_display = {"encrypted_text": caesar_encrypt(item["text"],item["offset"])}
        print(data_to_display)
        return data_to_display
    elif item["mode"] == "decrypt":
        data_to_display = {"decrypted_text": caesar_decrypt(item["text"],item["offset"])}
        print(data_to_display)
        return data_to_display


@app.get("/fence/encrypt")
def fence_encryption_to_get(text:str):
    data_to_display ={"encrypted_text": fence_encryption(text)}
    print(data_to_display)
    return data_to_display

@app.post("/fence/decrypt")
def fence_decrypt(item:dict):
    item["text"] = fence_decryption(item["text"])
    data_to_display = {"decrypted_text": item["text"]}
    print(data_to_display)
    return data_to_display


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8000)