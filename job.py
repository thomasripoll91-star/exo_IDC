import os

a = 2 
print("coucou", a)

# Récupération du secret injecté dans l'environnement
token = os.environ.get("SECRET_API_TOKEN")
print(f"Le token API est : {token}")