import sys
sys.path.append("src")

from preprocess import load_and_clean, prepare_data


def test_no_missing_values():
    df = load_and_clean("data/raw/insurance.csv")
    assert df['age'].isnull().sum() == 0
    assert df['bmi'].isnull().sum() == 0
    print("✅ No missing values after cleaning")


def test_correct_shape():
    df = load_and_clean("data/raw/insurance.csv")
    assert df.shape[0] == 15000
    assert df.shape[1] == 13
    print("✅ Dataset shape is correct")


def test_model_output():
    import joblib
    import pandas as pd

    model = joblib.load("src/model.pkl")
    X, y = prepare_data("data/raw/insurance.csv")
    prediction = model.predict(X[:1])

    assert len(prediction) == 1
    assert prediction[0] > 0
    print("✅ Model returns a valid prediction")


if __name__ == "__main__":
    test_no_missing_values()
    test_correct_shape()
    test_model_output()
    print("\n All tests passed!")