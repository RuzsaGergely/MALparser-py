# RuzGer's MAL parser (MALparser-py)

## About

This tool has been created for a colleague of mine back in 2020. They fiddled around with the HTML layout, so I needed to rewrite some of the parsing logic, but nothing serious so everything works fine as far as I saw.

This little script can:
- get all anime title in the specified category
- get the episode number of every anime title in the specified category
- filter out anime titles based on the episode number (eg. if you don't want to see animes just above 20 episode minimum, you can do that)

## Using

You need to install the packages specified in the `requirements.txt` file. You can do that by installing manually or by executing the `pip install -r requirements.txt` command.

After that you simply just should start the script. (eg. `py MALparser.py`)

After that you will be guided by the script. The result will be written out as a TXT file in the main folder of the script.

## License
This script is under MIT license. Tinker with it as you wish!