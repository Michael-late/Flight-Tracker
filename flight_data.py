import pandas as pd
import ast
from flight_search import FlightSearch, some
from data_manager import DataManager

class FlightData:
    """This class is responsible for structuring the flight data into a clean DataFrame."""
    def __init__(self, flight: FlightSearch):
        # Make pandas show full content
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 0)
        pd.set_option('display.max_colwidth', None)

        self.flight_search = flight
        self.data = self.flight_search.get_deal()

        # Build DataFrame from raw API results
        df = pd.DataFrame.from_dict(self.data)

        # Expand itineraries into flat list of segments
        segments_expanded = df['itineraries'].apply(
            lambda flights: [seg for offer in flights for seg in offer['segments']]
        )
        segments_df = pd.DataFrame([
            seg for all_segs in segments_expanded for seg in all_segs
        ])

        # Helper function to safely extract date from dict or string
        def extract_date(value):
            if isinstance(value, dict):
                return value['at'].split('T')[0]
            else:
                val = ast.literal_eval(value)
                return val['at'].split('T')[0]

        # Add separate columns for departure/arrival dates only (YYYY-MM-DD)
        segments_df['departure_date'] = segments_df['departure'].apply(extract_date)
        segments_df['arrival_date'] = segments_df['arrival'].apply(extract_date)

        # Store cleaned DataFrame as instance variable
        self.segments_df = segments_df

        # Print everything (optional)
        print(self.segments_df)


# Usage example
q = some()
a = FlightSearch(q)
z = FlightData(a)
