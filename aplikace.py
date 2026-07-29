from compose import *
import tkinter as tk

### Seznam vybraných aplikací ###
apps = []


### TKINTER GUI FUNCTIONS ###

#def print():
#def input():


### APPLICATION SELECTION GUI ###

def vyber_aplikaci():

	global apps
	apps = []

	root = tk.Tk()
	root.geometry("640x480")
	root.title("Vyberte aplikace k instalaci")

	vyber = ["navidrome", "jellyfin", "wordpress"]

	listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
	for i in vyber:
		listbox.insert(tk.END, i)
	listbox.pack(fill=tk.BOTH, expand=True)

	def ulozit_vyber():
		vybrane = [vyber[i] for i in listbox.curselection()]
		global apps
		apps = vybrane
		root.destroy()
		print(apps)

	btn = tk.Button(root, text="Uložit", command=ulozit_vyber)
	btn.pack(pady=4)

	root.mainloop()

if __name__ == "__main__":
	vyber_aplikaci()