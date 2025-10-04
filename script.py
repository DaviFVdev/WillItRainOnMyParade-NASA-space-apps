import os
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    
    # Get the absolute path to the index.html file
    file_path = os.path.abspath("index.html")
    
    page.goto(f"file://{file_path}")

    # Expect the main heading to be visible
    expect(page.get_by_role("heading", name="Bem vindo ao Clima IA")).to_be_visible()

    # Expect the form elements to be visible
    expect(page.get_by_label("Location:")).to_be_visible()
    expect(page.get_by_label("Date:")).to_be_visible()
    expect(page.get_by_role("button", name="Search")).to_be_visible()

    # Fill out the form
    page.get_by_label("Localização:").fill("São Paulo")
    page.get_by_label("Data:").fill("2025-10-04")

    page.screenshot(path="jules-scratch/verification/verification.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)