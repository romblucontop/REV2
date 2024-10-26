import argparse, base64, random, codecs

def rev2_encode(text: str):
    amount = random.randint(5, 9)
    encoded_text = text.encode('utf-8')
    for _ in range(amount):
        encoded_text = base64.b64encode(encoded_text)
    encoded_text = encoded_text.decode('utf-8')
    encoded_text = encoded_text[:4] + str(amount) + encoded_text[4:]
    encoded_text = encoded_text.encode('utf-8').hex()
    encoded_text = codecs.encode(encoded_text, 'rot_13')
    return encoded_text

def rev2_decode(text: str):
    decoded_text = text
    decoded_text = codecs.decode(decoded_text, 'rot_13')
    decoded_text = bytes.fromhex(decoded_text).decode('utf-8')
    amount_encoded = decoded_text[4]
    decoded_text = decoded_text[:4] + decoded_text[5:]
    for _ in range(int(amount_encoded)):
        decoded_text = base64.b64decode(decoded_text)
    decoded_text = decoded_text.decode('utf-8')
    return decoded_text

def main(type, path):
    try:
        if type in ['e', 'encrypt', 'enc', 'encode']:
            with open(path, 'r') as file:
                content = file.read()
            with open(path, 'w') as file:
                file.write(rev2_encode(content))
            print("File encoded successfully!")
        elif type in ['d', 'decrypt', 'dec', 'decode']:
            with open(path, 'r') as file:
                content = file.read()
            with open(path, 'w') as file:
                file.write(rev2_decode(content))
            print("File decoded successfully!")
        else:
            print('Argument 1 \'type\' must be either \'encode\' or \'decode\'')
    except:
        print('Path doesn\'t exist or is not a file!')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use REV2 to encode or decode a file!")

    parser.add_argument('type', type=str, help='encode or decode')
    parser.add_argument('file', type=str, help='the file path to encode or decode')

    args = parser.parse_args()

    main(args.type, args.file)