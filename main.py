import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import validators
from pyshorteners import Shortener
import clipboard


url=None
root = tk.Tk()
root.title("URL Shortener")
root.geometry("600x200")
root.resizable(False,False)
root.iconbitmap("url icon.ico")
source_url_label=tk.Label(root,text="Provide a Link")
source_url_label.place(x=120,y=10)
source_url_entry=ttk.Entry(font=("sans serif",10))
source_url_entry.place(x=120,y=30,width=400,height=20)
#url link image
url_link=tk.PhotoImage(file="image.png")
image_label=tk.Label(image=url_link)
image_label.place(x=100,y=30,height=20,width=10)
def shorten():
    entered_link=source_url_entry.get()
    if len(entered_link)==0:
        messagebox.showerror("Required","Please Provide a Link")
    else:
        link=source_url_entry.get()
        isValid = validators.url(link)
        if isValid ==True:
            try:
                short=Shortener()
                short_link=short.tinyurl.short(entered_link)
                shorten_link_entry=ttk.Entry(root)
                shorten_link_entry.place(x=120,y=90,width=400,height=20)
                shorten_link_entry.insert(0,str(short_link))
                def copy_link():
                    if shorten_link_entry.get():
                        clipboard.copy(short_link)
                        messagebox.showinfo("Copied","Link Copied")
                    else:
                        messagebox.showerror("Empty","Nothing to Copy")
                copy_link_button=ttk.Button(root,text="Copy Shorten Link" ,command=copy_link)
                copy_link_button.place(x=260,y=120)
            except:
                messagebox.showerror("Error","Connection Timeout or Slow internet or No internet")
        else:
            messagebox.showerror("Invalid URL","Provide a Valid URL")
            source_url_entry.delete(0,tk.END)
#clear input field button
def clear():
    source_url_entry.delete(0,tk.END)
def paste_url():
    global url
    url = clipboard.paste()
    source_url_entry.insert(0,str(url))
clear_button=ttk.Button(root,text="Clear",command=clear)
clear_button.place(x=445,y=60)
paste_button=ttk.Button(root,text="Paste",command=paste_url)
paste_button.place(x=280,y=60)
shorten_link_button=ttk.Button(root,text="Shorten",command=shorten)
shorten_link_button.place(x=120,y=60)
source_url_entry.focus()
root.mainloop()
