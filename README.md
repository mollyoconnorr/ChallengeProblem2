# Montana City & County Lookup 

An interactive Python program that helps users explore Montana cities,
their counties, and associated license plate prefixes. Users can look up
existing cities or add new ones, which are saved for future use.

------------------------------------------------------------------------

##  Features

-   Look up a Montana city and instantly see its county and license
    plate prefix\
-   Validate user input to prevent invalid city or county names\
-   Add new cities interactively when they are not found\
-   Persist user-added cities across program runs\

------------------------------------------------------------------------

##  How It Works

1.  Loads initial Montana city/county data from a CSV file\
2.  Loads previously added user data from a text file\
3.  Prompts the user to:
    -   Enter a city name
    -   View county and license prefix information
    -   Add missing cities if desired
4.  Saves new entries for future sessions

------------------------------------------------------------------------

## Function Overview

-   `main()` --- Program entry point and user interaction loop
-   `validate_name()` --- Ensures city and county names are valid
-   `lookup_city()` --- Searches for existing city data
-   `handle_unknown_city()` --- Guides users through adding new cities
-   `load_initial_cities()` --- Loads base data from CSV
-   `load_user_cities()` --- Loads user-added cities\
-   `save_new_city()` --- Saves new entries to file

------------------------------------------------------------------------

## How to Run

1.  Make sure you have Python 3 installed\

2.  Clone this repository:

    ``` bash
    git clone https://github.com/mollyoconnorr/ChallengeProblem2.git
    ```

3.  Navigate into the project directory:

    ``` bash
    cd ChallengeProblem2
    ```

4.  Run the program:

    ``` bash
    python Challenge2.py
    ```

------------------------------------------------------------------------

## Data Persistence

User-added cities are stored locally so that new entries remain
available the next time the program runs.

------------------------------------------------------------------------

## Example Output

### IF CITY EXISTS

    Bozeman is in Gallatin County (License Prefix 6)
    Missoula is in Missoula County (License Prefix 4)

### IF CITY DOESN'T EXIST

    Please enter a city name (or 'x' to exit): Four Corners
    Four Corners not found. Would you like to make a new entry for Four Corners? (y/n): y
    Enter the County name for Four Corners: Gallatin

    Please confirm your entry:
    City: Four Corners
    County: Gallatin
    Is this correct? (y/n): y
    Added: Four Corners - Gallatin - Prefix: 6

------------------------------------------------------------------------
