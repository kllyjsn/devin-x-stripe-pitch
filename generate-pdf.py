from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 720})
    page.goto("file:///home/ubuntu/pitch-deck/index.html")
    time.sleep(3)
    page.pdf(
        path="/home/ubuntu/pitch-deck/Devin_x_Stripe_Pitch_Deck.pdf",
        width="1280px",
        height="720px",
        print_background=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
    )
    browser.close()
    print("PDF generated successfully!")
