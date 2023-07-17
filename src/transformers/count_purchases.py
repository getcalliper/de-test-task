import pandas as pd

from transformers.coordinates_to_country import coordinates_to_country
from repositories.events_repository import read_events
from repositories.results_repository import save_results


def run_purchase_count_transformer() -> None:
    events_dataframe = read_events()

    events_dataframe['country'] = events_dataframe['coordinates'].apply(coordinates_to_country)

    events_dataframe['created_at'] = pd.to_datetime(events_dataframe['created_at'])
    events_dataframe['date'] = events_dataframe['created_at'].dt.date

    events_dataframe = events_dataframe[events_dataframe['event_type'] == 'purchase']

    results = events_dataframe.groupby(['country', 'device_type', 'date']).size().reset_index(name='purchases')

    save_results(results)
