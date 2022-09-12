# import Python Modules
import tkinter as tk
from PIL import Image, ImageTk

assets_dir = "assets/"
icon_file = "internetspeed_102161.ico"
logo_file = "internet-speed_icon-icons.com_52832.png"

root = tk.Tk()

root.geometry("450x600")
root.resizable(0, 0)
root.title("Internet Download Speed Test")
root.iconbitmap(f"{assets_dir}{icon_file}")

logo = Image.open(f"{assets_dir}{logo_file}")
logo = logo.resize((100, 100), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.pack(padx=20, pady=10)

text_label = tk.Label(root, text="Internet Download Speed Test", font=("Arial", 18, "bold"), fg="green")
text_label.pack(padx=0, pady=10)

button1 = tk.Button(root, text="Test", font=("Arial", 18, "bold"))
button1.pack()

root.mainloop()