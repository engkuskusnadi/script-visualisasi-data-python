# Analisis Genre Film

Script ini melakukan analisis data film dengan fokus pada genre "Drama" dan sub-genernya, menggunakan library Pandas dan Seaborn untuk manipulasi data dan visualisasi.

## Persyaratan

Pastikan Anda telah menginstal library berikut:
- `matplotlib`
- `pandas`
- `seaborn`
- `numpy`
- Google Colab (jika menggunakan fitur unggah file)

Untuk menginstal library yang diperlukan, gunakan perintah berikut:

```sh
pip install matplotlib pandas seaborn numpy
```
## Cara Memulai

### Unggah Dataset

Script ini menggunakan fungsi unggah file dari Google Colab untuk mengunggah file CSV bernama movies.csv. Pastikan file ini sesuai format dan memiliki kolom bernama **genre**.

### Penjelasan Script

#### Import Library

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from google.colab import files
```
Unggah File
```python
uploaded = files.upload()
```
Membaca Data
```python
df = pd.read_csv('movies.csv')
```
Filter Genre
```python
genres_of_interest = ["Drama", "Crime, Drama", "Drama, Horror", "Drama, War"]
filtered_df = df[df['genre'].isin(genres_of_interest)]
```
Menghitung Jumlah Genre
```python
genre_counts = filtered_df['genre'].value_counts()
```
Visualisasi
```python
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")
plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Perbandingan Genre Drama Movie berdasarkan Top 100 IMDB')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.show()
```
Cara Menggunakan
Buka Google Colab dan salin script ke dalam sel kode.
Jalankan sel untuk mengeksekusi prompt unggah file.
Pilih dan unggah file movies.csv Anda.
Script akan menampilkan DataFrame yang telah difilter dan diagram lingkaran perbandingan jumlah genre.
Contoh Output
Menjalankan script akan menampilkan DataFrame yang difilter untuk setiap genre dan sebuah diagram lingkaran dengan judul:
```python
Perbandingan Genre Drama Movie berdasarkan Top 100 IMDB
```
Catatan
Pastikan file CSV Anda berisi data yang relevan dengan kolom berjudul genre agar script dapat berjalan dengan baik.
