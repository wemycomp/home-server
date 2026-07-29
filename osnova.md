---
categories:
date: 2026-07-29
tags:
---
# Osnova ročníkové práce
## Domácí server
# Název
Domácí server jednoduše (pracovní název)
Obor: Informatika
# Prohlášení
# Poděkování
# Anotace
Práce se zabývá problematikou domácích serverů a za cíl si klade vytvořit jednoduchou aplikaci, která uživatele provede instalací serveru na svém vlastním domácím počítači. Takovýto server bude podle volby uživatele umožňovat pomocí řady aplikací prohlížení fotek a filmů, ukládání dalších souborů a poznámek, hostování vlastního Minecraft serveru, ukládání hesel a jiných přistupových klíčů, blokování reklam a sledovacích prvků při prohlížení webu, hostování vlastní webové stránky a správu chytré domácnosti. To vše jednoduše přes vyladěný webový interface.
# Klíčová slova
Ročníková práce; Gymnázium a ZUŠ Šlapanice; networking; domácí server; server; chytrá domácnost; informatika; programování; Docker; WSL; Windows; protokoly FTP, SMB, HTTP, SSH; DNS; Immich; Jellyfin; DuckDNS; Cloudflare; Portainer; Github; Nginx Proxy; Crafty Controller; Bitwarden; Pi-hole; Glance; Cisco Packet Tracer; Python; Obsidian; Home Assistant; Wordpress; PyInstaller
# Úvod
- Souhrnný popis práce,
- zmínění používaných nástrojů (Docker; WSL; Windows; protokoly FTP, SMB, HTTP, SSH; DNS; Immich; Jellyfin; Navidrome; DuckDNS; Cloudflare; Portainer; Github; Nginx Proxy; Crafty Controller; Bitwarden; Pi-hole; Glance; Cisco Packet Tracer; Python; Obsidian; Home Assistant; Wordpress; PyInstaller),
- popis cílů práce,
- popis praktické části, kterou bude tvorba aplikace usnadňující instalaci všech potřebných aplikací a jiných nástrojů
# 1. Teoretická část
## 1.1. Úvod do networkingu
- Vysvětlení telekomunikační terminologie používané v práci
- Popis a vylíčení struktury domácí sítě, do které implementujeme náš server v praktické části
- Teoretická úvaha nad exposováním aplikací serveru na internet a souhrn způsobů, jak nejefektivněji k aplikacím přistupovat jinak, než přes domácí síť
## 1.2. Představení nástrojů používaných při nastavování serveru
- Představení Dockeru
- WSL – potřebujeme ke spuštění Dockeru na Windows
- Jak spolu fungují služby Cloudflare, DuckDNS a Nginx Proxy
- Představení programovacího jazyka Python
## 1.3. Výhody vytvářené aplikace oproti manuálnímu postupu
- Popis funkce serveru a manuální postup jeho konfigurace
# 2. Praktická část
## 2.1. Představení konceptu aplikace a představení aplikací serveru
- Co vytvářená aplikace umožňuje
	- stažení všeho potřebného softwaru,
	- volba aplikací serveru,
	- automatický Docker compose,
	- pomoc s dodatečnou manuální instalací
- Jaké aplikace si může uživatel na server stáhnout a k čemu slouží
	- Immich,
	- Jellyfin,
	- Pi-hole,
	- Glance,
	- Portainer,
	- Nginx Proxy + DuckDNS,
	- Obsidian,
	- Home Assistant,
	- SMB Server,
	- FTP Server,
	- Wordpress,
	- Crafty Controller,
	- Bitwarden
## 2.2. Tvorba aplikace podle navrhovaného konceptu
- Tvorba skriptu pomocí programovacího jazyka Python, který umožní snadnou instalaci všeho potřebného a provede nastavením serveru.
- Zabalení skriptu do spustitelné aplikace pomocí PyInstaller
- Aplikace bude obsahovat všechny potřebné vysvětlivky a bude intuitivní na používaní, proto není k aplikaci potřeba vytvářet uživatelský manuál nebo číst samotnou práci
## 2.3. Ověřování funkčnosti aplikace
- Ukázka průchodu instalací serveru pomocí vytvořené aplikace krok po kroku
# Závěr
- Zhodnocení práce, poukázání na možné chyby a složité pasáže
# Přílohy
## I. Seznam zkratek
## II. Seznam obrázků a tabulek
## III. Skript aplikace v Pythonu
## IV. DVD se spustitelným programem