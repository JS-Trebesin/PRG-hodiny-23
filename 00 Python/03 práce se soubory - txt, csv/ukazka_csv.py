import csv

# cesta = "K:\\gymplprogramovani\\python\\ukazky z hodin\\data.csv"
# with open(cesta, "r") as f:
#     reader = csv.reader(f, delimiter=";")
#     for x in reader:
#         print(x)


cesta = "K:\\gymplprogramovani\\python\\ukazky z hodin\\data.csv"
with open(cesta, "w", newline="") as f:
    jmeno = input("Zadej jméno: ")
    pocet = int(input("Zadej počet: "))
    writer = csv.writer(f, delimiter=";")
    writer.writerow([jmeno, pocet])