import tkinter as tk

from tkinter import filedialog
from tkinter import messagebox

import pandas as pd

base = tk.Tk()

canvas1 = tk.Canvas(base, width=300, height=300, bg='white', relief='raised')
canvas1.pack()

label1 = tk.Label(base, text='JSON to CSV', bg='white')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)


def get_json():
    global read_file

    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_json(import_file_path)


browseButton_JSON = tk.Button(text="Import JSON", command=get_json, bg='green', fg='white',
                              font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_JSON)


def convertToCSV():
    global read_file

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv(export_file_path, index=None, header=True)


saveAsButton_CSV = tk.Button(text='Convert JSON to CSV', command=convertToCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)


def exitApplication():
    msg_box = tk.messagebox.askquestion('Exit Application', 'Wanna exit?',
                                        icon='warning')
    if msg_box == 'yes':
        base.destroy()


exit_button = tk.Button(base, text='Exit Application', command=exitApplication, bg='brown',
                        fg='white', font=('helvetica', 12, 'bold'))

canvas1.create_window(150, 230, window=exit_button)

base.mainloop()
