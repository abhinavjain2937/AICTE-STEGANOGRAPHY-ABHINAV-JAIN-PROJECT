import cv2
import json

def decrypt_message(image_path, metadata_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    try:
        with open(metadata_path, "r") as meta_file:
            metadata = json.load(meta_file)
    except FileNotFoundError:
        print("Error: Metadata file not found!")
        return

    password = input("Enter the passcode for decryption: ")
    if password != metadata["password"]:
        print("Authentication failed!")
        return

    length = metadata["length"]
    height, width, _ = img.shape
    message = ""
    
    n, m, z = 0, 0, 0  # Row, Column, Channel
    for _ in range(length):
        message += chr(img[n, m, z])  # Retrieve ASCII character
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3  # Rotate channels

    print("Decryption successful! Secret message:", message)

if __name__ == "__main__":
    image_path = input("Enter the path of the encrypted image: ")
    metadata_path = image_path + ".json"

    decrypt_message(image_path, metadata_path)
