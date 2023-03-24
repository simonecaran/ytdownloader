import pytube;
import os
import tkinter as tk
def Download():
    link_video = link.get()
    yt = pytube.YouTube(link_video)
    yt.streams.get_highest_resolution().download(home_directory)
    empty_label.config(text='Scaricato ' + yt.title)
#Ricerca della homedirectory
home_directory = os.path.expanduser( '~' )
home_directory = home_directory+"\Desktop"
#Creazione della root
window = tk.Tk()
window.geometry("600x600")
window.title("YTDownloader by Simone Carannante")
window.resizable(False,False)
window.configure(background="grey")
#Creazione della whitelabel per scaricato
empty_label = tk.Label(window,fg='green',font=('Arial',14))
empty_label.grid(row=2,column=1,sticky='S')
#Input del link
link = tk.StringVar()
link_entry = tk.Entry(window,textvariable=link,width=60,)
link_entry.insert(0,"Inserisci il link da Youtube da scaricare")
link_entry.place(relx=0.5,rely=0.3,anchor='center')
# Bottone
first_button = tk.Button(text="Download",command=Download)
first_button.place(relx=0.5,rely=0.5,anchor='center')
window.mainloop()
