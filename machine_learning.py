import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

df = pd.read_csv('analysis_results.csv')

# Bağımsız (X) ve bağımlı (Y) değişkenleri seçin
X = df[['entropy']]
y = df['encrypted']

# Veriyi eğitim ve test setlerine bölün
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear regression modelini oluşturun ve eğitin
model = LinearRegression()
model.fit(X_train, y_train)

# Eğitim seti üzerinde tahmin yapın
y_train_pred = model.predict(X_train)

# Test seti üzerinde tahmin yapın
y_test_pred = model.predict(X_test)

# Eğitim seti için performans metriklerini değerlendirin
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)

# Test seti için performans metriklerini değerlendirin
mse_test = mean_squared_error(y_test, y_test_pred)
r2_test = r2_score(y_test, y_test_pred)

# Modelin eğitim seti üzerindeki regresyon doğrusunu çizin
plt.scatter(X_train, y_train, color='blue', label='Gerçek Değerler')
plt.plot(X_train, y_train_pred, color='red', linewidth=2, label='Tahmin Edilen Değerler')
plt.title('Linear Regression - Eğitim Seti')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Modelin test seti üzerindeki regresyon doğrusunu çizin
plt.scatter(X_test, y_test, color='blue', label='Gerçek Değerler')
plt.plot(X_test, y_test_pred, color='red', linewidth=2, label='Tahmin Edilen Değerler')
plt.title('Linear Regression - Test Seti')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Performans metriklerini yazdırın
print(f'Eğitim Seti MSE: {mse_train:.2f}')
print(f'Eğitim Seti R^2: {r2_train:.2f}')
print(f'Test Seti MSE: {mse_test:.2f}')
print(f'Test Seti R^2: {r2_test:.2f}')



