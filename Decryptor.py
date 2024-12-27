import base64
import os
# from icecream import icy

print("""

   ___                        __          
  / _ \___ __________ _____  / /____  ____
 / // / -_) __/ __/ // / _ \/ __/ _ \/ __/
/____/\__/\__/_/  \_, / .__/\__/\___/_/   
                 /___/_/                  

""")

def decrypt(*args):
    # try:
    # Decryptor
    min_index = 0

    if __name__ == '__main__':
        file = args[0]
        key = args[1]
        max_index = len(key)
        with open(file, "rb") as f:
            encoded_message = f.read()

    else:
        key = args[0][:16]
        file = args[0][16:]
        max_index = len(key)
        encoded_message = file.encode()
    decoded_message = base64.b64decode(encoded_message)
    decrypted_message = bytearray()

    for xor_result in decoded_message:
        
        xor_result = xor_result & 0xFF
        byte = xor_result ^ ord(key[min_index])
        decrypted_message.append(byte)

        
        if min_index == max_index - 1:
            min_index = 0
        else:
            min_index += 1

    fileName = decrypted_message.decode()[:decrypted_message.decode().index("|")]
    decrypted_message = decrypted_message.replace((fileName + "|").encode(), b"")
    if __name__ == '__main__':
        with open(file, "wb") as f:
            f.write(decrypted_message)
        os.rename(file, fileName)
    else:
        return decrypted_message.decode()

    # except Exception as e:
    #     print(e)


if __name__ == '__main__':
    key = input("Enter the key: ")
    file = input("Enter the file name: ")
    decrypt(file, key)
