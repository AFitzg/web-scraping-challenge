from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/arielfitzgerald/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    
    #Assign text to variables to be referenced later
    news_title = soup.find('div',class_ ="list_text").find('div',class_="content_title").text
    news_p = soup.find("div",class_="article_teaser_body").text

    jpl_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_img_url)

    browser.links.find_by_partial_text('FULL IMAGE').click()

    #visit the url for JPL Featured Space image

    #Find featured image and click using splinter
    jpl_img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_img_url)
    browser.links.find_by_partial_text('FULL IMAGE').click()


    #To get full size image navigate to more info for full res image
    browser.links.find_by_partial_text("more info").click()

    html = browser.html
    featured_img_soup = bs(html,"html.parser")

    img_url = featured_img_soup.find("figure", class_="lede").find('a').attrs['href']
    #print(img_url)

    #get main url for jpl nasa to match example url in instructions
    jpl_nasa_gov = 'https://www.jpl.nasa.gov'
    featured_image_url = f'{jpl_nasa_gov}{img_url}'
    
    #visit mars facts url
    mars_facts_url = 'https://space-facts.com/mars/'
    #read into pandas
    mars_facts_html = pd.read_html(mars_facts_url)

    #scrape table for only mars not mars v earth compare
    mars_only = mars_facts_html[0]

    #clean
    mars_only.columns=['Description','Mars']
    mars_only=mars_only.iloc[1:]
    mars_only.set_index('Description',inplace=True)

    #use pandas to conver the data to a HTML table string
    MARS = mars_only.to_html()

    #visit usgs astrogeology site to obtain high res images for Mars' hemispheres
    usgs_astrogeology_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_astrogeology_url)
    html = browser.html
    usgs_astrogeology_soup = bs(html,"html.parser")
    
    #print(usgs_astrogeology_soup.prettify())

    hemis = usgs_astrogeology_soup.find_all("div", class_="item")
    #print(hemis)

    #create an empty dictionary to store img_url and titles
    hemisphere_image_urls = []

    #loop through items in class items to get hemi img info.
    #Get title info for each hemisphere under correct tag
    #loop through each hemisphere url 
    mars_hemi_img_link_main = 'https://astrogeology.usgs.gov'

    for hemi in hemis:
        title = hemi.find("h3").text
        hemi_url = hemi.find("a").attrs["href"]
        marsss = mars_hemi_img_link_main + hemi_url
        browser.visit(marsss)
        mars_html = browser.html
        soup = bs(mars_html,"html.parser")
        img_url = soup.find("li").find("a").attrs["href"]
        title = title.strip('Enhanced')
        hemisphere_image_urls.append({"title":title, "img_url":img_url})

    # Quite the browser after scraping
    #browser.quit()

    #python dictionary containing all of the scraped data
    mars_info = {}

    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p
    
    mars_info['featured_image_url'] = featured_image_url
    mars_info['MARS'] = MARS

    mars_info['hemisphere_image_urls'] = hemisphere_image_urls

    #print(hemisphere_image_urls)

    # Return results
    return mars_info 
