from tkinter import *
from pytube import YouTube
from tkinter import ttk
import tkinter.messagebox

root = Tk()


def yutub():
    vid = w.get()
    yt = YouTube(vid).streams.get_by_itag(140).download('C:/Users/mario/Desktop')
    tkinter.messagebox.showinfo('Video', 'Video se skinuo')


b = Label(text="Upisi link videa:")
b.pack(side=TOP)

w = Entry(width=50)
w.pack()

b = ttk.Progressbar(maximum=10)

main = Frame(root)
main.pack()


submit = Button(main, text="Skini video", command=yutub)
submit.pack()

root.mainloop()
