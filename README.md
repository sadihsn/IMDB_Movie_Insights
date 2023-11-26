# IMDB_Movie_List_Insights

## Problem Statement
The goal of this project is to get insights from a movie list in IMDB website.[this website](https://m.imdb.com/list/ls055559860/?page=1).<br/> 
Later we utilized the scraped data to understand the following movie data and correlations using Tableau Dashboard: 

1. Movie Ratings Distributions.
2. Rating vs. Gross Profit.
3. Gross Profit vs Rating vs Votes.
4. Gross Profit Distribution.
5. Rating and Duration.
6. Name of Movies by Age Rating.

You can visit the public dashboard [here](https://public.tableau.com/app/profile/sadi.hossain/viz/IMDBMovieListInsights/Dashboard1). 

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/sadi.hossain/viz/IMDBMovieListInsights/Dashboard1)

1.Most movies get ratings in the middle; not too high or too low.<br/>
2.Better-rated movies often make more money.<br/>
3.Good ratings and lots of votes usually mean more money for movies.<br/>
4.Most movies make a medium amount of money, with a few making a lot.<br/>
5.The length of a movie doesn't always decide how well it's rated.<br/>
6.Movie age ratings guide targeted content for audience preferences.<br/>


## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone https://github.com/sadihsn97/IMDB_Movie_Data.git
```
2. Intialize and activate virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads 
5. Run the scraper
```bash
python selenium_scraper/scraper.py --chromedriver_path <path_to_chromedriver>
```
6. To generate a csv file you can use 
   ```
    df.to_csv("Top_IMDB_Movies_insights.csv", index=False)
   ```

