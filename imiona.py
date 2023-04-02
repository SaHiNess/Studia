tabela1 = ['Alicja','Weronika','Maciek']
zbior1 = set(tabela1)

tabela2 = ['Damian','Mariusz','Halina']
zbior2 = set(tabela2)

tabela3 = ['Weronika','Wiktoria','Łukasz']
zbior3 = set(tabela3)

print("\nZbiór A+B\n")
print(tabela1 + tabela2)
print("\nZbiór A+B+C\n")
print(tabela1 + tabela2 + tabela3)
print("\nZbiór C ale nie ma ich w A\n")
zad3=zbior3.difference(zbior1)
print(zad3)
print("\nZbiór B ale nie ma ich w A i C\n")
zad4=zbior2.difference(zbior1,zbior3)
print(zad4)
print("\nW przynajmniej jednym ze zbiorów\n")
zad5=zbior1.union(zbior2,zbior3)
print(zad5)
print("\nZbiór A ale nie ma ich w SUMIE zbiorów B i C\n")
zad6=zbior1.difference(zbior2.union(zbior3))
print(zad6)