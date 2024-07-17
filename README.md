# 90's Rock Bands Scraper

This project is a sample web scraper for extracting data about 90's rock bands using Python and Beautiful Soup. The script scrapes information about bands and their members, such as whether their album charted and whether a band member has died.

## Features

- Scrapes band name, charting status, and member death information.
- Handles pagination to scrape multiple pages of data.
- Includes error handling and logging.
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

## Project Structure

```
rock_bands_scraper/
├── scraper.py
├── README.md
├── .gitignore
├── venv/
└── rock_bands.csv (generated after running the script)
```

## Future Improvements

- Expand the scraper to collect more detailed information about each band.
- Add support for additional data sources.
- Implement a more robust data cleaning and validation process.

## License

This project is licensed under the MIT License.
