#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

tk = Tk()

languages = ['C', 'python', 'php', 'html', 'SQL', 'java']
listbox = Listbox(tk)
for item in languages:
    listbox.insert(END, item)
listbox.pack()

tk.mainloop()
