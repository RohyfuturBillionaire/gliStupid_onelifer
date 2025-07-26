# efa tsy ilaina intsony

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Exemple de données où l'heure du prochain caca est la cible
data = pd.DataFrame([
    {"heure_actuelle": 8.0, "café": 1, "repas_riche": 1, "stress": 0, "hier_wc": 1, "expression_tendue": 1, "heure_prochain_caca": 9.5},
    {"heure_actuelle": 10.0, "café": 0, "repas_riche": 0, "stress": 1, "hier_wc": 0, "expression_tendue": 0, "heure_prochain_caca": 15.0},
    {"heure_actuelle": 17.5, "café": 1, "repas_riche": 1, "stress": 1, "hier_wc": 1, "expression_tendue": 1, "heure_prochain_caca": 20.0},
])

# Variables explicatives
X = data.drop("heure_prochain_caca", axis=1)

# Cible (heure du prochain caca)
y = data["heure_prochain_caca"]

# Entraînement modèle de régression
model = RandomForestRegressor()
model.fit(X, y)

# Prédire l'heure du prochain caca pour une nouvelle situation
# Ici on ne donne aucune nouvelle donnée, donc il faut une situation par défaut ou moyenne
# Par exemple on peut prédire à partir de la dernière ligne (ou une valeur moyenne)
nouvelle_situation = pd.DataFrame([{
    "heure_actuelle": 12.0,
    "café": 0,
    "repas_riche": 0,
    "stress": 1,
    "hier_wc": 0,
    "expression_tendue": 0
}])

prediction = model.predict(nouvelle_situation)
print(f"Heure estimée du prochain caca : {prediction[0]:.2f} heures")
