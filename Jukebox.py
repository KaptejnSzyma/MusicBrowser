import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1) # spacer column

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ========= Labels =========
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ========= Artists listbox =========
artistList = Scrollbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    artistList.insert(tkinter.END, artist[0])

# ========= Album listbox =========
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# ========= Songs listbox =========
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# ========= Main loop =========
testList = range(0, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
print("Closing database connection")
conn.close()
