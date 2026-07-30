"""
Tento soubor je hlavním spouštěcím souborem, kde se pouze volají funkce z jiných souborů.
"""

from aplikace import *

apps = vyber_aplikaci()

file()
if "navidrome" in apps:
	navidrome()