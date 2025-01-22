from bs4 import BeautifulSoup
import requests


def main():

    response = requests.get("https://www.arsenal.com/results")

    soup = BeautifulSoup(response.content, "html.parser")

    scores = soup.find_all(class_="scores__score")
    # scores = soup.select(".scores__score")

    # for score in scores:
    #     print(score.text)

    print(f"all scores {scores}")
    print(f"first score {scores[0]}")
    print(f"first score content {scores[0].text}")
    
    score_home = int(scores[0].text)
    score_away = int(scores[1].text)

    if score_home > score_away:
        print("Učitel má skvělou náladu")
    else:
        print("Učitel má otřesnou náladu")

    



if __name__ == "__main__":
    main()