# web-scraping-challenge

Built a web application that scraped through various space related websites that pertained to the "Mission to Mars". Then create an index.html page that shows the results of the scrape. 

PT 1 - Scrape App
Used Jupyter notebook for initial scrape. Had to scrape the Nasa Mars New Site for the latest news title and paragraph. Needed to visit the url then by using beautiful soup I was able to view the html page contents to search for the correct tag reference that would allow me to pull the the title and paragraph. Same type of concept was used for the featured image of the day. Then I needed to visit a page to get mars facts and read it into pandas so that I could edit the table containing mars facts. Cleaned the table then converted it to an HTML string for reference in the final index.html file. Then had to take the url for where Mars' moon hemispheres are found and store the title and image url in a dictionary. Needed to append this to a list so that on the index.html file loop.

PT 2 - Mongo DB and Flask App
Converted Jupyter notebook to a python script for scraping where I called my scrape function. Stored this scraping script as a scrape route separately so that user could scrape separately. Main route/route route needed to query against my mongodb database and pass the info from the jupyter notebook into index.html.
Created index.html to display all of the scrape results.
