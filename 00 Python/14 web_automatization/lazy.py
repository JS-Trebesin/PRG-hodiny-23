from playwright.sync_api import sync_playwright


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")

        page.click('span[class="login pl-2"]')

        page.fill('input[id="username"]', "souhrada")

        input("Klikni na cokoliv pro zavření prohlížeče")
        browser.close()

if __name__ == "__main__":
    main()