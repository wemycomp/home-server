from compose import *
import tkinter as tk
from tkui import *

### TKINTER GUI FUNCTIONS ###

#def print():
#def input():


### APPLICATION SELECTION GUI ###

def vyber_aplikaci():

	apps = []

	# tlačítko pokračovat pro pokračování do potvrzení výběru
	def pokracovat1():
		nonlocal apps
		vybrane = [vyber[i] for i in listbox.curselection()]
		apps = vybrane
		root.destroy()

	# tlačítko pokračovat pro pokračování do konfigurace aplikací
	def pokracovat2():
		pokracovat["value"] = True
		root.destroy()

	# tlačítko zpět
	def zpet():
		pokracovat["value"] = False
		root.destroy()



	while True:

		pokracovat = {"value": False}

		# Vybírací okno
		root = tk.Tk()
		root.geometry("493x312")
		root.title("Vyberte aplikace k instalaci")

		vyber = ["navidrome", "jellyfin", "wordpress"]

		listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
		for i in vyber:
			listbox.insert(tk.END, i)
		listbox.pack(fill=tk.BOTH, expand=True)

		btn_frame = tk.Frame(root)
		btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=8, padx=8)

		btn = Button(root, text="Pokračovat", command=pokracovat1)
		btn.pack(side=tk.RIGHT, padx=8, pady=8)

		root.mainloop()

		# Další okno pro potvrzení výběru aplikací

		root = tk.Tk()
		root.geometry("493x312")
		root.title("Potvrzení výběru")
		# Zobrazení aplikací
		display_text = "Vybrané aplikace:\n" + "\n" + "\n".join(apps) if apps else "Žádné aplikace nebyly vybrány!"
		label = tk.Label(root, text=display_text, anchor="nw", justify="left")
		label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

		# Frame pro tlačítka Zpět a Pokračovat
		btn_frame = tk.Frame(root)
		btn_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=8, padx=8)

		btn_zpet = Button(btn_frame, text="Zpět", command=zpet)
		btn_zpet.pack(side=tk.LEFT)

		btn_pokr = Button(btn_frame, text="Pokračovat", command=pokracovat2)
		btn_pokr.pack(side=tk.RIGHT)

		root.mainloop()

		# Když se uživatel rozhodne vrátit zpět, znovu se otevře výběrové okno. Pokud potvrdí, vrátí se vybrané aplikace.
		if pokracovat["value"]:
			return apps

if __name__ == "__main__":
	apps = vyber_aplikaci()

	# Zápis do souboru docker-compose.yml
	file()
	if "navidrome" in apps:
		navidrome()