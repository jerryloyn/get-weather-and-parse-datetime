# Get Weather Info and Parse Datetime to ISO8601 Date

There are two py files for 
- get weather info (current temperature or next 3 days forecast) from HKO
- parse the datetime string into a ISO8601 formatted date
## Installation
1. Clone the repository
2. Go to repo folder
``` command
cd weather-time-conversion
```
3. Create a virtualenv and activate it (you have to install Python3 first)
``` command
python3 -m venv venv
. venv/bin/activate
```
Or on Windows cmd
``` command
    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat
```
4. Install libraries
``` command
pip install -r requirements.txt
```
5. Run the code
``` command
python weather.py
python time_conversion.py
```
