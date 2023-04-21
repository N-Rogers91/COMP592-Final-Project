'''
Library for interacting with NASA's Astronomy Picture of the Day API.
'''
import requests
#from datetime import date
from datetime import datetime

#nasa_api_url = "https://api.nasa.gov/"
#api_url = f"https://api.nasa.gov/planetary/apod?api_key=6k6BWl9meM6Nq1GOg3Akhk8cEqMgDfQPleAZ7dDS&date={apod_date}"


def main():
    # TODO: Add code to test the functions in this module
    
    #apod_date = datetime.today().strftime('%Y-%m-%d')

    date = "2023-04-20"
    image_url = get_apod_info(date)
    print(image_url)


    return

def get_apod_info(date):
    """Gets information from the NASA API for the Astronomy 
    Picture of the Day (APOD) from a specified date.

    Args:
        apod_date (date): APOD date (Can also be a string formatted as YYYY-MM-DD)

    Returns:
        dict: Dictionary of APOD info, if successful. None if unsuccessful
    """

    today = datetime.today().strftime('%Y-%m-%d')
    first_date = datetime(1995,6,16).strftime('%Y-%m-%d')

    if date > today:
        print('Date cannot be greater than todays date')
    elif date < first_date:
        print('Date cannot be less than 1995-06-16')
    else:
    
    #apod_date = str(apod_date).strip().lower()#
 
        api_url = f"https://api.nasa.gov/planetary/apod?api_key=6k6BWl9meM6Nq1GOg3Akhk8cEqMgDfQPleAZ7dDS&date={date}"
        response = requests.get(api_url)
        response_json = response.json()
        image_url = response_json["url"]
        
    if response.status_code == 200:
        return image_url
    else:
        return None
  
  


def get_apod_image_url(apod_info_dict):
    """Gets the URL of the APOD image from the dictionary of APOD information.

    If the APOD is an image, gets the URL of the high definition image.
    If the APOD is a video, gets the URL of the video thumbnail.

    Args:
        apod_info_dict (dict): Dictionary of APOD info from API

    Returns:
        str: APOD image URL
    """
    return

if __name__ == '__main__':
    main()