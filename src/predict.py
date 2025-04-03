import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import xgboost as xgb
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv('Bicycle_Thefts_Open_Data.csv')


def parse_dates(date_str):
    formats = [
        "%m/%d/%Y %I:%M:%S %p",  # Format 1
        "%d-%m-%Y %H:%M"         # Format 2
    ]
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except ValueError:
            continue
    return pd.NaT


def hour_to_bin(hour):
    if 5 <= hour < 12:
        return 0
    elif 12 <= hour < 17:
        return 1
    elif 17 <= hour < 21:
        return 2
    else:
        return 3


data['OCC_DATE'] = data['OCC_DATE'].apply(parse_dates)
data['hour'] = data['OCC_HOUR']  # Target variable
data['hour_bin'] = data['hour'].apply(hour_to_bin)
data['day_of_week'] = data['OCC_DATE'].dt.dayofweek
data['month'] = data['OCC_DATE'].dt.month
data['is_weekend'] = data['day_of_week'].apply(
    lambda x: 1 if x >= 5 else 0)  # Weekend flag

# Select features for prediction
X = data[['LAT_WGS84', 'LONG_WGS84', 'day_of_week', 'month', 'is_weekend']]
y = data['hour_bin']  # Hour of theft is the target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)


# Random Forest Classifier
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

# Predict the Theft Time for New Data
new_data = pd.DataFrame({
    'LAT_WGS84': [43.70011, 43.65426],
    'LONG_WGS84': [-79.4163, -79.3832],
    'day_of_week': [2, 6],
    'month': [6, 7],
    'is_weekend': [0, 1]
})
new_data['predicted_hour'] = model.predict(new_data)
print("New Data Predictions:")
print(new_data)

y_pred_train = model.predict(X_train)
print("Accuracy Score Random forrest:", accuracy_score(y_train, y_pred_train))


# Gradient Boosting
xgb_model = xgb.XGBClassifier(
    objective='multi:softmax',  # Use 'multi:softmax' for multi-class classification
    num_class=4,
    eval_metric='mlogloss',
    max_depth=6,
    learning_rate=0.1,
    n_estimators=100
)

xgb_model.fit(X_train, y_train)
y_pred_t = xgb_model.predict(X_train)
accuracy = accuracy_score(y_train, y_pred_t)
print(f"Model Accuracy Gradient boosting: {accuracy:.2f}")


nb = GaussianNB()

nb.fit(X_train, y_train)

y_pred_train = nb.predict(X_train)
print("Accuracy Score naive bayes:", accuracy_score(y_train, y_pred_train))

clf = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred_train = clf.predict(X_train)
print("Accuracy Score Decision tree:", accuracy_score(y_train, y_pred_train))
