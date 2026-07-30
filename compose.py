"""
Pozn.: Vyzkoušet metodu insert()  insert(END, item + "\n")

Tento soubor slouží k definici funkcí, které provedou zápis do souboru docker-compose.yml. Každá funkce odpovídá jedné aplikaci, která je vybrána uživatelem v GUI. Funkce zapisují potřebné konfigurace pro danou aplikaci do souboru docker-compose.yml.
Při spuštění tohoto souboru se nejprve vytvoří soubor docker-compose.yml a poté se spustí funkce pro aplikaci Navidrome, která zapisuje potřebné konfigurace do souboru.
"""


import tkinter as tk
from tkinter import filedialog
from time import sleep
from tkui import *

def file():
    with open("docker-compose.yml", "w", encoding="utf-8") as file:
        file.write("services:\n")

def navidrome():
    port=str(input_int("Zadejte vhodný port pro aplikaci Navidrome (default=4533 - v tomto případě nezadávejte nic): "))
    if port=="":
        port=str("4533")
    user=str(input_int("Specifikujte ID uživatele (default=1000 - v tomto případě nezadávejte nic): "))
    if user=="":
        user=str("1000")

    print("Vyberte nejprve adresář pro instalaci aplikace Navidrome (default=./data - klikněte při výběru na Zrušit): ")
    data=filedialog.askdirectory()

    print("Vyberte adresář s hudbou (default=./music - klikněte při výběru na Zrušit): ")
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