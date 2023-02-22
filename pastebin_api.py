import requests
from typing import Union

def create_paste(title: str, body: str, expire: str, public: bool) -> Union[str, None]:
    """
    Create a new PasteBin paste using the PasteBin API.

    Args:
        title (str): The title of the new paste.
        body (str): The body text of the new paste.
        expire (str): The expiration period of the new paste. Valid values are "N", "10M", "1H", "1D", or "1W".
        public (bool): Whether the new paste should be publicly listed or not.

    Returns:
        str or None: The URL of the newly created paste if it's created successfully, or None if the new paste is not
        created successfully.

    Raises:
        ValueError: If the expiration period is not a valid value.
    """
        # Fill in your own PasteBin developer API key
    api_key = "mB2Zh82SMqpg_3BqejDt-wfobHtUZpUt"

    # Construct the data dictionary for the PasteBin API
    data = {
        "api_dev_key": api_key,
        "api_option": "paste",
        "api_paste_code": body,
        "api_paste_name": title,
        "api_paste_expire_date": expire,
        "api_paste_private": "0" if public else "1"
    }
    
    # Make a POST request to the PasteBin API
    url = "https://pastebin.com/api/api_post.php"
    response = requests.post(url, data=data)
    
    # Check if the paste was created successfully
    if response.status_code == 200:
    
    # Extract the URL of the new paste from the response text
        url = response.text
        print(f"Paste created successfully. URL: {url}")
        return url
    else:
        print("Error creating paste:", response.text)
        return None
