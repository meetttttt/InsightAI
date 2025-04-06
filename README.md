#InsightAI
This project is a web application that allows users to extract tables from Screener.in, view the extracted data in Markdown format, and optionally analyze the data using Google Gemini AI.

## Features

* **Extract Tables from URL:** Users can input a screener.in URL, and the application will attempt to find and extract all HTML tables from that page.
* **View Extracted Markdown:** The extracted table data is displayed in the user interface in Markdown format, making it easy to read and understand.
* **AI-Powered Analysis (via Google Gemini):** Users can choose to analyze the extracted table data using Google Gemini. The AI will provide a summary of key insights, trends, and notable observations.
* **Download Markdown:** Users can download the extracted table data as a `.md` (Markdown) file.
* **Pleasant User Interface:** The application features a clean and user-friendly interface built with basic HTML and CSS.

# Application View
- Initial View:
![image](https://github.com/user-attachments/assets/dd93e8ff-09f3-47d0-938f-08a0e51277be)

- Extract Markdown:
![image](https://github.com/user-attachments/assets/9fc19e44-867d-4ef0-b030-6896f45fd5f5)

- Analyse Report:
![image](https://github.com/user-attachments/assets/60d924bb-0b9f-4af8-90e4-e54b9cdb78a7)


## Prerequisites

Before running the project, ensure you have the following:
* **Google Gemini API Key:** You will need a Google Gemini API key to use the AI analysis feature. You can obtain one from the Google AI Studio.

## Setup and Installation

1.  **Clone the repository** (if you have the code in a repository):
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install Flask pandas requests beautifulsoup4 google-generativeai
    ```

3.  **Set the Google Gemini API Key:**
    You need to set your Gemini API key as an environment variable. Replace `YOUR_ACTUAL_GEMINI_API_KEY` with your key:
    ```bash
    export GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
    ```
    (On Windows, use `set GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"`)

## Running the Application

1.  Navigate to the project directory in your terminal.
2.  Run the Flask application:
    ```bash
    python app.py
    ```
3.  Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1.  **Enter URL:** In the provided input field, enter the URL of the webpage from which you want to extract tables.
2.  **Choose Action:**
    * **Extract to Markdown:** Click this button to extract the tables and display them in Markdown format on the page. A download link for the Markdown file will also be provided.
    * **Analyze Report:** Click this button to extract the tables, send the Markdown data to Google Gemini for analysis, and display the streamed analysis results on the page. The raw Markdown will not be displayed when this option is chosen.
3.  **View Results:** The extracted Markdown or the AI-generated analysis will be shown in the respective sections on the page.
4.  **Download (Markdown Only):** If you chose "Extract to Markdown", you can click the "Download Markdown File" link to save the extracted data as a `.md` file.

## Project Structure

```
your_project/
├── app.py             # Main Flask application file
├── utils/
│   ├── ETS.py         # Utility for extracting tables to Markdown
│   └── utils_gemini.py # Utility for analyzing Markdown with Gemini
├── templates/
│   └── index.html   # HTML template for the user interface
├── docs/              # Directory for temporary storage (e.g., Markdown files)
└── README.md          # This file
```


## Notes

* The accuracy of table extraction depends on the structure and complexity of the HTML on the target webpage.
* The quality of the AI analysis depends on the content of the tables and the capabilities of the Gemini model.
* The `docs` directory is used for temporary storage of the extracted Markdown files during the analysis process. It is cleaned up after the analysis is complete.

## Further Enhancements

* Implement more robust error handling for website fetching and table parsing.
* Allow users to customize the Gemini analysis prompt.
* Add support for extracting tables in other formats (e.g., CSV).
* Improve the UI with a more advanced CSS framework.
* Implement client-side validation of the URL.
* Add progress indicators for the extraction and analysis processes.

## Author
Meet Nagadia
