import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
np.random.seed(42)

# --- 1. Generare dataset 60 zile ---
produse = ['ProdusA','ProdusB','ProdusC','ProdusD','ProdusE','ProdusF','ProdusG','ProdusH']
zile = pd.date_range(start='2024-01-01', periods=60)
vanzari_data = []

for zi in zile:
    n_prod = np.random.randint(5,16)
    produse_vandute = np.random.choice(produse, size=n_prod, replace=True)
    for produs in produse_vandute:
        pret = round(max(1, np.random.normal(40,8)),2)
        cantitate = np.random.randint(1,11)
        promo = np.random.rand() < 0.3
        if promo:
            pret = round(pret*0.8,2)
        total_vanzari = round(pret * cantitate,2)
        profit = round(total_vanzari * 0.3,2)
        vanzari_data.append({
            'data': zi,
            'produs': produs,
            'cantitate': cantitate,
            'pret_unitar': pret,
            'promo': promo,
            'total_vanzari': total_vanzari,
            'profit': profit
        })

df_vanzari = pd.DataFrame(vanzari_data)

# --- 2. Statistici generale ---
print("Total vanzari:", df_vanzari['total_vanzari'].sum())
print("Total profit:", df_vanzari['profit'].sum())

# --- 3. Analiza si vizualizare ---
venit_profit_pe_zi = df_vanzari.groupby('data')[['total_vanzari','profit']].sum().reset_index()
plt.figure(figsize=(12,6))
plt.plot(venit_profit_pe_zi['data'], venit_profit_pe_zi['total_vanzari'], label='Venit total')
plt.plot(venit_profit_pe_zi['data'], venit_profit_pe_zi['profit'], label='Profit total')
plt.xlabel('Data')
plt.ylabel('Lei')
plt.title('Evolutia veniturilor si profitului pe zile')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
