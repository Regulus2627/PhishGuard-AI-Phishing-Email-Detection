import pandas as pd
import pickle
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/phishing.csv")

# Select features
binary_cols = ['Contains_Link', 'Contains_Attachment', 'Urgent_Words', 'From_Trusted_Domain']

# Convert Yes/No → 1/0
for col in binary_cols:
    df[col] = df[col].map({'Yes': 1, 'No': 0})

# Encode labels
le = LabelEncoder()
df['Label_Encoded'] = le.fit_transform(df['Label'])

# Split data
X = df[binary_cols]
y = df['Label_Encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = BernoulliNB()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred) * 100)

# Save model
pickle.dump(model, open("model/model.pkl", "wb"))
pickle.dump(le, open("model/label_encoder.pkl", "wb"))

print("Model saved successfully!")