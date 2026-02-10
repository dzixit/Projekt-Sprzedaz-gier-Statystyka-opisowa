#%%
import kagglehub
import skew
from kagglehub import KaggleDatasetAdapter
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#%%
projectData = pd.read_csv(r'C:\Users\barto\PycharmProjects\Statystyka\Video_Games_Sales_as_at_22_Dec_2016.csv')
#%%
projectData.info()
#%%
projectData.head()
#%%
selected_columns=['Name', 'Platform', 'Publisher', 'Global_Sales', 'Critic_Score', 'User_Score','Year_of_Release']
projectData_selected=projectData[selected_columns]
projectData_cleaned=projectData_selected.dropna()
projectData_cleaned.head()


#%% md
# Okreslony typ zmiennej i typ skali pomiarowej dla wybranych kolumn
# 
# 1.Platform
# 
# Typ zmiennej:Zmienna jakościowa
# 
# Skala pomiarowa: Skala nominalna
# 
# 2.Publisher
# Typ zmiennej: Zmienna jakościowa
# 
# Skala pomiarowa: Skala nominalna
# 
# 3.Global_Sales
# Typ zmiennej: Zmienna ilościowa
# 
# Skala pomiarowa: Skala ilorazowa
# 
# 4.Critic_Score
# Typ zmiennej: Zmienna ilościowa
# 
#  pomiarowa: Skala przedziałowa
#%%
selected_columns = ['Name', 'Platform', 'User_Score', 'Year_of_Release']
projectData_cleaned = projectData[selected_columns].dropna()
projectData_cleaned['User_Score'] = pd.to_numeric(projectData_cleaned['User_Score'], errors='coerce')

