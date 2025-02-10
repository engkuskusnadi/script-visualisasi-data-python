import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

from google.colab import files
uploaded = files.upload()

movies = pd.read_csv('movies.csv')
print(movies)

genre_drama_filtered = movies[movies['genre'] == 'Drama']
print(genre_drama_filtered)

genre_crime_drama_filtered = movies[movies['genre'] == 'Crime, Drama']
print(genre_crime_drama_filtered)

genre_drama_horror_filtered = movies[movies['genre'] == 'Drama, Horror']
print(genre_drama_horror_filtered)

genre_drama_war_filtered = movies[movies['genre'] == 'Drama, War']
print(genre_drama_war_filtered)

movies_genre = [np.count_nonzero(movies['genre'] == 'Drama'), np.count_nonzero(movies['genre'] == 'Drama, Horror'), np.count_nonzero(movies['genre'] == 'Crime, Drama'), np.count_nonzero(movies['genre'] == 'Drama, War')]
label = ['Drama', 'Horror', 'Crime', 'War']
plt.title('Perbandingan Genre Drama Movie berdasarkan Top 100 IMDB')
plt.pie(movies_genre, labels = label, radius = 1.3, startangle = 60, autopct = '%.1f%%', shadow=True)
plt.show()