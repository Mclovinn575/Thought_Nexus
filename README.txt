========================================================================
                        _
 _ __   ___   __ _   __| | _ __ ___    ___
| '__| / _ \ / _` | / _` || '_ ` _ \  / _ \
| |   |  __/| (_| || (_| || | | | | ||  __/
|_|    \___| \__,_| \__,_||_| |_| |_| \___|

========================================================================

-- Overview --

This Python script is designed to scrape data from a specified webpage. It retrieves the page title, links, and paragraph text, then saves this information to local CSV files and a text file for further processing.

-- Requirements --

To run this script, it is recommended to use a virtual environment. Make sure to activate your virtual environment and then run the following command from the script's directory to install the necessary packages:
- pip install -r requirements.txt

========================================================================

-- Usage -- 

- Clone this repository to your local machine.
- Navigate to the project directory.
- Activate your virtual environment (if using).
- Run the script:
** python scraper.py **
- When prompted, input the URL of the website you want to scrape.

========================================================================

-- Features --

Scrapes the webpage title, all links, and paragraph texts.
Saves extracted links to site_links/{title}_links.csv.
Saves extracted paragraphs to site_text/{title}.csv.
Saves all paragraph texts to AI_data.txt.
Provides a summary of the collected data using an AI tool (Ollama).

*Notes*
Ensure that you have ollama downloaded on your system. Change the model as needed, for lower powered systems tinyllama is recommended.
Ensure that the directories site_links and site_text exist in the project folder before running the script.
The script will clear the console and output messages regarding the scraping progress.
Troubleshooting
If you encounter issues retrieving the webpage, check your internet connection and ensure that the URL is correct. The script also provides feedback on the HTTP status code for easier debugging.



