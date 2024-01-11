import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Veri setini yükleyin
dataset_path = "analysis_results.csv"  # Veri seti dosya yolunu güncelleyin
df = pd.read_csv(dataset_path)

# Bağımsız değişkenler (X) ve hedef değişkeni (y) belirleyin
X = df[['entropy']]  # Gerekirse diğer özellikleri de ekleyin
y = df['encrypted']

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Sınıflandırma modelini oluşturun (Random Forest kullanıldı, başka modeller de tercih edilebilir)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Test setini kullanarak modelin performansını değerlendirin
y_pred = model.predict(X_test)

# Doğruluk ve sınıflandırma raporu yazdırın
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy}")
print("Classification Report:")
print(classification_report(y_test, y_pred))
