# Get quarterly result of the company based on the url provided.

import pandas as pd
from bs4 import BeautifulSoup
import requests


def extract_table_from_url(url):
    """
    Extracts the table from the given URL and returns it as a pandas DataFrame.

    Args:
        url (str): The URL of the webpage containing the table.

    Returns:
        pandas.DataFrame: The extracted table as a DataFrame, or None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table')

        if table is None:
            return None  # Return None if no table is found

        data = []
        headers = []

        for i, row in enumerate(table.find_all('tr')):
            cols = row.find_all(['td', 'th'])
            cols = [ele.text.strip() for ele in cols]
            if i == 0:
                headers = cols
            else:
                data.append(cols)

        df = pd.DataFrame(data, columns=headers)
        df = df.iloc[:-1, :]  #Remove last row (Raw PDF)
        df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x.str.replace(',', '').str.replace('%', ''))

        return df

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# # Uncomment below to run the code and check output we check.
# # Example usage:
# Example usage
# url = "https://www.screener.in/company/RELIANCE/"
# df = extract_table_from_url(url)
#
# if df is not None:
#     print(df.to_markdown(index=False))
# else:
#     print("Failed to extract table.")
