from crud.entity.Baum import Baum
from crud.entity.Ast import Ast
from crud.entity.Blatt import Blatt

# Da Blatt den Ast nicht mehr referenziert, ist die Erstellung nun zirkelfrei
blatt1 = Blatt(id=1, farbe="Grün")
ast1 = Ast(id=1, eigenschaft="Knorrig", blatt=blatt1)

blatt2 = Blatt(id=2, farbe="Rot")
ast2 = Ast(id=2, eigenschaft="Gerade", blatt=blatt2)

baum1 = Baum(id=1, name="Eiche", ast=ast1)
baum2 = Baum(id=2, name="Ahorn", ast=ast2)

# Mock-Datenbank-Listen ("Tabellen")
baeume: list[Baum] = [baum1, baum2]
aeste: list[Ast] = [ast1, ast2]
blaetter: list[Blatt] = [blatt1, blatt2]
