'''Zadanie 1'''
zmienna1 = int(5)
zmienna2 = int(2)
zmienna3 = float(20.8)
zmienna4 = float(1.3)
print(f"Wartość int: {zmienna1} oraz {zmienna2}"
      f"\n Wartość float {zmienna3} oraz {zmienna4}")

'''Zadanie 2'''
zmienna = int(5)
zmienna2 = float(2.2)
zmienna3 = float(2)
wynik = int.bit_count(zmienna)
print(f"Wartość {zmienna} to {wynik}")
print("Fałsz: ", float.is_integer(zmienna2))
print("Prawda: ", float.is_integer(zmienna3))

'''Zadanie 3'''
binarnie = bin(10)
calkowicie = int(binarnie, base = 2) #base = 2 oznacza ze jest to system dwojkowy czyli 0 i 1
print(f"Liczba całkowita {calkowicie} na ciąg binarny to {binarnie}") #0b to pokazuje ze jest to ciag binarny

'''Zadanie 4 '''
x = int(5)
y = int(2)
print(f"Alternatywa rozłączna: {x^y} \n"
      f"Koniunkcja: {x&y} \n"
      f"Przesunięte w lewo o n bitów: {x<<y} \n"
      f"Przesunięte w prawo o n bitów: {x>>y} \n"
      f"Negacja x: {~x} \n"
      f"Negacja y: {~y} \n")

'''Zadanie 5'''
przecinek = float(2.2)
szesnastkowa = float.hex(przecinek)
print(f"Wartość {przecinek} szesnastkowo {szesnastkowa}")
powrot = float.fromhex(szesnastkowa)
print(f"Wartość {szesnastkowa} zmiennoprzecinkowo {powrot}")