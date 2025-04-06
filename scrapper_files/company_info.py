# Get the Metric and Value and Company info based on the url passed

import requests
import pandas as pd

from bs4 import BeautifulSoup


def format_dataframe(df):

    df_transposed = df.T.reset_index()
    df_transposed.columns = ['Metric', 'Value']
    return df_transposed


def extract_company_name(soup):
    company_name_tag = soup.find('h1', class_='company-name')
    if company_name_tag:
        return company_name_tag.text.strip()
    else:
        company_name_tag = soup.find('h1', class_='margin-0')
        return company_name_tag.text.strip() if company_name_tag else "N/A"


def extract_value(soup, label):
    try:
        label_tag = soup.find(string=lambda text: text and label in text)

        if label_tag:
            parent = label_tag.parent
            value_tag = parent.find_next(class_='number')
            if value_tag:
                return value_tag.text.strip()

        return "N/A"

    except Exception as e:
        print(f"Error while extracting values for {label} : {e}")
        return "N/A"


def scrape_screener(url: str):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        try:
            company_name = extract_company_name(soup)

            data = {
                'Company Name': company_name,
                'Market Cap': extract_value(soup, 'Market Cap'),
                'Current Price': extract_value(soup, 'Current Price'),
                'High / Low': extract_value(soup, 'High / Low'),
                'Stock P/E': extract_value(soup, 'Stock P/E'),
                'Book Value': extract_value(soup, 'Book Value'),
                'Dividend Yield': extract_value(soup, 'Dividend Yield'),
                'ROCE': extract_value(soup, 'ROCE'),
                'ROE': extract_value(soup, 'ROE'),
                'Face Value': extract_value(soup, 'Face Value'),
            }

            df = pd.DataFrame([data])
            return df

        except Exception as e:
            print(f"Error occurred while parsing the HTML: {e}")
            return None
    else:
        print(f"Failed to retrieve data. Status COde: {response.status_code}")
        return None


# # Uncomment below to run the code and check output we check.
# # Example usage:
# url = 'https://www.screener.in/company/OLAELEC/'
# df = scrape_screener(url)
# df = format_dataframe(df)
# print(df.to_markdown(index=False))
