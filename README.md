# Alyssum-Global-Services-Assignment
This project is for an assignment that was provided by Alyssum Global Services Pvt. Lt. for an Internship.

Objective: 

Develop a crawler for the following URL:  
https://www.cpppc.org:8082/inforpublic/homepage.html#/searchresult 
When you visit this page.. You will find list of various projects on this page in the bottom
You need to open one of the project listed and crawl the project page and save data in MySQL DB. For this assignment purpose you need not to crawl the entire data on the project page… Just pull some of the fields. 

Summary:

This project led me to explore a lot more with python. I started trying to scrape the table data using beautiful soup, however I came into an issue where most of the source code was hidden within javascript. So trying to explore more options, went for using Selenium which I knew about but never used before.
The complete project was donw with the help of the following modules :
-pandas: for creating the dataframe.
-googletrans: for translating the chinese characters.
-selenium: for automating through browser and extracting data.
-sqlalchemy: for connecting sql with python.


How to run:

-Add the requirements.txt file in your virtual environment.
-Install all the libraries using `pip install -r requirements.txt` command.
-Run the python file alyssum.py
