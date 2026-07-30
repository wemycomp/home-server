"""Modul s funkcemi pro okýnkové otázky a odpovědi:

input(otazka) -> str

nacti_cislo(otazka) -> int

ano_nebo_ne(otazka) -> bool

print(argument0, argument1, argument2, ..., argument_n, sep='')

"""

from tkinter import Tk, LEFT, RIGHT, BOTTOM, TOP, W, BOTH, Label, Button, Entry, Frame
from tkinter.ttk import Label, Button, Entry

# Spinbox byl přidán v Pythonu 3.7
try:
    from tkinter.ttk import Spinbox
except ImportError:
    Spinbox = None

def input(otazka):
    """Zeptá se uživatele na otázku a vrátí odpověď jako řetězec."""
    root = Tk()
    root.title('')
    root.geometry("493x312")

    label = Label(root, text=otazka, anchor="nw", justify="left")
    label.pack(expand=True, padx=10, pady=10)

    button = Button(root, text="OK", command=root.quit)
    button.pack(side=RIGHT)

    entry = Entry(root)
    entry.pack(side=LEFT)

    root.mainloop()

    value = entry.get()
    root.destroy()

    return value

def input_int(otazka='odpověz'):
    """Zeptá se uživatele na otázku a vrátí odpověď jako celé číslo."""
    root = Tk()
    root.title('')
    root.geometry("493x312")

    label = Label(root, text=otazka, anchor="nw", justify="left")
    label.pack(expand=True, padx=10, pady=10)

    button = Button(root, text="OK", command=root.quit)
    button.pack(side=RIGHT)

    entry = Spinbox(root, from_=1, to=9999)
    entry.pack(side=LEFT)

    root.mainloop()

    value = entry.get()
    root.destroy()

    return value


def nacti_cislo(otazka='Zadej číslo'):
    """Zeptá se uživatele na otázku a vrátí odpověď jako celé číslo."""
    if Spinbox == None:
        raise NotImplementedError(
            "nacti_cislo bohužel potřebuje Python verze 3.7 a výš"
        )

    root = Tk()
    root.title('')
    root.geometry("493x312")

    entry = Spinbox(root, from_=0, to=100)
    entry.set('0')
    entry.pack(side=LEFT)

    def ok_pressed():
        text = entry.get()
        try:
            value = int(text)
        except ValueError:
            entry.set('sem zadej číslo!')
        else:
            root.quit()

    button = Button(root, text="OK", command=ok_pressed)
    button.pack(side=RIGHT)

    root.mainloop()

    value = int(entry.get())
    root.destroy()

    return value

def ano_nebo_ne(otazka='Ano nebo ne?'):
    """Dá uživateli na výběr Ano/Ne a vrátí odpověď True nebo False."""
    root = Tk()
    root.title("Ano nebo ne?")
    root.geometry("493x312")

    value = False

    def yes():
        nonlocal value
        value = True
        root.quit()

    def no():
        nonlocal value
        value = False
        root.quit()

    label = Label(root, text=otazka)
    label.pack(side=TOP, expand=True, padx=20, pady=10)

    button = Button(root, text="Ano", command=yes)
    button.pack(side=LEFT, expand=True, padx=10, pady=10)

    button = Button(root, text="Ne", command=no)
    button.pack(side=RIGHT, expand=True, padx=10, pady=10)

    root.mainloop()
    root.destroy()

    return value

def print(*args, sep=' ', end='', file=None, flush=False):
    """Zobrazí dané argumenty."""
    root = Tk()
    root.title('')
    root.geometry("493x312")

    str_args = ''
    for arg in args:
        str_args = str_args + sep + str(arg)

    label = Label(root, text=str_args[len(sep):] + end)
    label.pack(anchor=W)

    button = Button(root, text="Pokračovat", command=root.quit)
    button.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

    root.bind('<Return>', (lambda e: root.quit()))
    root.mainloop()
    root.destroy()