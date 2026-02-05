"""
Montana Counties License Plate Lookup
Author: Molly O'Connor
Date: 1/22/2026
Description:
    This program allows users to look up Montana counties based on the city name.
    Users can see the county and license plate prefix, and add new cities if unknown.
"""

import csv

CITY_FILE = "NewCities.txt"  # Persistent file storing user-added cities (city, county, license prefix)
CSV_FILE = "MontanaCounties.csv"  # Original Montana county data (county, county seat, license prefix)

def load_initial_cities(csv_file):
    """
    Load the base Montana county data from CSV file and store as a dictionary.

    Args:
        csv_file (str): Path to the CSV file containing initial county data.
                        Expected columns: 'city', 'county', 'prefix'.

    Returns:
        dict: A dictionary where:
            - key: city name (lowercased for consistent lookup)
            - value: tuple of (county name, license plate prefix)
    """
    cities = {}
    with open(csv_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city = row["city"].strip().lower() # normalize name for dict keys
            county = row["county"].strip()
            prefix = int(row["prefix"])
            cities[city] = (county, prefix) # key = city
    return cities

# -------------------------
# Load additional cities from persistent file
# -------------------------
def load_user_cities(file_path, cities):
    """
    Load user-added city data from a text file into the cities dictionary.

    Persistent data store containing cities added by the user in previous program runs.

    Args:
        file_path (str): Path to the text file storing user-added cities.
                         Expected format per line:
                         city,county,prefix
        cities (dict): Dictionary to update with user-added city data.
                       Format:
                       { city_name (str) : (county_name (str), prefix (int or str)) }
    """
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # skip empty lines

            parts = line.split(",")

            city = parts[0].strip().lower()
            county = parts[1].strip()
            prefix = parts[2].strip() if len(parts) > 2 else "unknown" # adds a prefix for each entry if it doesn't exist

            cities[city] = (county, prefix)

def save_new_city(city_name, county_name, prefix):
    """
    Save a newly added city to the persistent user data file.
    Appends a new city entry to the text file so the information is preserved between program runs.

    Args:
        city_name (str): Name of the city (expected to be lowercase).
        county_name (str): Name of the county the city belongs to.
        prefix (int or str): License plate prefix for the county,
                             or 'unknown' if not available.
    """
    # Open, write, and immediately close the file to prevent data corruption
    with open(CITY_FILE, "a") as file:
        file.write(f"{city_name},{county_name},{prefix}\n")

def validate_name(name):
    """
    Validate user input for city or county names.

    Args:
        name (str): The city or county name entered by the user.

    Returns:
        bool: True if the name is valid, False otherwise.
    """
    if not name:
        print("Invalid input. Please enter a valid name.")
        return False
    elif not name.replace(" ", "").isalpha():
        print("Name should only contain letters.")
        return False
    return True

def lookup_city(city_name, cities):
    """
    Look up a city in the cities dictionary and display its county information.

    Args:
        city_name (str): Name of the city entered by the user.
        cities (dict): Dictionary containing city data in the format:
                       { city_name (str) : (county_name (str), prefix) }

    Returns:
        bool: True if the city is found and displayed, False otherwise.
    """
    city_name_lower = city_name.lower() # lowercase for normalized dictionary lookup
    if city_name_lower in cities:
        county, prefix = cities[city_name_lower]
        print(f"{city_name.title()} is in {county} County (License Prefix {prefix})")
        return True
    return False

def unknown_city(city_name, cities):
    """
    Handle the case where a city is not found in the cities dictionary.
    Gives the user the option to add a new city entry.
    If the user chooses to add the city, they are prompted for the
    county name, the entry is validated, and the user is asked to
    confirm the information before it is saved.

    Fun addition!
    If the county already exists in the dataset, the corresponding
    license plate prefix is reused. Otherwise, the prefix is stored
    as 'unknown'.

    Args:
        city_name (str): Name of the city entered by the user.
        cities (dict): Dictionary containing known cities in the format:
                       { city_name (str) : (county_name (str), prefix) }

    Returns:
        None
    """
    while True:
        user_input = input(
            f"{city_name.title()} not found. Would you like to make a new entry for {city_name.title()}? (y/n): ").lower()
        if user_input not in ("y", "n"):
            print("Invalid input. Please type 'y' or 'n'.")
            continue
        elif user_input == "n":
            break
        elif user_input == "y":
            county_name = input(f"Enter the County name for {city_name.title()}: ").strip().title()
            if not validate_name(county_name):
                continue

            # Determine prefix if the county already exists
            existing_prefix = None
            for county, prefix in cities.values():
                if county.lower() == county_name.lower():
                    existing_prefix = prefix
                    break
            prefix_to_use = existing_prefix if existing_prefix is not None else "unknown"

            # Ask the user to confirm the new entry before saving
            while True:
                print("\nPlease confirm your entry:")
                print(f"City: {city_name.title()}")
                print(f"County: {county_name}")
                confirm = input("Is this correct? (y/n): ").lower()

                if confirm not in ("y", "n"):
                    print("Invalid input. Please type 'y' or 'n'.")
                    continue
                elif confirm == "n":
                    print("Let's try again.")
                    break  # Re-enter county name
                elif confirm == "y":
                    # Update dictionary and file
                    cities[city_name.lower()] = (county_name, prefix_to_use)
                    # Persist the new city entry to disk
                    save_new_city(city_name.lower(), county_name, prefix_to_use)
                    print(f"Added: {city_name.title()} - {county_name} - Prefix: {prefix_to_use}\n")
                    return


def main():
    """
    Main loop for Montana city and county lookup.

    Initializes the program by loading the data stores.
    Provides a short introduction.
    Creates interactive loop that allows users to:
    - Look up a city to find its county and license plate prefix
    - Add new cities if they are not already known
    - Exit the program when finished
    """
    # Load initial files
    cities = load_initial_cities(CSV_FILE)
    load_user_cities(CITY_FILE, cities)

    # Intro
    print("Do you want to learn about your Montana Counties?")
    print("Sounds like SOOO much fun... right?")

    still_playing = input("Ready to play? (y/n): ").lower()
    if still_playing != "y":
        print("Okay, goodbye!")
        return

    # Main interaction loop
    while True:
        city_name = input("Please enter a city name (or 'x' to exit): ").strip()
        if city_name.lower() == "x":
            break
        if not validate_name(city_name):
            continue
        if not lookup_city(city_name, cities):
            unknown_city(city_name, cities)

    print("Thanks! Have a good day.")

# Run the program
if __name__ == "__main__":
    main()
