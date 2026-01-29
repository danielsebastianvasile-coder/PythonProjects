import numpy as np
import pandas as pd

# --- Setare seed pentru reproducibilitate ---
np.random.seed(42)

# Lista de produse
produse = ['ProdusA', 'ProdusB', 'ProdusC', 'ProdusD', 'ProdusE', 'ProdusF', 'ProdusG', 'ProdusH']

# Perioada de 60 de zile
zile = pd.date_range(start='2024-01-01', periods=60)

# Lista pentru a stoca toate vanzarile
vanzari_data = []

for zi in zile:
    # 1️⃣ Numar aleatoriu de produse vandute pe zi (5-15)
    n_prod = np.random.randint(5, 16)

    # Alegem produse aleatoriu (fara repetitie)
    produse_vandute = np.random.choice(produse, size=n_prod, replace=True)

    for produs in produse_vandute:
        # 2️⃣ Pretul unitar (distributie normala)
        pret = np.random.normal(loc=40, scale=8)
        pret = max(1, round(pret, 2))  # pret minim 1

        # 3️⃣ Cantitate vanduta (uniforma)
        cantitate = np.random.randint(1, 11)

        # 4️⃣ Promoții: 30% sanse ca pretul sa scada cu 20%
        if np.random.rand() < 0.3:
            pret = round(pret * 0.8, 2)
            promo = True
        else:
            promo = False

        # 5️⃣ Total vanzari
        total_vanzari = round(pret * cantitate, 2)

        # 6️⃣ Profit: 30% marja
        profit = round(total_vanzari * 0.3, 2)

        vanzari_data.append({
            'data': zi,
            'produs': produs,
            'cantitate': cantitate,
            'pret_unitar': pret,
            'promo': promo,
            'total_vanzari': total_vanzari,
            'profit': profit
        })

# --- Creare DataFrame ---
df_vanzari = pd.DataFrame(vanzari_data)

# --- Statistici generale ---

print("\n--- Statistici generale ---")
print("Pret unitar:")
print(f"  Media: {df_vanzari['pret_unitar'].mean():.2f}")
print(f"  Max: {df_vanzari['pret_unitar'].max():.2f}")
print(f"  Min: {df_vanzari['pret_unitar'].min():.2f}")

print("\nCantitate vanduta:")
print(f"  Media: {df_vanzari['cantitate'].mean():.2f}")
print(f"  Max: {df_vanzari['cantitate'].max()}")
print(f"  Min: {df_vanzari['cantitate'].min()}")

print("\nProfit:")
print(f"  Media: {df_vanzari['profit'].mean():.2f}")
print(f"  Max: {df_vanzari['profit'].max():.2f}")
print(f"  Min: {df_vanzari['profit'].min():.2f}")

# --- Totaluri pe 60 de zile ---
total_vanzari = df_vanzari['total_vanzari'].sum()
total_profit = df_vanzari['profit'].sum()

print(f"\nTotal vanzari pe 60 zile: {total_vanzari:.2f}")
print(f"Total profit pe 60 zile: {total_profit:.2f}")

# --- Optional: afisare primele 10 randuri ---
print("\nPrimele 10 vanzari generate:")
print(df_vanzari.head(10))
