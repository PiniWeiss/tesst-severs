LETTERS_LIST = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



def caesar_encrypt(text:str,offset:int):
    decrypted_text = ""
    for letter in text:
        if letter != " ":            
            decrypted_text += LETTERS_LIST[(LETTERS_LIST.index(letter)+offset)%26]
        else:
            decrypted_text += " "
    return decrypted_text

def caesar_decrypt(text:str,offset:int):
    decrypted_text = ""
    for letter in text:
        if letter != " ":            
            decrypted_text += LETTERS_LIST[(LETTERS_LIST.index(letter)-offset)%26]
        else:
            decrypted_text += " "
    return decrypted_text


def fence_encryption(text:str):
    no_places_text = text.replace(" ","")
    double_lettrs = ""
    odd_letters = ""
    for i in range(len(no_places_text)):
        if no_places_text[i] != " ":
            if i %2 == 0:
                double_lettrs += no_places_text[i]
            else:
                odd_letters += no_places_text[i]
    return double_lettrs + odd_letters



def fence_decryption(text:str):
    first_half = text[:len(text)//2+1]
    second_helf = text[len(text)//2-1::-1]
    fixed_text = ""
    for i in range(len(len(text)//2)):
        fixed_text += first_half[i]
        fixed_text += second_helf[i]
    return fixed_text
