import sqlite3 as lite
import pandas as pd

# Connect to getting_started database
con = lite.connect('getting_started.db')

# Add data for tables

cities = (('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'), ('Miami', 'FL'), ('Dallas', 'TX'), ('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA'), ('Los Angeles', 'CA'))
weather = (('New York City', 2013, 'July', 'January', 62), ('Boston', 2013, 'July', 'January', 59), ('Chicago', 2013, 'July', 'January', 59), ('Miami', 2013, 'August', 'January', 84), ('Dallas', 2013, 'July', 'January', 77), ('Seattle', 2013, 'July', 'January', 61),('Portland', 2013, 'July', 'December', 63),('San Francisco', 2013, 'September', 'December', 64), ('Los Angeles', 2013, 'September', 'December', 75))

with con:
    cur = con.cursor()
	
	# Clear database of old data
	
	cur.execute("DROP TABLE IF EXISTS <cities>")
	cur.execute("DROP TABLE IF EXISTS <weather>")
	
	# Create tables in database
	
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather (name text, year integer, warm_month text, cold_month text, average_high integer)")
	
	# Add new data to database
	
	cur.executemany("INSERT INTO cities VALUES (?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES (?,?,?,?,?)", weather)
	
	# Join data from tables - cities and weather
	
	cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON cities.name")
	
	# Find hottest cities in July
	
	cur.execute("SELECT cities.name, state, year, warm_month, cold_month, AVG(average_high) 
				FROM cities 
				INNER JOIN weather ON cities.name 
				ORDER BY warm_month = 'July' 
				WHERE AVG(average_high) > '65'")
	
	# Load into Pandas dataframe
	
	rows = cur.fetchall()
	df = pd.DataFrame(rows)
	for row in rows:
	    return row
	
	#Print statement
	
	"Cities that are hottest in July are:" row