import tkinter as tk
from tkinter import scrolledtext
import time


def add_text():
    text = "Downloaded...\n"  
    txt_area.insert(tk.END, text)  
    txt_area.yview(tk.END)  

# main view
view = tk.Tk()
view.title("INSTAGRAM PHOTO-SCRAPPER")
view.geometry("500x300")  
view.configure(bg="black")  
view.resizable(False, False)

# set view icon
icono = tk.PhotoImage(file="pank.png")  
view.iconphoto(False, icono)

# label for the title
label_title = tk.Label(view, text="INSTAGRAM PHOTO-SCRAPPER", font=("Arial", 14), fg="white", bg="black")
label_title.pack(padx=10, pady=10)

# button to start scrapping
btn_start_scrapping = tk.Button(view, text="Iniciar Scrap", command=add_text, fg="white", bg="black", border=2)
btn_start_scrapping.pack(padx= 10, pady=10)

# text area to display downloads
txt_area = scrolledtext.ScrolledText(
    view, 
    width=50, 
    height=15, 
    wrap=tk.WORD, 
    font=("Arial", 10), 
    bg="#333333",      
    fg="#FFFFFF"       
)
txt_area.pack(pady=20)
txt_area.configure(state="normal")  

# main view loop
view.mainloop()
