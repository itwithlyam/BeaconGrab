from tkinter import *
import urllib.request
import json

linkinput = input('What is the IP Tunnel your sniffer runs on? Make sure to include a forward slash at the end. ')

def send():
    uuidd = uuid.get()
    minorr = minor.get()
    majorr = major.get()
    req = urllib.request.Request(
        url=f"{linkinput}api/set?action=tagadd&uuid={uuidd}&major={majorr}&minor={minorr}"
    )


tk = Tk()
tk.title("BeaconGrab")

uuidLab = Label(tk, text="UUID:")
uuidLab.pack()
uuid = Entry(tk)
uuid.pack()

majorLab = Label(tk, text="Major:")
majorLab.pack()
major = Entry(tk)
major.pack()

minorLab = Label(tk, text="Minor:")
minorLab.pack()
minor = Entry(tk)
minor.pack()

sendButton = Button(tk, text="Send", command=send)
sendButton.pack()

tk.mainloop()