from asyncio import subprocess
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

###########################
# OKNO A STRÁNKY #
###########################

class okno(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Hose")
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setFixedSize(600, 400) # Pevná velikost
        
        # Datové úložiště pro aplikace napříč stránkami
        self.vybrane_aplikace = []

        self.glance = [] # 0 - port, 1 - config
        self.homeassistant = [] # 0 - config
        self.immich = [] # 0 - port, 1 - fotky
        self.jellyfin = [] # 0 - port, 1 - filmy, 2 - serialy
        self.navidrome = [] # 0 - port, 1 - hudba, 2 - username, 3 - password
        self.nginx = [] # 0 - port, 1 - config, 2 - letsencrypt
        self.pihole = [] # 0 - port, 1 - config, 2 - password
        self.portainer = [] # 0 - port
        self.vaultwarden = [] # 0 - port, 1 - slozka
        self.wordpress = [] # 0 - port, 1 - slozka

        # QStackedWidget - přepínání mezi stránkami
        self.okna = QtWidgets.QStackedWidget()
        
        # Inicializace jednotlivých stránek
        self.stranka_uvod = uvod(self)
        self.stranka_vyber = vyber(self)
        self.stranka_souhrn = souhrn(self)

        self.stranka_glance = glance(self)
        self.stranka_homeassistant = homeassistant(self)
        self.stranka_immich = immich(self)
        self.stranka_jellyfin = jellyfin(self)
        self.stranka_navidrome = navidrome(self)
        self.stranka_nginx = nginx(self)
        self.stranka_pihole = pihole(self)
        self.stranka_portainer = portainer(self)
        self.stranka_vaultwarden = vaultwarden(self)
        self.stranka_wordpress = wordpress(self)

        """self.stranka_instalace = instalace(self)"""

        self.mapa_stranek = {
            "Úvod": self.stranka_uvod,
            "Výběr aplikací": self.stranka_vyber,
            "Souhrn": self.stranka_souhrn,
            "Glance": self.stranka_glance,
            "Home Assistant": self.stranka_homeassistant,
            "Immich": self.stranka_immich,
            "Jellyfin": self.stranka_jellyfin,
            "Nginx Proxy Manager": self.stranka_nginx,
            "Navidrome": self.stranka_navidrome,
            "Pi-hole": self.stranka_pihole,
            "Portainer": self.stranka_portainer,
            "Vaultwarden": self.stranka_vaultwarden,
            "WordPress": self.stranka_wordpress,
        }

        # Přidání stránek do StackedWidgetu
        for app in self.mapa_stranek.values():
            self.okna.addWidget(app)
        

        # Hlavní layout aplikace
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.okna)
        self.setLayout(layout)

        self.sestav_pruvodce()
        self.aktualni_index = 0

    def sestav_pruvodce(self):
        self.aktivni_stranky = [self.stranka_uvod, self.stranka_vyber, self.stranka_souhrn]
        for app in self.vybrane_aplikace:
            if app in self.mapa_stranek:
                self.aktivni_stranky.append(self.mapa_stranek[app])
        
    def dalsi_stranka(self):
        if self.aktualni_index < len(self.aktivni_stranky) - 1:
            self.aktualni_index += 1
            self.okna.setCurrentWidget(self.aktivni_stranky[self.aktualni_index])
        else:
            QtWidgets.QMessageBox.information(self, "Hotovo", "Konfigurace byla úspěšně dokončena.")
            QtWidgets.QApplication.quit()

    def predchozi_stranka(self):
        if self.aktualni_index > 0:
            self.aktualni_index -= 1
            self.okna.setCurrentWidget(self.aktivni_stranky[self.aktualni_index])

###################
# ŠABLONA STRÁNKY #
###################

