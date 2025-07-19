 import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)
    return df
