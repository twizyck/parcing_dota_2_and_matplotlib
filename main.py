import matplotlib.pyplot as plt
import selenium.common as selenium
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

import time

siteURL = "https://ru.dotabuff.com/heroes"

fullXpath = "/html/body/div[2]/div[2]/div[3]/div[5]/div[1]/div/div/div[2]/div[1]/div[2]/div/div[2]/table/tbody"


def main():
    browser = webdriver.Chrome()
    browser.get(siteURL)
    time.sleep(3)

    heroes = []
    winrates = []

    for i in range(10):
        try:
            name = browser.find_element(By.XPATH, fullXpath +f"/tr[{i+1}]" + "/td[1]").text
            winrate = browser.find_element(By.XPATH, fullXpath +f"/tr[{i+1}]" + "/td[3]").text

            winrate = float(winrate.strip('%').replace(',', '.'))

            heroes.append(name)
            winrates.append(winrate)
        except Exception as e:
            print(e)
            break


    time.sleep(2)
    browser.close()
    browser.quit()

    heroes, winrates = zip(*sorted(zip(heroes, winrates), key=lambda x: x[1], reverse=True))

    plt.figure(figsize=(15, 6))
    plt.barh(heroes[::-1], winrates[::-1], color='skyblue')  # Реверсируем списки для лучшего отображения
    plt.xlabel("Winrate (%)")
    plt.ylabel("Hero")
    plt.title("Winrate of Dota 2 Heroes")
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
