import os
import requests
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup


def extract_tables_to_markdown(url, output_dir="docs"):
    """
    Extracts all tables from a given URL and saves them as markdown files
    in the specified directory.

    Args:
        url (str): The URL of the webpage to extract tables from.
        output_dir (str, optional): The directory to save the markdown files.
                                     Defaults to "docs".

    Returns:
        bool: True if the process was successful, False otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table')

        os.makedirs(output_dir, exist_ok=True)
        output_filepath = os.path.join(output_dir, "tables.markdown")

        with open(output_filepath, 'w', encoding='utf-8') as f:
            for i, table in enumerate(tables):
                heading_text = None
                previous_element = table.find_previous(['h1', 'h2', 'h3', 'caption'])
                if previous_element:
                    heading_text = previous_element.get_text(strip=True)
                elif table.find('caption'):
                    heading_text = table.find('caption').get_text(strip=True)

                if heading_text:
                    f.write(f"## {heading_text}\n")
                else:
                    f.write(f"## Table {i + 1}\n")

                try:
                    df = pd.read_html(StringIO(str(table)))[0]
                    f.write(df.to_markdown(index=False))
                    f.write("\n\n")
                except ValueError:
                    f.write("Error: Could not parse this table into a DataFrame.\n\n")
        print("Done")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
