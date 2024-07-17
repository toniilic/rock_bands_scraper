import requests
from bs4 import BeautifulSoup
import pandas as pd

# Sample URL (replace with the actual URL when known)
url = "https://example.com/90s-rock-bands"

def scrape_band_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    bands = []
    for band_section in soup.find_all("div", class_="band"):
        band_name = band_section.find("h2").text
        charted = band_section.find("span", class_="charted").text
        member_died = band_section.find("span", class_="member-died").text

        bands.append({
            "Band Name": band_name,
            "Charted": charted,
            "Member Died": member_died
        })

    return bands

def save_to_csv(data, filename="rock_bands.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    band_data = scrape_band_data(url)
    save_to_csv(band_data)

