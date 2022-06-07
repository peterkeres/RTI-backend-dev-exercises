# What tasks I completed

Just wanted to put a simple markdown file of what all tasks are completed. a 'birds eye' view.

### Tasks

0. Read the section below about **The Data**.
   1. completed, pretty straight forward
1. Write a SQL query that creates a consolidated dataset from the normalized tables in the database. In other words, write a SQL query that "flattens" the database to a single table.
   1. completed: Check for a table called 'flatten_data' in the sqlite database. Also attached a sql file of the query's used to set this up, its 'flatten_database.sql' 
2. Export the "flattened" table to a CSV file.
   1. completed: Used a py script to do this, the scipt used is 'make_flatten_data.py' and the csv file of the data is 'flatten_Data.csv'. Was going to use the built in csv export in pycharm but that felt like cheating.
3. Import the "flattened" table (or CSV file) into your programming language of choice (R, Python, Java, etc.) and put it into a data structure for analysis.
   1. completed: I put the data into a pandas dataframe. Check the 'exploratory_analysis.py' file. Also cleaned up some of the data here, replace ? with null and over_50k to a boolean.
4. Perform some simple exploratory analysis and generate summary statistics to get a sense of what is in the data.
   1. completed: Wasnt sure how much to really do here, just did 3 methods that look at the data.
      1. show a bar graph for race
      2. show a bar graph for sex
      3. show a bar graph for age
5. Create a simple web application that shows your analysis.
   1. kinda?: The data statics methos above kick out to a graph. so its not a 'web app', but there is some visual analysis going on. Flask would have been a good option here.
6. Create a paginated view of the data in your web application.
   1. NA
7. Generate one or more charts that you feel convey important relationships in the data.
   1. NA