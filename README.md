# IMDB_Movie_Insights(andreea_nastasa)

## Problem Statement
The goal of this project is to get insights from a movie list in IMDB website.[Link](https://m.imdb.com/list/ls055559860/?page=1).<br/> 
The scraped data was from a movie list created by andreea_nastasa based on his/her personal preferences.I have explored a large set of data to learn important things about movies because I'm really interested in the whole movie scene.<br>

Used google sheets and python to clean the messy dataset and missing values,after cleaning the data set contains columns such as 'movie_name','Year','Age','Duration','Rating','Gross Profit',and 'Votes' with 1965 rows.Initial scraped data contains 4900 records<br>

Later we utilized the scraped data to understand the following movie data and correlations using Tableau Dashboard: 

1. Movie Ratings Over the Years.(Line graph)<br>
   Illustrates how movie ratings have evolved across different years.
 <img src = "viz_images/1.png" width="450" height="250">
2. Movie Duration Distribution.(Histogram)<br>
   Displays the frequency distribution of movie durations, showing the range and frequency of different durations.
 <img src = "viz_images/2.png" width="450" height="250">
3. Relationship Between Ratings and Gross Profit.(Scatter Plots)<br>
   Reveals the correlation between movie ratings and their corresponding gross profits through individual data points.
 <img src = "viz_images/3.png" width="450" height="250">
4. Average Ratings by Age Group.(Bar Chart)<br>
   Depicts the average movie ratings for different age groups, providing a summary of audience preferences.
 <img src = "viz_images/4.png" width="450" height="250">
5. Movie Count by Year.(Bar Chart)<br>
   Shows the number of movies released each year, providing an overview of the industry's output over time.
 <img src = "viz_images/5.png" width="450" height="250">
6. Votes Distribution.(Tree Maps)<br>
  Visualizes the distribution of votes across different categories,offering insights into audience engagement and preferences.
 <img src = "viz_images/6.png" width="450" height="250">

You can visit the public dashboard [here](https://public.tableau.com/app/profile/sadi.hossain/viz/IMDB_Movie_Insights/Dashboard1). 

## Findings and Observations from the [Dashboard](https://public.tableau.com/app/profile/sadi.hossain/viz/IMDB_Movie_Insights/Dashboard1)

1.Ratings saw a consistent rise post-2000, peaked in 2014, and then declined, signaling a noteworthy shift in audience response or industry dynamics.<br/>
2.Most movies fall within the 90 to 110-minutes range, showing a clear preference that aligns with audience tastes and market demands.<br/>
3.No clear correlation between higher ratings and greater profits, emphasizing the need for a nuanced understanding of factors influencing financial success.<br/>
4.A substantial number of movies cater to Teen/Adults (Age > 13), reflecting a prevailing trend towards mature content.<br/>
5.The dataset is concentrated between 2000 and 2020, highlighting a significant period of cinematic output.<br/>
6.Identifies movies with the highest vote counts, providing insights into audience favorites and significant public engagement within the dataset.<br/>



## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
git clone https://github.com/sadihsn97/IMDB_Movie_Insights.git
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
python web_scraping_IMDB/scraper.py --chromedriver_path <path_to_chromedriver>
```
6. To generate a csv file you can use 
   ```
    df.to_csv("IMDB_Movies_Insights.csv", index=False)
   ```

