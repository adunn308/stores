from src.test.test_setup import ProjectTests
from src.get_stores import GetStores


class TestStores(ProjectTests):

    def test_list_stores(self):
        get_stores = GetStores()
        response = get_stores.list_stores()

        # check all data points listed
        self.assertEquals(len(response), 6)

        # check first one is "Edinburgh Castle" and last one is St Ives (alphabetically)
        self.assertEquals(response[0].name, "Edinburgh Castle")
        self.assertEquals(response[-1].name, "St Ives")

        # check the long lat has been fetched, and is correct (based on postcodes.io)
        self.assertEquals(response[0].longitude, -3.201478)
        self.assertEquals(response[0].latitude, 55.948965)
        self.assertEquals(response[1].name, "Greenwich")
        self.assertEquals(response[1].longitude, -0.000874)
        self.assertEquals(response[1].latitude, 51.477346)

    def test_radius_picks_correct_values(self):
        get_stores = GetStores()

        # using postcode of Edinburgh National Gallery, under 1000m away from Edinburgh castle (only one returned)
        response = get_stores.find_stores('EH2 2EL', 1000)
        self.assertEquals(len(response[0]), 1)
        self.assertEquals(response[0][0].name, "Edinburgh Castle")

        # same postcode with 5000m should give 2 results, with Leith first (as the more northern)
        response = get_stores.find_stores('EH2 2EL', 5000)
        self.assertEquals(len(response[0]), 2)
        self.assertEquals(response[0][0].name, "Leith")

        # same postcode with 640000 should now include the London results in order of north to south
        response = get_stores.find_stores('EH2 2EL', 650000)
        self.assertEquals(len(response[0]), 4)
        self.assertEquals(response[0][0].name, "Leith")
        self.assertEquals(response[0][1].name, "Edinburgh Castle")
        self.assertEquals(response[0][2].name, "London Zoo")
        self.assertEquals(response[0][-1].name, "Greenwich")

    def test_bad_postcode(self):
        get_stores = GetStores()
        # test that function does not crash if bad postcode is used, and error message is returned
        response = get_stores.find_stores('ABC', 1000)
        self.assertEquals(response[1],
                          "Could not find details on this postcode, please check it is valid or try again later")
