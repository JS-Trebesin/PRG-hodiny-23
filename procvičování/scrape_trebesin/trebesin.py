from bs4 import BeautifulSoup
import requests, json


def main():
    
    response = requests.get("https://www.trebesin.cz")

    soup = BeautifulSoup(response.content, "html.parser")



    all_p = soup.find_all("p")

    list_p = []

    for p in all_p:
        list_p.append(p.text)

    with open("trebesin_data.json", mode="w") as file:
        json.dump(list_p, file, indent=4, ensure_ascii=False)

    print(type(all_p))


if __name__ == "__main__":
    main()



