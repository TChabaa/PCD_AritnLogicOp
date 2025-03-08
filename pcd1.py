import tkinter as tk
from tkinter import filedialog
import cv2
from not_logic import not_operation
from PIL import Image, ImageTk
from addition_arit import addition_operation
from and_logic import and_operation
from subtraction_arit import subtraction_operation
from or_logic import or_operation
from multiplication_arit import multiplication_operation
from division_arit import division_operation
from xor_logic import xor_operation

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operasi Logika dan Arimatika")
        self.root.geometry("1000x400")

        title_label = tk.Label(root, text="Operasi Logika dan Aritmatika", font=("Arial", 14), fg="black")
        title_label.grid(row=0, column=1, columnspan=4, pady=10)

        frame = tk.Frame(root)
        frame.grid(row=1, column=0, columnspan=6, pady=10)

        self.img_label1 = tk.Label(frame, text="Image 1", bg="white", relief="solid", padx=100, pady=100)
        self.img_label1.grid(row=0, column=0, padx=10)

        self.upload_btn1 = tk.Button(frame, text="Upload Image", bg="lightgray", fg="black", command=lambda: self.upload_image(1))
        self.upload_btn1.grid(row=1, column=0, pady=5)

        self.img_label2 = tk.Label(frame, text="Image 2", bg="white", relief="solid", padx=100, pady=100)
        self.img_label2.grid(row=0, column=1, padx=10)

        self.upload_btn2 = tk.Button(frame, text="Upload Image", bg="lightgray", fg="black", command=lambda: self.upload_image(2))
        self.upload_btn2.grid(row=1, column=1, pady=5)

        self.create_buttons(frame)
        self.create_arithmetic_buttons(frame)

        self.result_label = tk.Label(frame, text="Result", bg="white", relief="solid", padx=100, pady=100)
        self.result_label.grid(row=0, column=4, padx=10)

        self.reset_btn = tk.Button(frame, text="RESET", width=10, bg="lightgray", fg="black", command=self.reset)
        self.reset_btn.grid(row=1, column=4, pady=10)

        self.image_path1 = None
        self.image_path2 = None

    def cv_to_tk(self, cv_image):
        """Convert OpenCV image to Tkinter PhotoImage"""
        image_rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)  
        image_pil = Image.fromarray(image_rgb) 
        return ImageTk.PhotoImage(image_pil) 
   
    def upload_image(self, img_num):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            image = cv2.imread(file_path) 
            image = cv2.resize(image, (215, 215))  
            img_tk = self.cv_to_tk(image) 

            if img_num == 1:
                self.image_path1 = file_path
                self.img_label1.config(image=img_tk, text="")  
                self.img_label1.image = img_tk 
            else:
                self.image_path2 = file_path
                self.img_label2.config(image=img_tk, text="")
                self.img_label2.image = img_tk

    def apply_not_a(self):
        if self.image_path1:
            result_array = not_operation(self.image_path1)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array) 
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk

    def apply_not_b(self):
        if self.image_path2:
            result_array = not_operation(self.image_path2)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array)  
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk

    def apply_or(self):
        if self.image_path1 and self.image_path2:
            result_array = or_operation(self.image_path1, self.image_path2) 
            result_array = cv2.resize(result_array, (215, 215)) 
            img_tk = self.cv_to_tk(result_array)  
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk        

    def apply_addition(self):
        if self.image_path1 and self.image_path2:
            result_array = addition_operation(self.image_path1, self.image_path2)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array) 
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk
            
    def apply_and(self):
        if self.image_path1 and self.image_path2:
            result_array = and_operation(self.image_path1, self.image_path2)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array)
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk

    def apply_subtraction(self):
        if self.image_path1 and self.image_path2:
            result_array = subtraction_operation(self.image_path1, self.image_path2)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array)
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk
            
    def apply_multiplication(self):
        if self.image_path1 and self.image_path2:
            result_array = multiplication_operation(self.image_path1, self.image_path2)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array)
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk
            
    def apply_division(self):
        if self.image_path1 and self.image_path2:
            result_array = division_operation(self.image_path1, self.image_path2)
            result_array = cv2.resize(result_array, (215, 215))
            img_tk = self.cv_to_tk(result_array)
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk
            
    def apply_xor(self):
        if self.image_path1 and self.image_path2:
            result_array = xor_operation(self.image_path1, self.image_path2) 
            result_array = cv2.resize(result_array, (215, 215)) 
            img_tk = self.cv_to_tk(result_array)  
            self.result_label.config(image=img_tk)
            self.result_label.image = img_tk

    def create_buttons(self, frame):
        button_frame = tk.Frame(frame)
        button_frame.grid(row=0, column=2, padx=10)

        not_a_btn = tk.Button(button_frame, text="NOT A", width=10, bg="lightgray", fg="black", command=self.apply_not_a)
        not_a_btn.grid(row=0, column=0, pady=3)

        not_b_btn = tk.Button(button_frame, text="NOT B", width=10, bg="lightgray", fg="black", command=self.apply_not_b)
        not_b_btn.grid(row=1, column=0, pady=3)

        or_btn = tk.Button(button_frame, text="OR", width=10, bg="lightgray", fg="black", command=self.apply_or)
        or_btn.grid(row=2, column=0, pady=3)

        and_btn = tk.Button(button_frame, text="AND", width=10, bg="lightgray", fg="black", command=self.apply_and)
        and_btn.grid(row=3, column=0, pady=3)

        xor_btn = tk.Button(button_frame, text="XOR", width=10, bg="lightgray", fg="black", command=self.apply_xor)
        xor_btn.grid(row=4, column=0, pady=3)

    def create_arithmetic_buttons(self, frame):
        arithmetic_frame = tk.Frame(frame)
        arithmetic_frame.grid(row=0, column=3, padx=10)

        add_btn = tk.Button(arithmetic_frame, text="+", width=10, bg="lightgray", fg="black", command=self.apply_addition)
        add_btn.grid(row=0, column=0, pady=3)

        subtract_btn = tk.Button(arithmetic_frame, text="-", width=10, bg="lightgray", fg="black", command=self.apply_subtraction)
        subtract_btn.grid(row=1, column=0, pady=3)

        multiply_btn = tk.Button(arithmetic_frame, text="x", width=10, bg="lightgray", fg="black", command=self.apply_multiplication)
        multiply_btn.grid(row=2, column=0, pady=3)

        divide_btn = tk.Button(arithmetic_frame, text="÷", width=10, bg="lightgray", fg="black", command=self.apply_division)
        divide_btn.grid(row=3, column=0, pady=3)

    def mock_operation(self):
        print("Operation button clicked")

    def reset(self):
        self.img_label1.config(image='', text='Image 1')
        self.img_label2.config(image='', text='Image 2')
        self.result_label.config(image='', text='Result')
        self.image_path1 = None
        self.image_path2 = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()