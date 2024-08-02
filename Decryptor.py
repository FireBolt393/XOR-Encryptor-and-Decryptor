import base64

try:
    key = input("Enter the Decryption key: ")
    file = input("Enter the file name: ")

    # Decryptor
    min_index = 0
    max_index = len(key)

    with open(file, "rb") as f:
        encoded_message = f.read()

    # Decode the base64 message
    decoded_message = base64.b64decode(encoded_message)
    decrypted_message = bytearray()

    for xor_result in decoded_message:
        # Ensure the result is within the valid byte range (0-255)
        xor_result = xor_result & 0xFF
        byte = xor_result ^ ord(key[min_index])
        decrypted_message.append(byte)

        if min_index == max_index - 1:
            min_index = 0
        else:
            min_index += 1

    with open(file, "wb") as f:
        f.write(decrypted_message)

except Exception as e:
    print(e)
