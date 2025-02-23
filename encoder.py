import cv2
import os
import json

def encrypt_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return False

    height, width, _ = img.shape
    if len(message) > height * width:
        print("Error: Message too long for this image!")
        return False

    n, m, z = 0, 0, 0  # Row, Column, Channel
    for char in message:
        img[n, m, z] = ord(char)  # Store ASCII value
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3  # Rotate channels

    cv2.imwrite(output_path, img)
    print(f"Encryption successful! Encrypted image saved as {output_path}")

    # Save metadata (password & message length) for decryption
    metadata = {"password": password, "length": len(message)}
    with open(output_path + ".json", "w") as meta_file:
        json.dump(metadata, meta_file)

    return True

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    output_path = "encryptedImage.png"
    message = input("Enter the secret message: ")
    password = input("Enter a passcode: ")

    encrypt_message(image_path, output_path, message, password)
