# Discord Message Scraper

**_Use at your own risk!_ This is only for educational purposes!**

Allows you to scrape messages from a Discord channel!  
Saves scraped messages to a JSON file, use `process.py` to further process the output file.

## Usage
### Scrape.py
`python scrape.py OUTPUT_FILE_NAME CHANNEL_ID NUM_OF_MESSAGES`  
(note that `OUTPUT_FILE_NAME` does not include a file extention name, will save as JSON)

### Process.py
`python process.py INPUT_FILE_NAME OUTPUT_FILE_NAME`  
(note that neither `INPUT_FILE_NAME` nor `OUTPUT_FILE_NAME` should have file extentions, same as with `scrape.py`)