class sablona(QtWidgets.QWidget):
    def __init__(self, mainw):
        super().__init__(mainw)
        self.mainw = mainw
        
        # Hlavní vertikální layout
        self.main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_layout)
        
        # Layout pro samotný obsah stránky
        self.obsah_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.obsah_layout)
        
        # Pružná mezera
        self.main_layout.addStretch()
        
    def tlacitka(self, text_zpet=None, akce_zpet=None, text_dalsi=None, akce_dalsi=None):
        tlacitka = QtWidgets.QHBoxLayout()
        tlacitka.addStretch() # Zarovná tlačítka doprava

        if text_zpet and akce_zpet:
            btn_zpet = QtWidgets.QPushButton(text_zpet)
            btn_zpet.clicked.connect(akce_zpet)
            tlacitka.addWidget(btn_zpet)
            
        if text_dalsi and akce_dalsi:
            btn_dalsi = QtWidgets.QPushButton(text_dalsi)
            btn_dalsi.clicked.connect(akce_dalsi)
            tlacitka.addWidget(btn_dalsi)
            
        self.main_layout.addLayout(tlacitka)

    def odkaz(self, url):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))

    def vyber_slozky1(self, nazev, default_dir1):
        self.slozka1 = default_dir1
        radek_slozka = QtWidgets.QHBoxLayout()
        radek_slozka.addWidget(QtWidgets.QLabel(nazev))
        btn_vybrat = QtWidgets.QPushButton("Vybrat složku")
        btn_vybrat.clicked.connect(self.prohlizec1)
        radek_slozka.addWidget(btn_vybrat)
        radek_slozka.addStretch()
        self.obsah_layout.addLayout(radek_slozka)

        self.slozka_display1 = QtWidgets.QLabel(f"Vybraná složka (default): {default_dir1}")
        self.obsah_layout.addWidget(self.slozka_display1)

    def prohlizec1(self):
        cesta = QtWidgets.QFileDialog.getExistingDirectory(self, "Vyberte složku")
        if cesta:
            self.slozka1 = cesta
            self.slozka_display1.setText(f"Vybraná složka: {self.slozka1}")

    def vyber_slozky2(self, nazev, default_dir2):
        self.slozka2 = default_dir2
        radek_slozka = QtWidgets.QHBoxLayout()
        radek_slozka.addWidget(QtWidgets.QLabel(nazev))
        btn_vybrat = QtWidgets.QPushButton("Vybrat složku")
        btn_vybrat.clicked.connect(self.prohlizec2)
        radek_slozka.addWidget(btn_vybrat)
        radek_slozka.addStretch()
        self.obsah_layout.addLayout(radek_slozka)

        self.slozka_display2 = QtWidgets.QLabel(f"Vybraná složka (default): {default_dir2}")
        self.obsah_layout.addWidget(self.slozka_display2)

    def prohlizec2(self):
        cesta = QtWidgets.QFileDialog.getExistingDirectory(self, "Vyberte složku")
        if cesta:
            self.slozka2 = cesta
            self.slozka_display2.setText(f"Vybraná složka: {self.slozka2}")
    
    def vyber_username(self):
        radek_username = QtWidgets.QHBoxLayout()
        radek_username.addWidget(QtWidgets.QLabel("Uživatelské jméno (prázdné - admin):"))
        self.username_input = QtWidgets.QLineEdit()
        self.username_input.setPlaceholderText("admin")
        radek_username.addWidget(self.username_input)
        radek_username.addStretch()
        self.obsah_layout.addLayout(radek_username)

    def vyber_password(self):
        radek_password = QtWidgets.QHBoxLayout()
        radek_password.addWidget(QtWidgets.QLabel("Heslo (prázdné - admin):"))
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setPlaceholderText("admin")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        radek_password.addWidget(self.password_input)
        radek_password.addStretch()
        self.obsah_layout.addLayout(radek_password)

    def vyber_port(self, default):
        self.default_port = str(default)
        radek_port = QtWidgets.QHBoxLayout()
        radek_port.addWidget(QtWidgets.QLabel(f"Číslo portu (prázdné - {default}):"))

        self.port_input = QtWidgets.QLineEdit()
        self.port_input.setPlaceholderText(str(default))
        self.port_input.setFixedWidth(100)
        self.port_input.setValidator(QtGui.QIntValidator(1, 65535, self))
        radek_port.addWidget(self.port_input)

        info = QtWidgets.QLabel("🛈")
        info.setToolTip("Síťový port je číslo od 0 do 65 535...")
        info.mousePressEvent = lambda e: self.odkaz("https://cs.wikipedia.org/wiki/S%C3%AD%C5%A5ov%C3%BD_port")

        radek_port.addStretch()
        self.obsah_layout.addLayout(radek_port)

    # Pomocné metody pro získání hodnot v momentě odeslání
    def ziskej_username(self):
        val = self.username_input.text().strip()
        return val if val else "admin"

    def ziskej_password(self):
        val = self.password_input.text().strip()
        return val if val else "123456"

    def ziskej_port(self):
        val = self.port_input.text().strip()
        return val if val else self.default_port

    def cara(self):
        cara = QtWidgets.QFrame()
        cara.setFrameShape(QtWidgets.QFrame.HLine)
        self.obsah_layout.addWidget(cara)

    def nadpis(self, text):
        nadpis = QtWidgets.QLabel(text)
        nadpis.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.obsah_layout.addWidget(nadpis)

    def ziskej_username(self):
        text = self.username_input.text().strip()
        return text if text else "admin"

    def ziskej_password(self):
        text = self.password_input.text().strip()
        return text if text else "123456"

