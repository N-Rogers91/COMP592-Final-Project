import inspect

import requests
from datetime import datetime
import os
import requests

#function that is able to handle API data
import ctypes

def main():
   #asks user to print text in format
    print('Date format: YYYY-MM-DD')
   
    #where user to inputs date
    date = input('Date: ')
   
    #passes date through funtion to return url
    image_url = get_apod_image(date)
   
    #print the url 
    print(image_url)
    
    #sets directory variable to directoy script is in
    directory = get_script_dir()

    #function is suppose to set wallpaper by pulling image from directory
    set_wallpaper_from_url(image_url, directory)


def get_apod_image(date):

    #this sets variable to function that will call todays date in none there
    today = datetime.today().strftime('%Y-%m-%d')

    #this variable is set to a function that limits the oldest date that can be selected
    first_date = datetime(1995,6,16).strftime('%Y-%m-%d')

    #if statement that sets todays date if none provided
    if date == '':
        date = today
    
    #if statement that prints text saying cannot be greater date, if user selects one
    if date > today:
        print('Date cannot be greater than todays date')

    #elif statment that prints statement saying if date is older then 1995-06-26, then it cannot be used    
    elif date < first_date:
        print('Date cannot be less than 1995-06-16')

    #if requirments are meant, then it will return url with APOD of selected date
    else:
        api_url = f"https://api.nasa.gov/planetary/apod?api_key=6k6BWl9meM6Nq1GOg3Akhk8cEqMgDfQPleAZ7dDS&date={date}"
        response = requests.get(api_url)
        response_json = response.json()
        image_url = response_json["url"]
        return image_url

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    ## DO NOT CHANGE THIS FUNCTION ##
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

def set_wallpaper_from_url(image_url, save_path):

    #
    os.chmod(os.path.dirname(save_path+'\images'), 0o777)

    # Download the image from the URL
    response = requests.get(image_url)
    image_content = response.content

    # Make sure the directory for the save path exists
    os.makedirs(os.path.dirname(save_path+'\images'), exist_ok=True)

    # Save the image to the specified file path
    with open(save_path+'\images', 'wb') as f:
        f.write(image_content)

    # Set the desktop wallpaper using the saved file path
    set_wallpaper = 20
    ctypes.windll.user32.SystemParametersInfoW(set_wallpaper, 0, os.path.abspath(save_path+'\images'), 3)

    # Set permissions for the directory to allow writing
    os.chmod(os.path.dirname(save_path+'\images'), 0o777)

if __name__ == '__main__':
    main()