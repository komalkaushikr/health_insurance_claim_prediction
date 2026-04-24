import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_and_clean(filepath):
    """Load raw data and fix missing values."""
    df = pd.read_csv(filepath)
    df['age'].fillna(df['age'].median(), inplace=True)
    df['bmi'].fillna(df['bmi'].median(), inplace=True)
    return df


def encode_features(df):
    """Convert text columns to numbers."""
    le = LabelEncoder()
    text_columns = ['sex', 'hereditary_diseases', 'city', 'job_title']
    for col in text_columns:
        df[col] = le.fit_transform(df[col])
    return df


def prepare_data(filepath):
    """Full pipeline — load, clean, encode."""
    df = load_and_clean(filepath)
    df = encode_features(df)
    X = df.drop('claim', axis=1)
    y = df['claim']
    return X, y