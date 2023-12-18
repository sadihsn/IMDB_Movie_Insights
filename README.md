# IMDB_Movie_Insights

## Problem Statement
The goal of this project is to get insights from a movie list in IMDB website.[Link](https://m.imdb.com/list/ls055559860/?page=1).<br/> 
Later we utilized the scraped data to understand the following movie data and correlations using Tableau Dashboard: 

1. Movie Ratings Distributions.<br>
   Identify the most common movie rating in our dataset.
 <img src = "viz_images/1.png" width="450" height="250">
2. Rating vs. Gross Profit.<br>
  Determine if there is a correlation between movie ratings and gross profit.
 <img src = "viz_images/2.png" width="450" height="250">
3. Gross Profit vs Rating vs Votes.<br>
   Explore the relationship between the number of votes, movie rating, and
gross profit.
 <img src = "viz_images/3.png" width="450" height="250">
4. Gross Profit Distribution.<br>
   Identify the category or segment in the tree map with the highest gross profit.
 <img src = "viz_images/4.png" width="450" height="250">
5. Rating and Duration.<br>
   Examine if there is a noticeable relationship between movie rating and
duration.
 <img src = "viz_images/5.png" width="450" height="250">
6. Name of Movies by Age Rating.<br>
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

## Recommendations:<br>
1.Diversify Ratings and Genres: Include movies with various ratings for a broader audience.<br>
2.Emphasize Quality Content: Highlight well-rated movies, showcasing the link between ratings and revenue.<br>
3.Highlight Popular Movies: Showcase movies with good ratings and a significant number of votes.<br>
4.Feature Medium-Budget Films: Include successful medium-budget films for a balanced selection.<br>
5.Incorporate Age Ratings: Guide users with age ratings to match their preferences.<br>
6.Interactive Recommendations: Implement filters for ratings, revenue, and genre for user customization.<br>
7.Include User Reviews: Integrate user reviews and comments for a social aspect.<br>
8.Regular Updates: Keep the list dynamic with new releases and popular films.<br>




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

