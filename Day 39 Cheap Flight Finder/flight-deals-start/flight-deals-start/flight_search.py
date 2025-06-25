class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, data):
        self.sheet_data = data

    def get_destination(self):
        for item in self.sheet_data:
            item["iataCode"] = "TESTING"
