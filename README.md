# Store Locations

## To Run
From main folder:

    >> pip install -r requirements.txt
    >> export FLASK_ENV=DEV
    >> python run.py

App should run on localhost:5000
Once the app is running, load the json data into the database by going to https://localhost:5000/load_data.
Once this has been completed. The list of stores can be viewed at: http://localhost:5000/stores
The endpoint to see stores within a certain radius can be found at:

    https://localhost:5000/check_stores/{`postcode}/{distance in m}

eg. [http://localhost:5000/check_stores/TW9 1BN/5000](http://localhost:5000/check_stores/TW9%201BN/5000) for stores within 5km of the postcode TW9 1BN

## Running Tests

Tests are implemented using nosetests. In order to use the test database rather than the real one, please export the FLASK_ENV=TEST before running nosetests.

    >> export FLASK_ENV=TEST
    >> nosetests

## Shortcuts and Assumptions
- I made an assumption that if the postcode could not be found in the current or expired postcodes on postcodes.io that it would not be added to the db and therefore will not appear in the list of stores. This could be changed depending on how the end product was used.
- I chose to use a postgis extension as this would give the quickest results when searching by radius. Although this is an extra step/add on, I think the time it will save is worth it.


## Questions:
#### - i) Which test did you complete? (backend or full-stack)
- backend

#### - ii) If you had chosen to spend more time on this test, what would you have done differently?
- The error messaging is very basic, this needs to be expanded to give more useful messages to the user.
- My script does not update if the data is changed. It will only create new entries for new names/postcodes.
- My tests are using the postcodes.io endpoint. If I had more time I would have faked a response for my records so that they are not reliant on a third party
- I'd add more error handling and retries if accessing the postcodes api failed.
- I'd look into other ways of using the testing env variable.
- Possibly looking into improving the application setup using factories (although this felt like it would be overkill for an app of it's current size)
- Postcode validation on user input, instead of the generic error message. Written in the app to avoid another external request.
- Adding a logger rather than simply using print statements.
- In the tests, I'm loading all the data in the setup rather than for each set of tests. This is simply because I'm using the same dataset and could be easily changed if other sets were added.

#### - iii) What part did you find the hardest? What part are you most proud of? In both cases, why?
- The hardest part of the test was deciding on a structure for the app. Flask is great because it's so open with what you can do, but this also is a challenge as there are always too many ways to do things.
- I am most proud of the postgis integration. I'd not worked with it before and I think it's ideally suited to the job. I was pleased with how quickly I picked it up and made it work.

#### - iv) What is one thing we could do to improve this test?
- Generally, I found the instructions clear. I'd like to have more of an idea of which areas matter more than others, therefore where to put my main focus.