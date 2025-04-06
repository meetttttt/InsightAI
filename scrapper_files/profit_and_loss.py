# Get the Profit and Loss from the Screener.in using the url provided.

import requests
import pandas as pd

from bs4 import BeautifulSoup


def load_data_from_screener(url_link: str):
    """
    Scrapes data from screener.in using requests and BeautifulSoup.

    Args:
        url_link (str): The URL of the screener.in page.

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped data, or None if an error occurs.
    """
    try:
        response = requests.get(url_link)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find_all("table")[1]  # Assuming the desired table is the second one

        headers = [th.text.strip() for th in table.find_all("th")]

        data = []
        rows = table.find_all("tr")

        for row in rows:
            cols = row.find_all("td")
            if cols:
                row_data = [col.text.strip() for col in cols]
                data.append(row_data)

        data = pd.DataFrame(data, columns=headers)
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except IndexError:
        print("Table not found or index out of range.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# # Uncomment below to run the code and check output we check.
# # Example usage:
# if __name__ == "__main__":
#     url = "https://www.screener.in/company/RELIANCE/"
#     df = load_data_from_screener(url)
#
#     if df is not None:
#         print(df.to_markdown(index=False))
#     else:
#         print("Failed to retrieve data.")
