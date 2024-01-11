import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("analysis_results.csv")
# Etiketleri sayısallaştırma (Sifreli: 1, Sifresiz: 0)
df['encrypted'] = df['encrypted'].map({'Sifreli': True, 'Sifresiz': False})



# Eğitim ve test setlerini oluşturun
X = df[['entropy', 'sha1','sha256','md5']]
y = df['encrypted']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli eğit
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test setini kullanarak modelin doğruluğunu değerlendirin
tahminler = model.predict(X_test)
dogruluk = accuracy_score(y_test, tahminler)
print("Model doğruluğu:", dogruluk)

# Gerçek dosyalar için tahminler yapın
df['tahmini_sifreli_durum'] = model.predict(df[['entropy', 'sha1','sha256','md5']])

# Sonuçları yazdır
print(df[['dosya_yolu', 'encrypted', 'tahmini_sifreli_durum']])
