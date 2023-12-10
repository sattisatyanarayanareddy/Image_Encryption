from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x160")
root.title("Image Encryption and Decryption")

def encrypt_image():
    file1 = filedialog.askopenfile(mode='rb', filetype=[('png files', '*.png')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)
        if key.strip():
            key = int(key)
            fi = open(file_name, 'rb')
            image = bytearray(fi.read())
            fi.close()
            for index, value in enumerate(image):
                image[index] = value ^ key
            fi1 = open(file_name, 'wb')
            fi1.write(image)
            fi1.close()
            print("Image encrypted successfully!")
        else:
            print("Please enter a valid key.")

def decrypt_image():
    file1 = filedialog.askopenfile(mode='rb', filetype=[('png files', '*.png')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)
        if key.strip():
            key = int(key)
            fi = open(file_name, 'rb')
            image = bytearray(fi.read())
            fi.close()
            for index, value in enumerate(image):
                image[index] = value ^ key
            fi1 = open(file_name, 'wb')
            fi1.write(image)
            fi1.close()
            print("Image decrypted successfully!")
        else:
            print("Please enter a valid key.")

b1 = Button(root, text='Encrypt', command=encrypt_image)
b1.place(x=50, y=10)

b2 = Button(root, text='Decrypt', command=decrypt_image)
b2.place(x=150, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=120, y=50)

root.mainloop()
