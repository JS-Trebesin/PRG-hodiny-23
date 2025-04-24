seznam_ovoce = ["jablko", "mandarinka", "pomeranč", "banán"]

seznam_ovoce.append("kiwi")

print(seznam_ovoce[1])

print(len(seznam_ovoce))

seznam_ovoce[0] = "hruška"


odebrane_ovoce = seznam_ovoce.pop(1)
print(f"Bylo odebráno ovoce: {odebrane_ovoce}")


for index, ovoce in enumerate(seznam_ovoce):
    print(f"{index+1}. {ovoce}")

if "pomeranč" in seznam_ovoce:
    print("Yay!")


tel_seznam = {
    "Květoslav": "777 123 456",
    "Jarmila": "666 666 666",
    "Kazi": "765 431 111"
}

for key in tel_seznam.keys():
    print(key)

for x in tel_seznam:
    print(x)



for v in tel_seznam.values():
    print(v)

for y in tel_seznam:
    print(tel_seznam[y])



for key, value in tel_seznam.items():
    print(key, value)


tel_seznam["Kazi"]
tel_seznam.get("Kazi", "Nic tam není")