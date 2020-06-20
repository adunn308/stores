# Store Locations

## To Run
From main folder:

    >> pip install -r requirements.txt
    >> python src/app.py

App should run on localhost:5000
Once the app is running, load the json data into the database by going to https://localhost:5000/load_data.
Once this has been completed. The list of stores can be viewed at: http://localhost:5000/stores
The endpoint to see stores within a certain radius can be found at:

    https://localhost:5000/check_stores/{`postcode}/{distance in m}

eg. [http://localhost:5000/check_stores/TW9 1BN/5000](http://localhost:5000/check_stores/TW9%201BN/5000) for stores within 5km of the postcode TW9 1BN

## Running Tests

Tests are implemented using nosetests. Simply run 'nosetests' to run the tests.

    >> nosetests

## Shortcuts and Improvements Needed
- Tests load a new database for each test, although this is encouraged in the documentation, it is not a scalable solution
- I made an assumption that if the postcode could not be found in the current or expired postcodes on postcodes.io that it would not be added to the db and therefore will not appear in the list of stores. This could be changed depending on how the end product was used.
- I chose to use a postgis extension as this would give the quickest results when searching by radius. Although this is an extra step/add on, I think the time it will save is worth it.
- The error messaging is very basic, this needs to be expanded to give more useful messages to the user.
- My script does not update if the data is changed. It will only create new entries for new names/postcodes.
