import os
from file_object import FileClass
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

data = r"C:\Users\ayseg\OneDrive\Masaüstü\CYBER_DOSYA"
file_paths = [os.path.join(data, file) for file in os.listdir(data)]
labels = [1 if "malicious" in file.lower() else 0 for file in file_paths]

files = [FileClass(file_path, label) for file_path, label in zip(file_paths, labels)]

# Extract features from FileClass instances
features = ["entropy", "signature", "file_sha1", "file_sha256", "file_md5"]
X = [[getattr(file, feature) for feature in features] for file in files]
y = [file.label for file in files]

# Identify categorical feature indices
categorical_feature_indices = [1, 2, 3, 4]  # Adjust these indices based on the actual positions of your string features

# Use ColumnTransformer for preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_feature_indices)
    ],
    remainder='passthrough'
)

# Fit and transform the data
X_processed = preprocessor.fit_transform(X)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=25)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
