from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

#bestands locatie bepalen
def bestandslocatie():
    global bestandsnaam
    bestandsnaam = filedialog.askdirectory()
    if(len(bestandsnaam)>1):
        locatie.config(text=bestandsnaam, fg="green")
    else:
        locatie.config(text="selecteer een andere folder", fg="red")

#download video in audio bestand
def download():
    url = url_text.get()

    if(len(url)>1):
        yt = YouTube(url)
        select = yt.streams.filter(only_audio=True).first()

    select.download(bestandsnaam)


#het aanmaken van de app
application = Tk()
application.title("Python Youtube Downloader")
application.geometry("700x300")
application.resizable(0,0)
application.columnconfigure(0, weight=1)

#label voor de url toevoegen
url_label = Label(application, text="Vul hieronder de url van de video in", font=("arial", 30))
url_label.grid(padx=10, pady=5)

#een textbox voor de url aanmaken
url_textVar = StringVar()
url_text = Entry(application, width=75, textvariable=url_textVar)
url_text.grid(padx=10, pady=15)

#een download knop maken
bestandslocatie_knop = Button(application, text="Locatie kiezen", width=20, bg="red", command=bestandslocatie)
bestandslocatie_knop.grid(padx=10, pady=5)

#informatie over de bestandslocatie
locatie = Label(application, text=" ")
locatie.grid()

#een download knop maken
download_knop = Button(application, text="Download", width=20, bg="red", command=download)
download_knop.grid(padx=10, pady=20)

application.mainloop()
