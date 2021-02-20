#!/usr/bin/env python3

# A Cracker to crack HASHED values
# Cracking MD5 | SHA1 | SHA512
# CyberSamurai DK

import hashlib

type_of_hash = str(input('[!] Which type of Hash do you want to Crack?  (md5, SHA1, SHA512): '))
file_path = str(input('[!] Enter Path to .txt file: '))
hash_to_decrypt = str(input('[!] (⌐■_■)  Enter Hash Value To Decrypt: '))

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[++] (^‿^) Found MD5 Password: ' + line.strip())
                exit(0)

        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[++] (^‿^) Found SHA1 Password: ' + line.strip())
                exit(0)

        if type_of_hash == 'sha512':
            hash_object = hashlib.sha512(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[++] (^‿^) Found SHA512 Password: ' + line.strip())
                exit(0)

    print('[-] (-_-) No Password in file list')