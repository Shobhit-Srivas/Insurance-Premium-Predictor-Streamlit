import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

df = pd.read_csv("insurance.csv")

df["sex"] = df["sex"].map({
    "male":0,
    "female":1
})

df["smoker"] = df["smoker"].map({
    "no":0,
    "yes":1
})

df = pd.get_dummies(
    df,
    columns=["region"],
    drop_first=True
)

df["bmi_category_obese"] = (
    df["bmi"] >= 30
).astype(int)

X = df.drop("charges", axis=1)
print("\nFeatures used for training:")
print(X.columns.tolist())
y = df["charges"]

scaler = StandardScaler()

X[["age","bmi","children"]] = scaler.fit_transform(
    X[["age","bmi","children"]]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

joblib.dump(
    model,
    "insurance_model.pkl"
)

joblib.dump(
    scaler,
    "scaler.pkl"
)

print("Model Saved Successfully")