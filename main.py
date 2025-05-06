# Task 4: Importing helpers and data
import data
import helpers

# Task 3: Test class definition
class TestUrbanRoutes:

    # Task 4: This setup method checks if the Urban Routes server is online
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Route Server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_cream(self):
        # Add in S8
        print("function created for order 2 ice cream")
        for _ in range(2):# Add in S8
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model")
        pass
