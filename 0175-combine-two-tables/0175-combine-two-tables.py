import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    final = person.merge(address, on = 'personId', how = 'left')
    return final[['firstName', 'lastName', 'city', 'state']]    