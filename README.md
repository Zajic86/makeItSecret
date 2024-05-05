# makeItSecret
Python script for encrypting/decrypting a file and generating own keys using RSA256 asymmetric ciphers

## Install & run
``` bash
git clone https://github.com/Zajic86/makeItSecret.git
cd makeItSecret
pip install -r requirements.txt
cd makeItSecret
python3 main.py
```

## Usage
Menu:
1. Generate keys: generate PRIVATE/PUBLIC keys for enc/dec files
2. Encrypt file: encrypting file with PUBLIC key
3. Decrypt file: decrypting file with your secret PRIVATE key
4. Exit: guess what