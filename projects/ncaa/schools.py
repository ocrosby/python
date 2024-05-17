import os
import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

SCHOOLS_INDEX_URL = "https://www.ncaa.com/schools-index"


class School:
    short_name: str
    long_name: str
    ncaa_url: str
    division: str
    location: str


if __name__ == "__main__":
    if not os.path.isfile("schools.txt"):
        parsed_url = urlparse(SCHOOLS_INDEX_URL)
        protocol = parsed_url.scheme
        hostname = parsed_url.netloc
        prefix = f"{protocol}://{hostname}"

        response = requests.get(SCHOOLS_INDEX_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the 'a' tag with the text "Last »"
        last_page_link = soup.find('a', text='Last »')

        if last_page_link is None:
            raise ValueError("Could not find the last page link")


        # Extract the 'href' attribute
        href = last_page_link.get('href').strip()

        # Split the 'href' by '/' and get the last element
        page_number = href.split('/')[-1]

        # Convert the page number to an integer
        last_page = int(page_number)

        # Create a list of URLs for all the pages
        urls = [f"{SCHOOLS_INDEX_URL}/{i}" for i in range(1, last_page + 1)]


        schools = []
        for url in urls:
            print(f"Processing {url} ...")

            # For each page extract the school information
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', class_='responsive-enabled')
            rows = table.find_all('tr')

            for row in rows:
                cells = row.find_all('td')

                if len(cells) == 0:
                    continue

                current_school = School()

                anchor = cells[1].find('a')

                current_school.short_name = anchor.text.strip()
                current_school.ncaa_url = urljoin('https://www.ncaa.com', anchor.get('href').strip())
                current_school.long_name = cells[2].text.strip()

                schools.append(current_school)

        for school in schools:
            # Load the school page and extract the division, location, conference, nickname, and colors
            print(f"Processing {school.ncaa_url} ...")
            response = requests.get(school.ncaa_url)
            soup = BeautifulSoup(response.text, 'html.parser')

            division_location = soup.find('div', class_='division-location')

            school.division = ""
            school.location = ""

            if division_location:
                division_location = division_location.text.strip()
                division_location = division_location.replace("\n", "")
                if " - " in division_location:
                    try:
                        division, location = division_location.split(' - ')

                        school.division = division.strip()
                        school.location = location.strip()
                    except ValueError as err:
                        pass

        print("Sorting schools ...")
        # Sort the schools list by division and then by short_name within the same division
        schools = sorted(schools, key=lambda school: (school.division, school.short_name))

        print("Writing schools to file ...")
        with open("schools.csv", "w") as file:
            file.write("short_name,long_name,division,location,ncaa_url\n")
            for school in schools:
                file.write(f"{school.short_name},{school.long_name},{school.division},{school.location},{school.ncaa_url}\n")

        print("Done!")
