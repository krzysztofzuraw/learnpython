import tkinter as tk
from PIL import Image, ImageTk
import captcha_maker as captcha
import captcha_reader as cap

class MainApplication(tk.Frame):
    """Main window"""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.create_widgets()
        
    def create_widgets(self):
        """Creating widgets"""
        self.input_label = tk.Label(self, text="Text: ")

        self.input_text = tk.Entry(self)
        
        self.input_button = tk.Button(self, text="Generate captcha", 
                                        command=self.make_captcha)
        self.img = ImageTk.PhotoImage(Image.open('bin/blank'))
        self.image_label = tk.Label(self, image= self.img)
        self.image_label.image = self.img
        
        self.strings = tk.StringVar()
        self.read_button = tk.Button(self, text="Read captcha", 
                                        command=self.read_captcha)
        self.output_text = tk.Label(self, textvariable=self.strings)
        
        self.input_label.grid(row=0, column=0)
        self.input_text.grid(row=0, column=1)
        self.input_button.grid(row=1, column=0)
        self.image_label.grid(row=1, column=1)
        self.read_button.grid(row=2, column=0)
        self.output_text.grid(row=2, column=1)
        
        
    def make_captcha(self):
        captcha.make(self.input_text.get())
        self.img2 = ImageTk.PhotoImage(Image.open('bin/result'))
        self.image_label.configure(image=self.img2)
        self.image_label.image = self.img
        
    def read_captcha(self):
        cap.read()
        with open('bin/output.txt', 'r') as f:
            read_data = f.read().rstrip()
        self.strings.set(read_data)    

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid()
    root.mainloop()
