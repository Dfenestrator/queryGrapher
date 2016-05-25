# queryGrapher

![Alt text](queryGrapher.jpg?raw=true "queryGrapher example")

A MySQL query graphing tool, written in Flask. Flask is a python web platform. It's similar to Django, but simpler, geared towards smaller projects. The graph output uses the Google Charts Line Chart API. Once you have all the dependencies, this project is ready to go, and includes a connection to a sample MySQL database. Please see the screenshot in this project for a sample.

To run this project, you need Python 2, Flask, and MySQL installed on your system. Once you have python and pip installed, you can run the following to get the right dependencies:

sudo pip install virtualenv  
sudo pip install Flask  
sudo pip install flask-mysqldb

If you are having trouble, please verify with Flask's and MySQL's documentation in case I am missing something in the list above.

Once all dependencies are in place, run the following:

python queryGrapher.py

Then, open up your browser window and go to:
http://localhost:5000

Enter your query and you are good to go! The output of the select query should be a set of columns, where the first column is the independent variable (x-axis) and the successive columns are the dependent variables (y-axis). Please see the screenshot for an example query. 

The example database is hosted on freemysqlhosting.net. The sample table provided is called popByState. It lists the populations of each state from 1960 to 2010. The first column is the year, and successive columns are states, as follows: (year, Alabama, Arkansas, California...)

The sample query "SELECT year, Alabama, California, Mississippi FROM popByState" generates a graph for the states Alabama, California, and Mississippi from the years 1960-2010 in 10 year increments. You can zoom in on the graph by boxing with your mouse. To reset your zoom, just right click.

If you have any questions/comments, raise an issue and I will try to address it.
