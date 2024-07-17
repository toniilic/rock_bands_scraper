import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample URL (replace with the actual URL when known)
BASE_URL = "https://example.com/90s-rock-bands"

def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def scrape_band_data(url):
    soup = get_soup(url)
    if not soup:
        return []

    bands = []
    for band_section in soup.find_all("div", class_="band"):
        band_name = band_section.find("h2").text.strip()
        charted = band_section.find("span", class_="charted").text.strip()
        member_died = band_section.find("span", class_="member-died").text.strip()

        bands.append({
            "Band Name": band_name,
            "Charted": charted,
            "Member Died": member_died
        })

    return bands

def scrape_all_pages(base_url):
    page_number = 1
    all_bands = []

    while True:
        url = f"{base_url}?page={page_number}"
        logging.info(f"Scraping page {page_number}: {url}")
        bands = scrape_band_data(url)
        if not bands:
            break
        all_bands.extend(bands)
        page_number += 1

    return all_bands

def save_to_csv(data, filename="rock_bands.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    logging.info(f"Data saved to {filename}")

if __name__ == "__main__":
    band_data = scrape_all_pages(BASE_URL)
    save_to_csv(band_data)