# Histogram dla zmiennej ilościowej
plt.figure(figsize=(10, 5))
sns.histplot(data=projectData_cleaned, x='User_Score', bins=20, kde=True, color='teal')
plt.title('Rozkład zmiennej User_Score', fontsize=16)
plt.xlabel('User Score', fontsize=12)
plt.ylabel('Liczba gier', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Wykres słupkowy dla zmiennej jakościowej
plt.figure(figsize=(10, 5))
platform_counts = projectData_cleaned['Platform'].value_counts()
sns.barplot(x=platform_counts.index, y=platform_counts.values, palette='mako')
plt.title('Liczba gier na różnych platformach', fontsize=16)
plt.xlabel('Platforma', fontsize=12)
plt.ylabel('Liczba gier', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#%%
platform_counts = projectData_cleaned['Platform'].value_counts()
top_5_platforms = platform_counts[:5]
other_count = platform_counts[5:].sum()

# Preparing data for the pie chart
platform_pie_labels = list(top_5_platforms.index) + ['Other']
platform_pie_sizes = list(top_5_platforms.values) + [other_count]

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    platform_pie_sizes,
    labels=platform_pie_labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel')[0:6]
)
plt.title('Distribution of Top 5 Platforms and Other Categories', fontsize=14)
plt.show()

#%%

#%%
# Określenie przedziałów dla grupowania User_Score
bins = [0, 2, 4, 6, 8, 10]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10']
projectData_cleaned['User_Score_Group'] = pd.cut(projectData_cleaned['User_Score'], bins=bins, labels=labels,
                                                 include_lowest=True)

# Liczba obserwacji w każdej grupie
grouped_data = projectData_cleaned['User_Score_Group'].value_counts().sort_index()

# Wyświetlenie szeregu statystycznego
print("Rozkład częstości w grupach User_Score:")
print(grouped_data)

# Wizualizacja szeregu grupowego
plt.figure(figsize=(10, 5))
grouped_data.plot(kind='bar', color='skyblue')
plt.title('Rozkład gier w grupach User_Score', fontsize=16)
plt.xlabel('Grupy User_Score', fontsize=12)
plt.ylabel('Liczba gier', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#%%
columns = ['Global_Sales', 'Critic_Score', 'User_Score']
projectData_cleaned = projectData[columns].dropna()

# Zamiana 'User_Score' na typ numeryczny
projectData_cleaned['User_Score'] = pd.to_numeric(projectData_cleaned['User_Score'], errors='coerce')

# Obliczenie miar za pomocą funkcji wbudowanych
summary = pd.DataFrame({
    'Średnia': projectData_cleaned.mean(),  # Średnia
    'Mediana': projectData_cleaned.median(),  # Mediana
    'Dominanta': projectData_cleaned.mode().iloc[0],  # Dominanta
    'Wariancja': projectData_cleaned.var(),  # Wariancja
    'Odchylenie standardowe': projectData_cleaned.std(),  # Odchylenie standardowe
    'Rozstęp': projectData_cleaned.max() - projectData_cleaned.min(),  # Rozstęp
    'Odchylenie ćwiartkowe': projectData_cleaned.quantile(0.75) - projectData_cleaned.quantile(0.25),  # IQR
    'Współczynnik zmienności (%)': (projectData_cleaned.std() / projectData_cleaned.mean()) * 100  # CV
})

# Dodatkowo uwzględnienie kwartyli
quartiles = projectData_cleaned.quantile([0.25, 0.5, 0.75]).T
quartiles.columns = ['Q1 (25%)', 'Q2 (Mediana)', 'Q3 (75%)']

# Łączenie wyników w jedną tabelę
final_summary = pd.concat([summary, quartiles], axis=1)

# Wyświetlenie wyników
print("Miary centralne i miary rozrzutu dla analizowanych zmiennych:")
print(final_summary)

#%% md
#  Wnioski z otrzymanych danych:
# 1. Global_Sales (globalna sprzedaż):
#     - Średnia sprzedaż wynosi około 0.69 mln sztuk, ale mediana to 0.25, co wskazuje, że większość gier osiąga znacznie niższe wyniki sprzedaży niż sugeruje średnia.
#     - Dominanta to 0.02 mln sztuk, co oznacza, że najczęściej sprzedawana liczba kopii to bardzo niskie wartości sprzedaży.
#     - Rozstęp wynoszący 82.52 mln sztuk oraz współczynnik zmienności na poziomie 263.59% wskazują na bardzo duże zróżnicowanie wyników sprzedażowych wśród gier.
#     - Odchylenie ćwiartkowe na poziomie 0.55 pokazuje, że 50% centralnych wyników (między Q1 a Q3) ma mniejsza zmienność w porównaniu do całkowitego rozstępu.
# 
# 2. Critic_Score (ocena krytyków):
#     - Średnia ocena wynosi około 69, a mediana to 71 – większość gier otrzymuje umiarkowanie pozytywne oceny.
#     - Dominanta to 70, co oznacza, że taka ocena jest wystawiana najczęściej.
#     - Rozstęp wynoszący 85 punktów oraz odchylenie standardowe na poziomie 13.93 wskazują na dość szeroki zakres ocen, ale ich zmienność (wyrażona współczynnikiem zmienności 20.2%) jest stosunkowo niska.
#     - Odchylenie ćwiartkowe wynosi 19, co oznacza, że centralne 50% gier (między Q1 = 60 a Q3 = 79) mieści się w tym przedziale ocen.
# 
# 3. User_Score (ocena użytkowników):
#     - Średnia ocena użytkowników to 7.18, a mediana (7.50) oraz dominanta (7.80) wskazują na to, że większość gier cieszy się dobrą opinią wśród graczy.
#     - Rozstęp wynosi 9.10, co wskazuje na pewną różnorodność ocen, ale odchylenie standardowe (1.44) oraz współczynnik zmienności (20.07%) wskazują na stosunkową jednorodność wyników w tej kategorii.
#     - Odchylenie ćwiartkowe to 1.70, a centralne 50% ocen mieści się w zakresie między 6.5 a 8.2, co również potwierdza względną stabilność opinii graczy.
#%%
projectData_cleaned['User_Score'] = pd.to_numeric(projectData_cleaned['User_Score'], errors='coerce')

# Obliczanie miar asymetrii (skewness) i kurtozy (kurtosis) przy użyciu pandas
asymmetry_kurtosis = pd.DataFrame({
    'Asymetria (skewness)': projectData_cleaned.skew(),
    'Kurtoza (kurtosis)': projectData_cleaned.kurt()
})

# Wyświetlenie wyników
print("Miary asymetrii i koncentracji dla analizowanych zmiennych:")
print(asymmetry_kurtosis)

#%% md
# Global_Sales
# - Asymetria (Skewness): 17.182206
#     - Rozkład danych jest znacznie asymetryczny w prawo.
#     - Oznacza to, że większość wartości jest skupiona w niższym zakresie, a tylko niewielka liczba obserwacji ma bardzo wysokie wartości (Global_Sales zawiera pojedyncze gry o ogromnych wynikach sprzedaży globalnej, co wypycha „ogon” rozkładu w prawo).
# 
# - Kurtoza (Kurtosis): 577.923286
#     - Bardzo wysoka wartość kurtozy wskazuje na rozkład o bardzo ostrym szczycie i długich ogonach. Oznacza to, że w danych występuje kilka ekstremalnych wartości, co jest typowe dla danych o sprzedaży globalnej w branży gier.
# 
# Podsumowanie: Rozkład Global_Sales jest skrajnie niesymetryczny, z dominującą większością małych wartości i kilkoma anomaliami (bardzo wysokimi wynikami).
# Critic_Score
# - Asymetria (Skewness): -0.615675
#     - Rozkład jest asymetryczny w lewo, ale asymetria nie jest bardzo silna.
#     - Większość gier ma względnie wysokie oceny krytyków (prawa strona rozkładu jest mocniej wypełniona), natomiast wartości niskie są mniej liczne.
# 
# - Kurtoza (Kurtosis): 0.147442
#     - Kurtoza oscyluje w pobliżu 0, co oznacza, że rozkład danych jest zbliżony do normalnego .
# 
# Podsumowanie: Critic_Score ma lekko spłaszczony rozkład i niewielką asymetrię w lewo, co jest charakterystyczne dla danych, gdzie wyniki są umiarkowanie wyrównane (większość gier ma podobne, nieekstremalne oceny).
#  User_Score
# - Asymetria (Skewness): -1.218593
#     - Rozkład jest asymetryczny w lewo, co oznacza, że większość użytkowników daje gry o wysokich wartościach ocen (prawa strona rozkładu), natomiast niskie oceny (lewa strona) zdarzają się rzadziej.
# 
# - Kurtoza (Kurtosis): 1.602901
#     - Kurtoza powyżej 0 oznacza, że dane są nieco bardziej skupione wokół wartości średniej, ale występują również grubsze ogony.
# 
# Podsumowanie: Rozkład User_Score wskazuje na to, że użytkownicy częściej zostawiają pozytywne oceny (wysokie), a negatywne oceny występują mniej regularnie. Istnieje też pewna liczba skrajnych wartości.
# 
# 
#%%
projectData_cleaned=projectData_selected.dropna()
sorted_games = projectData_cleaned.sort_values(by='Year_of_Release', ascending=False)

# Pobranie 50 najnowszych gier
top_50_latest_games = sorted_games.head(50)

# Wyświetlenie wyników
print(top_50_latest_games)


#%%

top_50_latest_games['User_Score'] = pd.to_numeric(top_50_latest_games['User_Score'], errors='coerce')
sorted_games['User_Score'] = pd.to_numeric(sorted_games['User_Score'], errors='coerce')


comparison_data = pd.DataFrame({
    'Category': ['Top 50'] * len(top_50_latest_games) + ['Bottom 50'] * len(sorted_games.tail(50)),
    'User_Score': pd.concat([top_50_latest_games['User_Score'], sorted_games.tail(50)['User_Score']])
})

# Group by 'Category' and calculate the mean of 'User_Score'
average_scores = comparison_data.groupby('Category')['User_Score'].mean().reset_index()


plt.figure(figsize=(10, 5))
sns.barplot(
    data=average_scores,
    x='Category',
    y='User_Score',
    palette='Set2'
)


for index, row in average_scores.iterrows():
    plt.text(index, row['User_Score'] + 0.1, f"{row['User_Score']:.2f}", ha='center', fontsize=12)


plt.title('Average User Score for Top 50 and Bottom 50 Games', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Average User Score', fontsize=12)
plt.ylim(0, 10)  # Set range for Y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


#%%

#liczenie zakresu czasu
max_year=projectData_cleaned['Year_of_Release'].max()
min_year=projectData_cleaned['Year_of_Release'].min()
print(max_year)
print(min_year)
year_diff=max_year-min_year
print(year_diff)
#%%

projectData_cleaned = projectData_selected.dropna(subset=['Year_of_Release', 'Critic_Score']).copy()

projectData_cleaned['Year_Group'] = (projectData_cleaned['Year_of_Release'] // 5) * 5


plt.figure(figsize=(12, 6))  # Rozmiar wykresu

# Tworzenie wykresu pudełkowego
sns.boxplot(
    data=projectData_cleaned,
    x='Year_Group',
    y='Critic_Score',
    palette='Set3',
    hue=None  # Wyłączenie legendy związanej z hue
)

# Dodanie tytułu i etykiet
plt.title('Rozkład wyników krytyków w przedziałach czasowych', fontsize=16)
plt.xlabel('Przedziały lat', fontsize=12)
plt.ylabel('Wyniki krytyków', fontsize=12)
plt.xticks(rotation=45)  # Obrót etykiet na osi X (opcjonalne)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


#%%

#%%
projectData_cleaned = projectData_selected.dropna(subset=['Year_of_Release', 'Critic_Score']).copy()

# Definicja przedziałów lat i odpowiadających im etykiet
bins = [1984, 1990, 1995, 2000, 2005, 2010, 2016]
labels = ['1985-1990', '1991-1995', '1996-2000', '2001-2005', '2006-2010', '2011-2016']

# Tworzenie nowej kolumny 'Year_Group' na podstawie kolumny 'Year_of_Release'
projectData_cleaned['Year_Group'] = pd.cut(projectData_cleaned['Year_of_Release'], bins=bins, labels=labels)

# Tworzenie wykresu pudełkowego
plt.figure(figsize=(12, 6))  # Rozmiar wykresu
sns.set_style("whitegrid")  # Styl wykresu

sns.boxplot(
    data=projectData_cleaned,
    x='Year_Group',
    y='Critic_Score',
    palette='Set3',
    showfliers=False  # Ukrycie wartości odstających
)

# Dodanie tytułu i etykiet
plt.title('Rozkład wyników krytyków w przedziałach czasowych', fontsize=16)
plt.xlabel('Przedziały lat', fontsize=12)
plt.ylabel('Wyniki krytyków', fontsize=12)
plt.xticks(rotation=45)  # Obrót etykiet na osi X
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
#%%
projectData_cleaned['User_Score'] = pd.to_numeric(projectData_cleaned['User_Score'], errors='coerce')

# Definicja przedziałów lat
bins = [1984, 1990, 1995, 2000, 2005, 2010, 2016]
labels = ['1985-1990', '1991-1995', '1996-2000', '2001-2005', '2006-2010', '2011-2016']

# Tworzenie nowej kolumny z grupami lat
projectData_cleaned['Year_Group'] = pd.cut(projectData_cleaned['Year_of_Release'], bins=bins, labels=labels)

# Obliczanie średniego User_Score dla każdego przedziału
user_score_avg = projectData_cleaned.groupby('Year_Group')['User_Score'].mean().reset_index()

# Wykres
plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

sns.barplot(
    data=user_score_avg,
    x='Year_Group',
    y='User_Score',
    palette='Set3'
)

plt.title('Średnia wartość User_Score w przedziałach czasowych', fontsize=16)
plt.xlabel('Przedziały lat', fontsize=12)
plt.ylabel('Średnia User_Score', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
#%%
# Grupowanie po wydawcach i zliczanie liczby gier dla każdego wydawcy
publisher_counts = projectData_cleaned['Publisher'].value_counts().head(10).reset_index()
publisher_counts.columns = ['Publisher', 'Game Count']

# Tworzenie wykresu słupkowego
plt.figure(figsize=(12, 6))
sns.barplot(
    data=publisher_counts,
    x='Publisher',
    y='Game Count',
    palette='magma'
)

# Dodanie tytułu i opisów osi
plt.title('Top 10 Publishers by Number of Games', fontsize=16)
plt.xlabel('Publisher', fontsize=12)
plt.ylabel('Number of Games', fontsize=12)
plt.xticks(rotation=45)  # Obrót etykiet (jeśli nazwy wydawców są długie)

# Dodanie wartości liczbowych nad słupkami
for index, row in publisher_counts.iterrows():
    plt.text(index, row['Game Count'] + 5, f"{row['Game Count']}", ha='center', fontsize=10)

plt.tight_layout()
plt.show()

#%%
publisher_stats = projectData_cleaned.groupby('Publisher').agg(
    avg_user_score=('User_Score', 'mean'),
    game_count=('Publisher', 'count')
).reset_index()

# Filtrowanie wydawców, którzy wydali co najmniej 20 gier
top_publishers_filtered = publisher_stats[publisher_stats['game_count'] >= 20]

# Posortowanie wydawców według średniej oceny użytkowników w malejącej kolejności
top_publishers_sorted = top_publishers_filtered.sort_values(by='avg_user_score', ascending=False).head(10)

# Resetting the index to ensure proper alignment of text annotations
top_publishers_sorted = top_publishers_sorted.reset_index(drop=True)

# Tworzenie wykresu słupkowego
plt.figure(figsize=(12, 6))
barplot = sns.barplot(
    data=top_publishers_sorted,
    x='avg_user_score',
    y='Publisher',
    palette='coolwarm'
)

# Dodanie tytułu i opisów osi
plt.title('Top 10 Publishers by Average User Score (min. 20 games)', fontsize=16)
plt.xlabel('Average User Score', fontsize=12)
plt.ylabel('Publisher', fontsize=12)

# Correctly adding values above the bars
for i, row in top_publishers_sorted.iterrows():
    plt.text(
        row['avg_user_score'] + 0.1,  # X-axis position (slightly offset)
        i,  # Correct Y-axis position from the loop index
        f"{row['avg_user_score']:.2f}",  # Value to display (formatted to 2 decimals)
        va='center', fontsize=10
    )

plt.tight_layout()
plt.show()

#%%
projectData_cleaned = projectData_selected.dropna()

platform_counts = projectData_cleaned['Platform'].value_counts()



# Wybór 10 najpopularniejszych platform
top_10_platforms = platform_counts.head(10)

# Suma dla reszty platform
other_count = platform_counts.iloc[10:].sum()

# Przygotowanie danych na wykres
platform_labels = list(top_10_platforms.index) + ['Inne']
platform_sizes = list(top_10_platforms.values) + [other_count]

# Tworzenie wykresu kołowego
plt.figure(figsize=(8, 8))
plt.pie(
    platform_sizes,
    labels=platform_labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel')
)
plt.title('Udział najczęściej używanych platform (10 głównych + Inne)', fontsize=14)
plt.show()



