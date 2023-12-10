# Image_Encryption
Image Encryption and decryption using python
We Have simple steps to Execute the code
Certainly! Here's a step-by-step guide:

**Step 1:** Ensure that Python is installed on your local system. You can download Python from the official [Python website](https://www.python.org/downloads/).

**Step 2:** Open a terminal or command prompt.

**Step 3:** Check the Python version by typing the following command and pressing Enter:

python --version
or for Python 3:

python3 --version

**Step 4:** Navigate to the directory where the `main.py` file is located using the `cd` command:

cd path/to/your/directory


**Step 5:** Run the Python script using the following command:

python main.py
or for Python 3:
python3 main.py
**Make sure to replace `path/to/your/directory` with the actual path where your `main.py` file is located. This will execute the Tkinter GUI application for image encryption and decryption.**

**After Execition:**
**Initially we got one box like this**
![Screenshot 2023-12-10 110358](https://github.com/sattisatyanarayanareddy/Image_Encryption/assets/113776283/e97a140c-f4ff-407f-9e2f-41fe32dc601d)

**Now set key for handling**


![Screenshot 2023-12-10 110416](https://github.com/sattisatyanarayanareddy/Image_Encryption/assets/113776283/f51537bc-2a7e-4bce-98a3-ba761aca9fd5)

**Choose the image you want to encrypt and upload it using the file dialog that appears in the GUI.**
![Screenshot 2023-12-10 110439](https://github.com/sattisatyanarayanareddy/Image_Encryption/assets/113776283/c96d4752-6873-4d9a-947f-857d4cf2cfd8)

**Now the image is Encrypted**

![Screenshot 2023-12-10 110507](https://github.com/sattisatyanarayanareddy/Image_Encryption/assets/113776283/74ce0669-5f5c-48b6-90fa-fe9876e250b3)

**If you wish to decrypt the image, simply re-upload the image file and provide the same key that you used during the encryption process**
![Screenshot 2023-12-10 110416](https://github.com/sattisatyanarayanareddy/Image_Encryption/assets/113776283/7a762781-7cfd-4919-b17e-6ef06a1a4196)

![Screenshot 2023-12-10 110524](https://github.com/sattisatyanarayanareddy/Image_Encryption/assets/113776283/de7f1251-15e7-4f9b-afad-0008256658b1)


**Deep Explanation For this code**
This Python code is a basic graphical user interface (GUI) application using the Tkinter library for image encryption and decryption. The application allows a user to select a PNG image file, enter a numerical key, and then either encrypt or decrypt the selected image based on a simple bitwise XOR operation.

Here's a brief explanation of the code:

1. **Importing Libraries:**
   - `from tkinter import *`: Imports all classes and functions from the Tkinter library for creating the GUI.
   - `from tkinter import filedialog`: Import the filedialog module to open file dialogs for selecting files.

2. **Creating the GUI Window:**
   - `root = Tk()`: Creates the main Tkinter window.
   - `root.geometry("300x160")`: Sets the initial size of the window.
   - `root.title("Image Encryption and Decryption")`: Sets the title of the window.

3. **Function Definitions:**
   - `encrypt_image()`: Opens a file dialog for selecting a PNG image file, prompts the user for a numerical key, and then performs bitwise XOR encryption on the image using the entered key.
   - `decrypt_image()`: Similar to `encrypt_image()`, but performs decryption using the same XOR operation.

4. **Buttons and Text Entry:**
   - `b1` and `b2`: Buttons labeled "Encrypt" and "Decrypt," respectively. Clicking these buttons triggers the corresponding encryption or decryption function.
   - `entry1`: A Text widget for the user to enter the encryption/decryption key.

5. **Main Event Loop:**
   - `root.mainloop()`: Enters the main event loop, allowing the GUI to respond to user interactions.

6. **Encryption and Decryption Process:**
   - The selected image file is opened in binary mode (`'rb'`), and its contents are read into a bytearray.
   - The key entered by the user is converted to an integer.
   - Each byte of the image is XORed with the key to perform encryption or decryption.
   - The modified bytearray is then written back to the same file in binary mode (`'wb'`).

7. **Print Statements:**
   - Messages indicating the success or failure of encryption/decryption are printed to the console.

Note: The code has a potential issue; it performs both encryption and decryption using the same XOR operation. In practice, encryption and decryption processes are usually different. Additionally, it would be more secure to use a stronger encryption algorithm and handle key management more robustly
