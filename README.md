# IMDB_Movie_List_Insights

## Problem Statement
The goal of this project is to get insights from a movie list in IMDB website.[this website](https://m.imdb.com/list/ls055559860/?page=1).<br/> 
Later we utilized the scraped data to understand the following movie data and correlations using Tableau Dashboard: 

1. Movie Ratings Distributions.<br/>
   Identify the most common movie rating in our dataset.
 <img src = "viz_images/1.png" width="450" height="250">
2. Rating vs. Gross Profit.
  Determine if there is a correlation between movie ratings and gross profit.
 <img src = "viz_images/2.png" width="450" height="250">
3. Gross Profit vs Rating vs Votes.
   Explore the relationship between the number of votes, movie rating, and
gross profit.
 <img src = "viz_images/3.png" width="450" height="250">
4. Gross Profit Distribution.
   Identify the category or segment in the tree map with the highest gross profit.
 <img src = "viz_images/4.png" width="450" height="250">
5. Rating and Duration.
   Examine if there is a noticeable relationship between movie rating and
duration.
 <img src = "viz_images/5.png" width="450" height="250">
6. Name of Movies by Age Rating.
   Identify the most common age ratings in our dataset and explore associated
movie names.
 <img src = "viz_images/6.png" width="450" height="250">

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
git clone https://github.com/sadihsn97/IMDB_Movie_List_Insights.git
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

