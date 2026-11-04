import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_model():

    data = pd.read_csv("sample_data.csv")

    features = [
        "account_age_months",
        "connections",
        "profile_completeness",
        "skills_count",
        "experience_years",
        "about_word_count"
    ]

    X = data[features]
    y = data["label"]

    model = DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    )

    model.fit(X, y)

    return model, features