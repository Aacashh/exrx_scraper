# Exercise Data Scraper from ExRx.net

## Introduction

This repository contains Python scripts for scraping exercise data from [ExRx.net](https://exrx.net/Lists/Directory). It collects information such as the exercise name, muscles involved, and the corresponding GIF images for each exercise.

## Features

- `ex_dir_scraper.py`: This script scrapes the links of all available exercises from ExRx.net's exercise directory.
- `exercise_scraper.py`: This script extracts detailed information about each exercise, such as the name of the exercise, muscles involved, and the corresponding GIF.

## Dependencies

- Python 3.x
- Selenium
- BeautifulSoup
- Requests

## How to Run

1. Clone the repository.
   ```bash
   git clone https://github.com/YourGitHubUsername/YourRepositoryName.git
   ```
2. Change to the directory.
   ```bash
   cd YourRepositoryName
   ```
3. Install the required packages.
   ```bash
   pip install -r requirements.txt
   ```
4. Run `ex_dir_scraper.py` to get the exercise directory links.
   ```bash
   python ex_dir_scraper.py
   ```
5. Run `exercise_scraper.py` to scrape individual exercise pages.
   ```bash
   python exercise_scraper.py
   ```

## Data

The scraped data will be saved in the following format:

- Exercise Name
- Muscles Involved
- Corresponding GIF link

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to ExRx.net for providing such comprehensive exercise data.
