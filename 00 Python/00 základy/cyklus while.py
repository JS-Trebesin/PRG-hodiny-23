import random


odpovedi = ["Ano", "Stopro", "Určitě", "Možná", "Nemyslím si", "Ne", "Zkus to znovu"]


while True:
  otazka = input("What is your question?\n")
  if otazka == "konec":
    break
  odpoved = random.randint(0, 6)
  print(odpovedi[odpoved])


  
  
  


