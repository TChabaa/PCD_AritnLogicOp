import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operasi Logika")
        self.root.geometry("900x500")
        
        title_label = tk.Label(root, text="Operasi Logika", font=("Arial", 14), fg="black")
        title_label.grid(row=0, column=1, columnspan=4, pady=10)
        
        frame = tk.Frame(root)
        frame.grid(row=1, column=0, columnspan=6, pady=10)
        
        self.img_label1 = tk.Label(frame, text="Image 1", width=20, height=10, bg="white", relief="solid")
        self.img_label1.grid(row=0, column=0, padx=10)
        
        self.upload_btn1 = tk.Button(frame, text="Upload Image", bg="lightgray", fg="black", command=self.mock_upload)
        self.upload_btn1.grid(row=1, column=0, pady=5)
        
        self.img_label2 = tk.Label(frame, text="Image 2", width=20, height=10, bg="white", relief="solid")
        self.img_label2.grid(row=0, column=1, padx=10)
        
        self.upload_btn2 = tk.Button(frame, text="Upload Image", bg="lightgray", fg="black", command=self.mock_upload)
        self.upload_btn2.grid(row=1, column=1, pady=5)
        
        self.create_buttons(frame)
        self.create_arithmetic_buttons(frame)
        
        self.result_label = tk.Label(frame, text="Result", width=20, height=10, bg="white", relief="solid")
        self.result_label.grid(row=0, column=4, padx=10)
        
        self.reset_btn = tk.Button(frame, text="RESET", width=10, bg="lightgray", fg="black", command=self.mock_reset)
        self.reset_btn.grid(row=1, column=4, pady=10)
    
    def mock_upload(self):
        print("Upload button clicked")
    
    def mock_operation(self, operation):
        print(f"Operation {operation} clicked")
    
    def create_buttons(self, frame):
        button_frame = tk.Frame(frame)
        button_frame.grid(row=0, column=2, padx=10)
        
        operations = ["NOT A", "NOT B", "OR", "AND", "XOR"]
        for i, op in enumerate(operations):
            btn = tk.Button(button_frame, text=op, width=10, bg="lightgray", fg="black", command=lambda o=op: self.mock_operation(o))
            btn.grid(row=i, column=0, pady=3)
    
    def create_arithmetic_buttons(self, frame):
        arithmetic_frame = tk.Frame(frame)
        arithmetic_frame.grid(row=0, column=3, padx=10)
        
        operations = ["+", "-", "x", "÷"]
        for i, op in enumerate(operations):
            btn = tk.Button(arithmetic_frame, text=op, width=10, bg="lightgray", fg="black", command=lambda o=op: self.mock_operation(o))
            btn.grid(row=i, column=0, pady=3)
    
    def mock_reset(self):
        print("Reset button clicked")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
