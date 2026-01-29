import pandas as pd


try:
    df = pd.read_csv("vanzari.csv")
except FileNotFoundError:
    print("Eroare: fisierul nu exista!")
    exit()
except pd.errors.ParserError:
    print("Eroare: fisierul CSV este corupt sau format gresit!")
    exit()

# --- 2. Conversie data_vanzarii la datetime ---
df['data_vanzarii'] = pd.to_datetime(df['data_vanzarii'], format='%d.%m.%Y', errors='coerce')

# Eliminam liniile cu date invalide
df = df.dropna(subset=['data_vanzarii'])

# --- 3. Venit total per vanzare ---
df['venit'] = df['cantitate_vanduta'] * df['pret']

# --- 4. Cele mai vandute produse pe luna ---
# Extragem luna si anul
df['luna'] = df['data_vanzarii'].dt.month
df['an'] = df['data_vanzarii'].dt.year

# Grupare pe produs + luna + an
vandute_lunar = df.groupby(['an', 'luna', 'produs'])['cantitate_vanduta'].sum().reset_index()

# Sortare descrescatoare pentru a vedea cele mai vandute produse
vandute_lunar_sorted = vandute_lunar.sort_values(['an', 'luna', 'cantitate_vanduta'], ascending=[True, True, False])
print("\n--- Cele mai vandute produse pe luna ---")
print(vandute_lunar_sorted)

# --- 5. Venitul total pe fiecare produs ---
venit_total_produs = df.groupby('produs')['venit'].sum().reset_index()
print("\n--- Venitul total pe fiecare produs ---")
print(venit_total_produs)

# --- 6. Filtrare vanzari intre doua date ---
start = pd.to_datetime('01.01.2024', format='%d.%m.%Y')
end = pd.to_datetime('31.03.2024', format='%d.%m.%Y')
vanzari_filtrate = df[(df['data_vanzarii'] >= start) & (df['data_vanzarii'] <= end)]
print("\n--- Vanzari intre 01.01.2024 si 31.03.2024 ---")
print(vanzari_filtrate)

# --- 7. Venitul mediu lunar (grupat dupa luna si an) ---
venit_mediu_lunar = df.groupby(['an', 'luna'])['venit'].mean().reset_index()
print("\n--- Venitul mediu lunar ---")
print(venit_mediu_lunar)
