import csv
file_path = "K:\\gymplprogramovani\\python\\ukazky z hodin\\data.csv"
bludistaci = {}
with open(file_path, "r", newline="") as f:
    reader = csv.reader(f, delimiter=";")
    for radek in reader:
        bludistaci[radek[0]] = int(radek[1])

print(bludistaci)