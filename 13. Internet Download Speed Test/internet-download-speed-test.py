# import Python Modules
import tkinter as tk

assets_dir = "assets/"
icon_file = "internetspeed_102161.ico"

root = tk.Tk()

root.geometry("450x600")
root.resizable(0, 0)
root.title("Internet Download Speed Test")
root.iconbitmap(f"{assets_dir}{icon_file}")

root.mainloop()