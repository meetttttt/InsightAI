# This will extract the balance sheet of the company based on the url provided.

import requests
import pandas as pd

from bs4 import BeautifulSoup


def extract_balance_sheet_from_url(url):
    """
    Extracts the balance sheet table from a given URL and returns it as a pandas DataFrame.

    Args:
        url (str): The URL of the webpage containing the balance sheet.

    Returns:
        pandas.DataFrame or None: The balance sheet DataFrame, or None if extraction fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')

        def extract_table_to_df(table_id):
            div = soup.find('section', id=table_id)
            if div:
                table = div.find('table')
                if table:
                    data = []
                    header = []

                    for i, row in enumerate(table.find_all('tr')):
                        cols = row.find_all('td')
                        if i == 0:
                            header_row = row.find_all('th')
                            header = [th.text.strip() for th in header_row]
                        else:
                            cols = [ele.text.strip().replace(',', '') for ele in cols]
                            data.append(cols)

                    return pd.DataFrame(data, columns=header)
                else:
                    print(f"Table not found inside section with id '{table_id}'")
                    return None
            else:
                print(f"Section with id '{table_id}' not found.")
                return None

        df_balance_sheet = extract_table_to_df('balance-sheet')
        return df_balance_sheet

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Uncomment below to run the code and check output we check.
# Example usage:
# url = "https://www.screener.in/company/RELIANCE/"
# df = extract_balance_sheet_from_url(url)
#
# if df is not None:
#     print("Balance Sheet:")
#     print(df.to_markdown(index=False))
