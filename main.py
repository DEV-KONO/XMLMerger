import tkinter as tk
import packages.DataFrame_SAT_XML as DFS
import pandas as pd
from packages.DataFrame_SAT_XML import to_dataframe
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path
from datetime import datetime

def select_file():
    filetypes = (
        ('ZIP Files', '*.zip'),
    )

    filename = fd.askopenfilename(
        title='Abre un archivo',
        initialdir=downloads_path,
        filetypes=filetypes
    )
    DFS.to_dataframe(filename).to_excel(xlsx_path, index=False)



def main():
    window = tk.Tk()
    window.title("XML Merger")
    window.resizable(False, False)
    window.geometry("300x150")
    open_file = ttk.Button(
        window,
        text = 'Abre el archivo .zip del sat',
        command = select_file
    )

    open_file.pack(expand=True)

    window.mainloop()


if __name__ == "__main__":
    global downloads_path
    global xlsx_path
    downloads_path = str(Path.home() / "Downloads")
    xlsx_path = downloads_path + f'\\Facturas {datetime.today().strftime("%d-%m-%Y %H%M%S %p")}.xlsx'
    main()