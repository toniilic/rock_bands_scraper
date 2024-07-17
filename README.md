# 90's Rock Bands Scraper

This project is a sample web scraper for extracting data about 90's rock bands using Python and Beautiful Soup. The script scrapes information about bands and their members, such as whether their album charted and whether a band member has died.

## Features

- Scrapes band name, charting status, and member death information.
- Saves the scraped data to a CSV file.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/toniilic/rock_bands_scraper.git
    cd rock_bands_scraper
    ```

2. **Set up the virtual environment and install dependencies:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install requests beautifulsoup4 pandas
    ```

## Usage

1. **Run the scraper:**

    ```bash
    python scraper.py
    ```

2. **Check the output CSV file:** `rock_bands.csv` will be created in the project directory.

## Future Improvements

- Handle pagination for websites with multiple pages of data.
- Add error handling and logging.
- Expand the scraper to collect more detailed information.

## License

This project is licensed under the MIT License.

