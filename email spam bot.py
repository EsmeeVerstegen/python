from tkinter import *
import tkinter as tk
from tkinter import ttk

import smtplib
from email.message import EmailMessage
import configparser

def load_contacts():
    config = configparser.ConfigParser()
    config.read('contactlist.ini')
    list_emails = config['contacts']['emails']
    email_receiver.set(list_emails)

#def send_mail():


bot = tk.Tk()
bot.title("Email spam bot")
bot.geometry("1500x700")
bot.resizable(0,0)

sender_label = Label(bot, text="From: ", font=("arial", 15)).place(x=50, y= 50)
email_sender = StringVar()
sender_mail = Entry(bot, width=75, textvariable=email_sender).place(x=175, y= 50)

receiver_label = Label(bot, text="To: ", font=("arial", 15)).place(x=50, y= 100)
email_receiver = StringVar()
receiver_mail = Entry(bot, width=75, textvariable=email_receiver).place(x=175, y= 100)

subject_label = Label(bot, text="Subject: ", font=("arial", 15)).place(x=50, y= 150)
email_subject = StringVar()
subject_mail = Entry(bot, width=75, textvariable=email_subject).place(x=175, y= 150)

message_label = Label(bot, text="Message: ", font=("arial", 15)).place(x=50, y= 200)
email_message = StringVar()
message_mail = tk.Entry(bot, width=200, textvariable=email_message).place(x=175, y= 200, height=50)

contactlist_button = Button(bot, text="Load contacts", width=20, command=load_contacts).place(x=200, y= 300)

send_button = Button(bot, text="Send", width=20, ).place(x=600, y= 300)


bot.mainloop()
