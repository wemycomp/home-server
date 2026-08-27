# Slovníček pojmů
## Definované třídy a jejich metody

- class main(QtWidgets.QWidget)
  - __init__(self, hlavni_okno)
    - Konstruktor základní šablony pro stránky. Vytváří hlavní QVBoxLayout (`self.main_layout`) a vnitřní `self.obsah_layout` pro obsah.
  - tlacitka(self, text_zpet=None, akce_zpet=None, text_dalsi=None, akce_dalsi=None)
    - Vytvoří vodorovné rozložení tlačítek (QHBoxLayout) a přidá tlačítka Zpět/Další podle předaných parametrů. Připojí signály `clicked` ke zadaným funkcím a přidá rozložení do `self.main_layout`.

- class vyber(main)
  - __init__(self, hlavni_okno)
    - Stránka s výběrem aplikací. Vytváří nadpis (QLabel), sadu checkboxů (QCheckBox) pro položky `aplikace` a tooltipy s popisy. Pro každý checkbox vytvoří řádek (QHBoxLayout) s checkboxem a ikonou nápovědy.
    - Přidá navigační tlačítko přes metodu `tlacitka` z nadřazené třídy.
  - dalsi(self)
    - Zpracuje zaškrtnuté položky, validuje (alespoň jedna vybraná) a uloží výsledek do `self.hlavni_okno.vybrane_aplikace`. Aktualizuje souhrnovou stránku a přepne `QStackedWidget` na index s přehledem.

- class souhrn(main)
  - __init__(self, hlavni_okno)
    - Stránka se souhrnem vybraných aplikací. Vytváří nadpis, QLabel (`self.vypis_label`) pro výpis a přidává navigační tlačítka (Zpět, Další).
  - aktualizuj_vypis(self)
    - Sestaví textový řetězec z položek `self.hlavni_okno.vybrane_aplikace` a vloží ho do `self.vypis_label` (jedna položka na řádek).
  - zpet(self)
    - Přepne `QStackedWidget` zpět na index 0 (stránka výběru).
  - dalsi(self)
    - Ukončí aplikaci voláním `QtWidgets.QApplication.quit()`.

- class okno(QtWidgets.QWidget)
  - __init__(self)
    - Hlavní okno aplikace. Nastaví titul, ikonu a pevnou velikost. Vytvoří `QStackedWidget` a přidá do něj instance `vyber` a `souhrn`. Uloží sdílený stav `self.vybrane_aplikace`.

## Spouštěcí blok
- app = QtWidgets.QApplication(sys.argv)
  - Vytvoření instance QApplication (nutné pro běh PyQt aplikace).
- app.setWindowIcon(QtGui.QIcon("icon.ico"))
  - Nastaví ikonu aplikace globálně.
- okno = okno()
  - Vytvoří hlavní okno.
- okno.show()
  - Zobrazí hlavní okno.
- sys.exit(app.exec_())
  - Spustí hlavní událostní smyčku Qt a ukončí proces po jejím skončení.

## PyQt5
- QtWidgets.QWidget
  - Základní widget — rodič pro vlastní komponenty.
- QtWidgets.QVBoxLayout / QHBoxLayout
  - Vertikální / horizontální layouty pro uspořádání widgetů.
- QWidget.setLayout(layout)
  - Nastaví layout pro widget.
- layout.addWidget(widget) / layout.addLayout(inner_layout) / layout.addStretch()
  - Přidání widgetu / pod-layoutu / pružné mezery do layoutu.
- QtWidgets.QLabel(text)
  - Textový štítek; používá se pro nadpisy i výpisy.
- QLabel.setFont(QtGui.QFont(...))
  - Nastaví písmo (rodinu, velikost, styl).
- QtWidgets.QCheckBox(text)
  - Zaškrtávací políčko s popiskem.
- QLabel.setToolTip(text)
  - Nastaví tooltip (nápovědu zobrazenou po najetí myší).
- QPushButton(text)
  - Tlačítko; signál `clicked` se připojuje k metodám/akcím.
- QPushButton.clicked.connect(function)
  - Připojí callback, který se zavolá po kliknutí.
- QtWidgets.QMessageBox.warning(parent, title, text)
  - Zobrazí varovné okno s informací pro uživatele.
- QtWidgets.QStackedWidget
  - Widget, který drží více „stránek“ a umožňuje přepínat mezi nimi pomocí indexu.
- QIcon(path)
  - Načte ikonu z cesty (použito pro okno a aplikaci).

---

- Sdílení stavu přes `self.hlavni_okno.vybrane_aplikace` je jednoduché a vhodné pro malou aplikaci; pro větší projekt doporučit využít signalů/slotů nebo oddělený model.