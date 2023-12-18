from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns = ["movie_name", "year", "time", "rating", "metascore", "votes", "gross", "description", "Director", "Stars", "Image URLs"]

def get_movie_details(row):
    details = row.text.split("\n")

    contents = {}
    contents["movie_name"] = details[0]
    contents["year"] = details[1]
    contents["time"] = details[2]
    contents["rating"] = details[3]

    # Check if there are enough elements in the details list for metascore
    if len(details) > 4:
        contents["metascore"] = details[4]
    else:
        contents["metascore"] = None

    # Check if there are enough elements in the details list for votes
    contents["votes"] = details[5] if len(details) > 5 else None

    # Check if there are enough elements in the details list for gross
    contents["gross"] = details[6] if len(details) > 6 else None

    # Check if there are enough elements in the details list for description
    contents["description"] = details[7] if len(details) > 7 else None

    # Check if there are enough elements in the details list for Director
    contents["Director"] = details[8] if len(details) > 8 else None

    # Check if there are enough elements in the details list for Stars
    contents["Stars"] = details[9] if len(details) > 9 else None

    # Extracting Image URLs
    image_element = row.find_element(By.CLASS_NAME, "loadlate")
    contents["Image URLs"] = image_element.get_attribute("src")

    return contents

def main():
    webdriver_path = "/Users/sadihossain/Desktop/chromedriver-mac-arm64/chromedriver"
    
    movie_data = []

    service = ChromeService(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service)

    for page_id in range(1, 50):
        url = f"https://www.imdb.com/list/ls055559860/?page={page_id}"
        chrome_options = Options()
        driver.get(url)

        movie_names = driver.find_elements(By.CLASS_NAME, 'lister-list')

        for movie_list in movie_names:
            rows = movie_list.find_elements(By.CLASS_NAME, 'lister-item')

            for row in rows:
                movie_data.append(get_movie_details(row))

        time.sleep(5)

        print(len(movie_data))
        print(movie_data)

    driver.quit()

    df = pd.DataFrame(data=movie_data, columns=columns)
    df.to_csv("Top_IMDB_Movies_insights.csv", index=False)

if __name__ == "__main__":
    main()
