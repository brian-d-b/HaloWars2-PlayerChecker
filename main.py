import requests
import webbrowser
import os

def check_hw2allunits(url):
    """
    Checks if the hw2allunits website is up.
    
    Args:
        url (str): The URL of the hw2allunits website to check.
    
    Returns:
        bool: True if the website is up, False if it is down (403 error).
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True  # Website is up
        else:
            return False  # Website is down or some other issue
    except requests.RequestException:
        return False  # Unable to connect or other error

def open_gamertag_tabs_hw2allunits(base_url, gamertags):
    """
    Opens browser tabs for each gamertag with the hw2allunits base URL.
    
    Args:
        base_url (str): The base URL of the hw2allunits website.
        gamertags (list of str): List of gamertags to append to the URL.
    """
    for tag in gamertags:
        formatted_tag = tag.replace(' ', '+')
        full_url = f"{base_url}?PlayerTag={formatted_tag}"
        webbrowser.open_new_tab(full_url)

def open_gamertag_tabs_halowarpoint(base_url, gamertags):
    """
    Opens browser tabs for each gamertag with the halowarpoint base URL.
    
    Args:
        base_url (str): The base URL of the halowarpoint website.
        gamertags (list of str): List of gamertags to append to the URL.
    """
    for tag in gamertags:
        formatted_tag = tag.replace(' ', '%20')  # Replace spaces with %20 for halowarpoint
        full_url = f"{base_url}/ranks/{formatted_tag}"
        webbrowser.open_new_tab(full_url)

def main():
    hw2allunits_url = "https://hw2allunits.azurewebsites.net/"
    halowarpoint_url = "https://halowarpoint.com"

    # Check if hw2allunits is up
    if check_hw2allunits(hw2allunits_url):
        print("Choose a website:")
        print("1. hw2allunits")
        print("2. halowarpoint")
        choice = input("Enter 1 or 2: ")
    else:
        print("Warning: hw2allunits is currently down. Using halowarpoint instead.")
        choice = "2"

    if choice == "1":
        gamertag_input = input("Enter gamertags, separated by a comma (no spaces): ")
        gamertags = gamertag_input.split(',')
        open_gamertag_tabs_hw2allunits(hw2allunits_url, gamertags)
    elif choice == "2":
        gamertag_input = input("Enter gamertags, separated by a comma (no spaces): ")
        gamertags = gamertag_input.split(',')
        open_gamertag_tabs_halowarpoint(halowarpoint_url, gamertags)
    else:
        print("Invalid choice. Exiting program.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
