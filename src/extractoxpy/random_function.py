import requests
from rich.console import Console

console = Console()

def is_online(url='http://www.google.com', timeout=5):
    """
    Check if the internet is accessible by making a HEAD request.

    Parameters:
    - url: The URL to request (default is Google's homepage).
    - timeout: The timeout for the request (default is 5 seconds).

    Returns:
    - True if online, False otherwise.
    """
    try:
        response = requests.head(url, timeout=timeout)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False

def check_internet(verbose=True):
    """
    Check internet connection with verbose messaging.

    Parameters:
    - verbose: Boolean to display messages.
    """
    if verbose:
        console.print("Checking Internet Connection...")
    if not is_online():
        console.print("It seems that you are not connected to the internet!", style="bold red")
        return False
    else:
        if verbose:
            console.print("Internet connection OK...", style="green")
        return True

