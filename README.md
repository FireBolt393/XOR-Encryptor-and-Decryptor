# Encryptor & Decryptor
## Overview

This project is a simple file encryption and decryption tool. It uses a randomly generated key to securely encrypt your files. The same key is required to decrypt the file, so make sure to save it during the encryption process. If the key is lost, the encrypted file cannot be decrypted.

### Features

Random Key Generation: Each file is encrypted with a unique, randomly generated key.
Base64 Encoding: The encrypted file is encoded in Base64 for safe storage and transfer.
User-Friendly Command Line Interface: Simple prompts for file name and key input.

### Requirements
Python 3.x

### Installation
**Clone the repository:**

`git clone https://github.com/FireBolt393/XOR-Encryptor-and-Decryptor.git`

`cd XOR-Encryptor-and-Decryptor`

### Usage
**Encrypting a File**
To encrypt a file, run the following command:

`python encryptor.py`

You will be prompted to enter the file name:

`Enter the file name: yourfile.txt`

The program will generate a key and display it:

`Key: ABCD1234efgh5678`

**Important:** Save this key. You will need it to decrypt the file later.

**Decrypting a File**

To decrypt a file, run the following command:

`python decryptor.py`

You will be prompted to enter the key and the file name:

`Enter the Decryption key: ABCD1234efgh5678`

`Enter the file name: yourfile.txt`

### Important Notes
**Supported File Types**: This tool can be used to encrypt and decrypt files of any type or extension. 

**Key Preservation:** The key generated during the encryption process is crucial. Without it, the encrypted file cannot be decrypted.

**Base64 Encoding:** The encrypted files are encoded in Base64, which may increase the file size slightly.

### Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

### License
This project is licensed under the MIT License. See the LICENSE file for details.
