from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://socialeagle.ai")

        # Better wait strategy
        page.wait_for_load_state("domcontentloaded")

        content = page.inner_text("body")

        with open("socialeagle.txt", "w", encoding="utf-8") as f:
            f.write(content)

        print("Content saved successfully!")

        browser.close()

main()