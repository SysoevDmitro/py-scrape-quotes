from dataclasses import dataclass
import requests
import csv
from bs4 import BeautifulSoup


@dataclass
class Quote:
    text: str
    author: str
    tags: list[str]


def main(output_csv_path: str) -> None:
    url = requests.get("https://quotes.toscrape.com")
    soup = BeautifulSoup(url.text, "html.parser")

    quotes = soup.findAll("span", attrs={"class": "text"})
    authors = soup.findAll("small", attrs={"class": "author"})
    tags = soup.findAll("div", attrs={"class": "tags"})

    with open(output_csv_path, "w", encoding="utf-8", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=",")
        csv_writer.writerow(["text", "author", "tags"])

        for quote, author, tag in zip(quotes,
                                      authors,
                                      tags):
            csv_writer.writerow([quote.text, author.text,
                                 tag.text.split()[1:]])


if __name__ == "__main__":
    main("quotes.csv")
