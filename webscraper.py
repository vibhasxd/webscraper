# Import necessary libraries
import csv
import requests
from bs4 import BeautifulSoup 

# The URL of the website you want to scrape
url = "https://www.dineout.co.in/mumbai-restaurants"

# Send a GET request to the website
response = requests.get(url) 

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Look for the specific HTML tags that contain the restaurant info
restaurants = soup.find_all('div', class_="restnt-card")

# Open (or create) a CSV file with write permissions
with open('restaurants.csv', 'w', newline='') as file:
    writer = csv.writer(file) # Create a csv writer object
    writer.writerow(["Name", "Rating"]) # Write the header row

    # Loop through the list of restaurant tags
    for restaurant in restaurants: 
        # Extract the restaurant's name
        name = restaurant.find('a', class_='restnt-name').text.strip()
        # Extract the restaurant's rating
        rating = restaurant.find('div', class_='restnt-rating').text.strip()
        # Print the name and rating
        writer.writerow([name, rating]) 