####################
# STRÁNKY APLIKACE #
####################

class uvod(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Vítejte v průvodci instalace domácího serveru!")

        self.cara()

        uvod_text = QtWidgets.QLabel(
            "Tento průvodce vám pomůže nainstalovat a nakonfigurovat vybrané aplikace.\n"
            "Postupujte podle pokynů na obrazovce a vyberte aplikace, které chcete nainstalovat.\n\n"

            "Ujistěte se, že máte nainstalovaný Docker, který je nezbytný pro běh vybraných aplikací. Pokud Docker není nainstalován, průvodce vás na to upozorní.\n"
            "Pro instalaci Dockeru navštivte oficiální dokumentaci: https://docs.docker.com/get-docker/"
        )
        uvod_text.setWordWrap(True)
        self.obsah_layout.addWidget(uvod_text)
        
        # Přidání tlačítka Další
        self.tlacitka(
            text_dalsi="Další", 
            akce_dalsi=self.dalsi
        )
        
    def dalsi(self):
        self.mainw.dalsi_stranka()

class vyber(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Vyberte alespoň 1 aplikaci pro instalaci:")

        self.cara()
        
        self.checkboxy = []
        aplikace = ["Glance", "Home Assistant", "Immich", "Jellyfin", "Navidrome", "Nginx Proxy Manager", "Pi-hole", "Portainer", "Vaultwarden", "WordPress"]
        
        # Nápověda
        popisy = {
            "Glance": "Nástroj pro správu a monitorování serverů a aplikací.",
            "Home Assistant": "Platforma pro automatizaci domácnosti a správu chytrých zařízení.",
            "Immich": "Osobní cloud pro zálohování a správu fotografií a videí.",
            "Jellyfin": "Svobodný mediální systém pro správu a přehrávání stažených filmů a seriálů.",
            "Navidrome": "Osobní hudební server a streamer pro přehrávání stažené hudby kompatibilní s Subsonic.",
            "Pi-hole": "Blokátor reklam a sledovacích skriptů na úrovni sítě.",
            "Portainer": "Nástroj pro správu kontejnerů Docker s webovým rozhraním.",
            "Nginx Proxy Manager": "Nástroj pro správu reverzních proxy serverů s webovým rozhraním.",
            "Vaultwarden": "Správce hesel pro bezpečné ukládání přihlašovacích údajů.",
            "WordPress": "Platforma pro tvorbu webových stránek a blogů."
        }

        odkazy = {
            "Glance": "https://github.com/glanceapp/glance",
            "Home Assistant": "https://www.home-assistant.io/",
            "Immich": "https://immich.app/",
            "Jellyfin": "https://jellyfin.org/",
            "Navidrome": "https://www.navidrome.org/",
            "Nginx Proxy Manager": "https://nginxproxymanager.com/",
            "Pi-hole": "https://pi-hole.net/",
            "Portainer": "https://www.portainer.io/",
            "Vaultwarden": "https://vaultwarden.com/",
            "WordPress": "https://wordpress.org/"
        }

        for i in aplikace:
            # Horizontální layout pro jeden řádek (checkbox + ikona)
            radek = QtWidgets.QHBoxLayout()
    
            cb = QtWidgets.QCheckBox(i)
            self.checkboxy.append(cb)
            radek.addWidget(cb)
    
            # Ikona nápovědy
            info = QtWidgets.QLabel("🛈")
            info.setToolTip(popisy[i])  # Tooltip se zobrazí při najetí na ikonu
            # info.setStyleSheet("color: gray; font-weight: bold;")
            info.mousePressEvent = lambda e, app=i: self.odkaz(odkazy[app])

            radek.addWidget(info)
            radek.addStretch()  # Zarovná ikonu těsně k checkboxu
    
            # Přidání řádku do obsahu
            self.obsah_layout.addLayout(radek)
            
        # Přidání tlačítek
        self.tlacitka(
            text_dalsi="Další", 
            akce_dalsi=self.dalsi,
            text_zpet="Zpět", 
            akce_zpet=lambda: self.mainw.predchozi_stranka()
        )
        
    def dalsi(self):
        # Uložení výběru do nového seznamu
        vybrane = [cb.text() for cb in self.checkboxy if cb.isChecked()]
        
        # Kontrola, zda uživatel vybral
        if not vybrane:
            QtWidgets.QMessageBox.warning(self, "Chyba", "Vyberte alespoň jednu aplikaci!")
            return
            
        # Předání seznamu hlavnímu oknu a aktualizace další stránky
        self.mainw.vybrane_aplikace = vybrane
        self.mainw.sestav_pruvodce()
        self.mainw.stranka_souhrn.vypis()
        
        # Přepnutí na druhou stránku
        self.mainw.dalsi_stranka()


class souhrn(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Zvolené aplikace:")
        
        # Label pro vypsání textu
        self.vypis_label = QtWidgets.QLabel()
        self.vypis_label.setAlignment(QtCore.Qt.AlignTop)
        self.obsah_layout.addWidget(self.vypis_label)
        
        # Přidání tlačítek Zpět a Další
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )
        
    def vypis(self):
        text_vypisu = ""
        for i in self.mainw.vybrane_aplikace:
            text_vypisu += f"{i}\n"
            
        self.vypis_label.setText(text_vypisu)
        
    def dalsi(self):
        self.mainw.dalsi_stranka()

class jellyfin(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Jellyfin")
        self.cara()
        self.vyber_port("8096")
        self.cara()
        self.vyber_slozky1("Vyberte složku s filmy:", "./filmy")
        self.cara()
        self.vyber_slozky2("Vyberte složku se seriály:", "./serialy")

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):

        self.mainw.jellyfin = [
            self.ziskej_port(),
            self.slozka1,
            self.slozka2,
        ]
        print(self.mainw.jellyfin)
        self.mainw.dalsi_stranka()

class vaultwarden(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)

        self.nadpis("Konfigurace Vaultwarden")
        self.cara()
        self.vyber_port("9445")
        self.cara()
        self.vyber_slozky1("Vyberte složku s hesly:", "./hesla")



        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.vaultwarden = [
            self.ziskej_port(),
            self.slozka1
        ]
        print(self.mainw.vaultwarden)
        self.mainw.dalsi_stranka()

class navidrome(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Navidrome")
        self.cara()
        self.port=self.vyber_port("4533")
        self.cara()
        self.slozka=self.vyber_slozky1("Vyberte složku s hudbou:", "./hudba")
        self.cara()
        self.username=self.vyber_username()
        self.cara()
        self.password=self.vyber_password()

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )
    
    def dalsi(self):
        # Uložení vybraných hodnot do hlavního okna
        self.mainw.navidrome = [
            self.ziskej_port(),
            self.slozka1,
            self.ziskej_username(),
            self.ziskej_password()
        ]
        print(self.mainw.navidrome)
        self.mainw.dalsi_stranka()

class portainer(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Portainer")
        self.cara()
        self.vyber_port("8000")

        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.portainer = [
            self.ziskej_port()
        ]
        print(self.mainw.portainer)
        self.mainw.dalsi_stranka()

class immich(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Immich")
        self.cara()
        self.vyber_port("2283")
        self.cara()
        self.vyber_slozky1("Vyberte složku pro ukládání obrázků", "./immich")

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.immich = [
            self.ziskej_port(),
            self.slozka1
        ]
        print(self.mainw.immich)
        self.mainw.dalsi_stranka()


class homeassistant(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Home Assistant")
        self.cara()
        self.vyber_slozky1("Vyberte složku pro ukládání konfigurace:", "./homeassistant")

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.homeassistant = [
            self.slozka1
        ]
        print(self.mainw.homeassistant)
        self.mainw.dalsi_stranka()

class pihole(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Pi-hole")
        self.cara()
        self.vyber_port("82")
        self.cara()
        self.vyber_slozky1("Vyberte složku pro ukládání konfigurace:", "./pihole")
        self.vyber_password()

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.pihole = [
            self.ziskej_port(),
            self.slozka1,
            self.ziskej_password()
        ]
        print(self.mainw.pihole)
        self.mainw.dalsi_stranka()

class nginx(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Nginx Proxy Manager")
        self.cara()
        self.vyber_port("81")
        self.cara()
        self.vyber_slozky1("Vyberte složku pro ukládání konfigurace:", "./nginx/data")
        self.cara()
        self.vyber_slozky2("Vyberte složku pro ukládání ssl certifikátů:", "./nginx/letsencrypt")

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.nginx = [
            self.ziskej_port(),
            self.slozka1,
            self.slozka2
        ]
        print(self.mainw.nginx)
        self.mainw.dalsi_stranka()

class glance(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Glance")
        self.cara()
        self.vyber_port("83")
        self.cara()
        self.vyber_slozky1("Vyberte složku pro ukládání konfigurace:", "./glance")

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.glance = [
            self.ziskej_port(),
            self.slozka1
        ]
        print(self.mainw.glance)
        self.mainw.dalsi_stranka()

class wordpress(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        self.nadpis("Konfigurace Wordpress")
        self.cara()
        self.vyber_port("8080")
        self.vyber_slozky1("Vyberte složku pro ukládání dat Wordpressu:", "./wordpress")

        # Spodní navigační tlačítka
        self.tlacitka(
            text_zpet="Zpět", akce_zpet=lambda: self.mainw.predchozi_stranka(),
            text_dalsi="Další", akce_dalsi=self.dalsi
        )

    def dalsi(self):
        self.mainw.wordpress = [
            self.ziskej_port(),
            self.slozka1
        ]
        print(self.mainw.wordpress)
        self.mainw.dalsi_stranka()


"""class instalace(sablona):
    def __init__(self, mainw):
        super().__init__(mainw)
        
        nadpis = QtWidgets.QLabel("Instalace a konfigurace")
        nadpis.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
        self.obsah_layout.addWidget(nadpis)

        docker_check = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if docker_check.returncode != 0:
            QtWidgets.QMessageBox.critical(self, "Chyba", "Docker není nainstalován. Prosím nainstalujte Docker a zkuste to znovu.")
            return False
        return True

    def compose_file(self):
        # Vytvoření docker-compose.yml souboru
        with open("docker-compose.yml", "w") as f:
            f.write("services:\n")
            for app in self.mainw.vybrane_aplikace:
                if app == "Navidrome":
                    f.write(f"  navidrome:\n    image: deluan/navidrome\n    ports:\n      - {self.mainw.navidrome[1]}:4533\n")
                elif app == "Jellyfin":
                    f.write(f"  jellyfin:\n    image: jellyfin/jellyfin\n    ports:\n      - \"{self.mainw.stranka_jellyfin.port_input.text()}:8096\"\n")
                elif app == "Vaultwarden":
                    f.write(f"  vaultwarden:\n    image: vaultwarden/server\n    ports:\n      - \"{self.mainw.stranka_vaultwarden.port_input.text()}:8080\"\n")
                elif app == "Portainer":
                    f.write(f"  portainer:\n    image: portainer/portainer-ce\n    ports:\n      - \"{self.mainw.stranka_portainer.port_input.text()}:9000\"\n")
                elif app == "Immich":
                    f.write(f"  immich:\n    image: immich/immich-server\n    ports:\n      - \"{self.mainw.stranka_immich.port_input.text()}:2283\"\n")
                elif app == "Crafty Controller":
                    f.write(f"  craftycontroller:\n    image: craftycontrol/craftycontrol\n    ports:\n      - \"{self.mainw.stranka_craftycontroller.port_input.text()}:3000\"\n")
                elif app == "Home Assistant":
                    f.write(f"  homeassistant:\n    image: homeassistant/home-assistant\n    ports:\n      - \"{self.mainw.stranka_homeassistant.port_input.text()}:8123\"\n")
                elif app == "Pi-hole":
                    f.write(f"  pihole:\n    image: pihole/pihole\n    ports:\n      - \"{self.mainw.stranka_pihole.port_input.text()}:80\"\n")

        self.tlacitka(
            text_dalsi="Ukončit", 
            akce_dalsi=self.mainw.dalsi_stranka
        )
"""
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.ico"))
    
    okno = okno()
    okno.show()
    sys.exit(app.exec_())