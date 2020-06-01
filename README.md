# NLP on Bike Craze Based On Location
This project is a part of Data Science hobby projects of mine.

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to use the Natural Language Processing techniques to find the current craze of bikes based on Location. As the country changes the types of bikes preferred by people changes , For example most people in India uses Low end bikes that are sufficient to meet their daily commute needs unlike in countries like Ireland where bike prices are very costly when compared to India. There are many other arbitary factors that influcene the bikes craze in any location such as weather, price, look and feel, roads, traffic rules etc. Because of these many factors the likebaility on bikes is every changing and dynamic. This project is mainly to provide solution/help those to get a quick overview of the current craze of a bike by location based on Tweets by users in the location.


### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Natural Language Processing
* Web Scraping
* Twitter
* Data Cleaning


### Technologies
* Python
* Json
* Pandas, jupyter
* HTML

* PLease look at requirements file [here](https://github.com/tejeshb/Near_RealTime_NLP_On_Bike_Craze_By_Location/blob/master/requirements.txt)


## Project Description
As countries have different bike companies and I dont want to put an extra load on Twitter API usage by searching through all the bike companies hashtags that exist in the world and so I have implemented a search of only the bike comapanies that exist in the user country. Used wikipedia page (https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers) to get the list of countries and its bike companies. The wikipedia page was scraped using Beautiful Soup library. 
Twitter API (free tier) is used to get the tweets based on bike names. All the tweets are cleaned and visualized.



## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is extracted from wikipedia page [here]( https://en.wikipedia.org/wiki/List_of_motorcycle_manufacturers)
3. Wikipedia page extration file is kept [here](https://github.com/tejeshb/Near_RealTime_NLP_On_Bike_Craze_By_Location/blob/master/wiki.py)
4. Location extraction / near by location search is done [here](https://github.com/tejeshb/Near_RealTime_NLP_On_Bike_Craze_By_Location/blob/master/loc.py)
5. Twitter API script to call, search, preprocess, clean and Visulaize can be found [here](https://github.com/tejeshb/Near_RealTime_NLP_On_Bike_Craze_By_Location/blob/master/twitter.py)

## Notebook

Please find the [notebook](https://github.com/tejeshb/NLP_On_Bike_Craze_By_Location/blob/master/Bike%20and%20Twitter.ipynb) to get a quick grasp at the whole project.



#### My Details:

|Name     |  Git Hub Handle   | Website  |
|---------|-----------------|--------------|
|[Tejesh Batapati]| https://github.com/tejeshb   | https://tejesh-ai.webflow.io/|

Feel free to look at my personal projects website here [tejesh.AI] (https://tejesh-ai.webflow.io/)

