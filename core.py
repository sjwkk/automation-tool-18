import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_retries:
                time.sleep(delay)
            else:
                raise RuntimeError(f"Max retries exceeded for {url}")

# Example usage:
# if __name__ == '__main__':
#     data = retry_request('https://api.example.com/data')
#     print(data)