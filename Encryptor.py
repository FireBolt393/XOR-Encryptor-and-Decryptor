import random
import base64

try:

    def encrypt_file(file):
        # Generate a random key
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}:|-=[]\:;'?/>.<,")
        random.shuffle(chars)
        key = "".join(chars[1:17])

        print(f"Key: {key}\n")
        min_index = 0
        max_index = len(key)

        # for file in filePaths:

        with open(file, "rb") as f:
            message = f.read()

        encrypted_message = []
        for byte in message:
            xor_result = byte ^ ord(key[min_index])
            encrypted_message.append(xor_result)

            if min_index == max_index - 1:
                min_index = 0
            else:
                min_index += 1

        # Encode the encrypted message to base64
        encoded_message = base64.b64encode(bytes(encrypted_message)).decode()

        with open(file, "wb") as f:
            f.write(encoded_message.encode())

    if __name__ == "__main__":
        file = input("Enter the file name: ")
        encrypt_file(file)

except Exception as e:
    print(e)
