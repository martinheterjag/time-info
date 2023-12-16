import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from pyfiglet import figlet_format


def print_theme_of_the_day():
    # URL of the website
    url = "https://temadagar.se/"

    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("Failed to retrieve the page. Status code:", response.status_code)
        return

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the specific div containing the strings
    content_div = soup.find('div', id='content', class_='post-single-content box mark-links')

    # Check if the content_div is found
    if content_div:
        center_tag = content_div.find('center')
        try:
            a_tags = center_tag.find_all('a')
        except:
            print("En helt vanlig dag.")
            return

        # Process and print the text within each a tag
        for a_tag in a_tags:
            string_text = a_tag.get_text(strip=True)
            print(string_text)


def print_weather():
    # url_weather = 'https://wttr.in/Norrkoping?format=3'
    url_weather = 'https://wttr.in/Norrköping?q&m0&lang=sv'
    try:
        data = requests.get(url_weather)
        weather = data.text
    except:
        weather = "Hittar ej väder"
    print(weather.strip())

print_weather()
time = datetime.now().strftime("%H:%M")
print(figlet_format(time, font='doom').strip())
print(date.today().strftime("%d %b %Y"))
print('\033[93m--------------------------------\033[00m')
print_theme_of_the_day()

