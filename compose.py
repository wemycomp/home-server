"""
Pozn.: Vyzkoušet metodu insert()  insert(END, item + "\n")
"""


import tkinter as tk
from tkinter import filedialog
from time import sleep

def file():
    with open("docker-compose.yml", "w", encoding="utf-8") as file:
        file.write("services:\n")

def navidrome():
    port=str(input("Zadejte vhodný port pro aplikaci Navidrome: "))

    user=input("Specifikujte ID uživatele (default=1000 - v tomto případě nezadávejte nic): ")
    if user=="":
        user=str("1000")

    print("Vyberte nejprve adresář pro instalaci aplikace Navidrome (default=./data - klikněte při výběru na Zrušit): ")
    sleep(3)
    data=filedialog.askdirectory()

    print("Vyberte adresář s hudbou (default=./music - klikněte při výběru na Zrušit): ")
    sleep(3)
    music=filedialog.askdirectory()

    # data=str(input("Zadejte cestu pro instalaci aplikace Navidrome (default=./data): "))
    # music=str(input("Zadejte cestu pro instalaci aplikace Navidrome (default=./music): "))
    if data=="":
        data=str("./data")
    
    if music=="":
        music=str("./music")

    with open("docker-compose.yml", "a", encoding="utf-8") as file:
        file.write("  navidrome:\n")
        file.write("    image: deluan/navidrome:latest\n")
        file.write("    container_name: navidrome\n")
        file.write("    user: " + user +":1000\n")
        file.write("    ports:\n")
        file.write("      - " + port + ":" + port +"\n")
        file.write("    restart: unless-stopped\n")
        file.write("    volumes:\n")
        file.write("      - " + data + ":/data\n")
        file.write("      - " + music + ":/music:ro\n")

"""
Zatím nedostupné

def homeassistant():

def jellyfin():

def portainer():

def immich():

def smb():

def ftp():

def craftycontroller():

def bitwarden():
"""
if __name__ == "__main__":
    file()
    navidrome()