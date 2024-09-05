from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox


def encrypt_number_to_image(number, input_image_path, output_image_path):
    image = Image.open(input_image_path)
    binary_number = bin(number)[2:]
    binary_number = binary_number.zfill(300*200)

    pixel_values = list(image.getdata())
    encrypted_pixels = []

    for i in range(len(pixel_values)):
        pixel = list(pixel_values[i])
        if i < len(binary_number):
            pixel[-1] = int(binary_number[i])
        encrypted_pixels.append(tuple(pixel))

    encrypted_image = Image.new(image.mode, image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_image_path)

def decrypt_image_to_number(input_image_path):
    image = Image.open(input_image_path)
    binary_number = ""

    for pixel in image.getdata():
        binary_number += str(pixel[-1])

    # Ensure the binary number is a multiple of 8 (byte)
    padded_length = (len(binary_number) + 7) // 8 * 8
    binary_number = binary_number.zfill(padded_length)

    return int(binary_number, 2)

class ImageEncryptorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Hider")

        # Center the content both horizontally and vertically
        self.master.geometry("700x500+500+180")
        self.master.resizable(False,False)
        self.master.config(bg="teal")
        img_icon=tk.PhotoImage(file="hidetext.png")
        self.master.iconphoto(False,img_icon)
        
        

        #frame 1
        self.l1=tk.Label(master,text="Text Hider",font="Helvetica 30 bold")
        self.l1.pack(side=tk.TOP,padx=0,pady=0)

        self.f1=tk.Frame(master,bg="misty rose",width=340,height=280,highlightbackground="black",highlightthickness=2)
        self.f1.place(x=10,y=80)
        self.lb1=tk.Label(self.f1,bg="black")
        self.lb1.place(x=40,y=10)
        

        #frame 2
        self.f2=tk.Frame(master,bg="black",width=200,height=200,highlightbackground="black",highlightthickness=2)
        self.f2.place(x=450,y=80)
        
        self.label = tk.Label(self.f2, text="Enter a number to encrypt:")
        self.label.pack()

        self.number_entry = tk.Entry(self.f2)
        self.number_entry.pack()
        
        #frame 3
        self.f3=tk.Frame(master,bg="pink",width=500,height=350,highlightbackground="black",highlightthickness=2)
        self.f3.place(x=380,y=150)
        
        self.browse_button = tk.Button(self.f3,text="Browse Image", width=10,height=2,command=self.browse_image)
        self.browse_button.pack(padx=10,pady=50)
        
        self.l1=tk.Label(self.f3,text="Picture,Image,\nPhoto file",bg="pink",fg="black")
        self.l1.place(x=5,y=5)
        
        #frame 4
        self.f4=tk.Frame(master,bg="RosyBrown1",width=300,height=250,highlightbackground="black",highlightthickness=2)
        self.f4.place(x=500,y=150)
        
        self.encrypt_button = tk.Button(self.f4, text="Encrypt",width=10,height=2, command=self.encrypt_image)
        self.encrypt_button.pack(padx=10,pady=50)

        self.decrypt_button = tk.Button(self.f4, text="Decrypt",width=10,height=2, command=self.decrypt_image)
        self.decrypt_button.pack(padx=30,pady=30)
        self.l2=tk.Label(self.f4,text="encryption & decryption",bg="pink",fg="black")
        self.l2.place(x=5,y=5)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        self.image_path = file_path
        self.show_image(file_path)

    def show_image(self, image_path):
        image = Image.open(image_path)
        image.thumbnail((340, 280))
        photo = ImageTk.PhotoImage(image)
        self.label_image = tk.Label(self.f1, image=photo)
        self.label_image.image = photo
        self.label_image.pack()

    def encrypt_image(self):
        try:
            number_to_encrypt = int(self.number_entry.get())
            output_image_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                               filetypes=[("PNG files", "*.png")])
            encrypt_number_to_image(number_to_encrypt, self.image_path, output_image_path)
            messagebox.showinfo("Encryption Complete", "Image encrypted successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def decrypt_image(self):
        try:
            decrypted_number = decrypt_image_to_number(self.image_path)
            messagebox.showinfo("Decryption Complete", f"Decrypted Number: {decrypted_number}")
        except Exception as e:
            messagebox.showerror("Error", f"Error during decryption: {str(e)}")
            
    def encrypt_image(self):
        try:
            number_to_encrypt = int(self.number_entry.get())
            output_image_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                               filetypes=[("PNG files", "*.png")])
            encrypt_number_to_image(number_to_encrypt, self.image_path, output_image_path)
            messagebox.showinfo("Encryption Complete", "Image encrypted successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()
