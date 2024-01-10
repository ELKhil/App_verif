import requests


def get_user_token():
    """Demander à l'utilisateur de saisir le token."""
    return input("Veuillez entrer votre token: ")


def get_auth_token(auth_url, auth_data):
    """Obtenir un token d'authentification."""
    try:
        response = requests.post(auth_url, json=auth_data)
        if response.status_code == 200:
            return response.json().get('token')
        else:
            print(f"Échec de l'authentification : {response.status_code}")
            return None
    except Exception as e:
        print(f"Erreur lors de l'authentification : {e}")
        return None


def check_api_status(api_url, token):
    """Vérifier le statut de l'API."""
    headers = {'Authorization': f'Bearer {token}'}
    try:
        response = requests.get(api_url, headers=headers)
        return response.status_code
    except Exception as e:
        print(f"Erreur lors de la requête API : {e}")
        return None


# Exemple d'utilisation
auth_url = "https://stages-staff-med.polesante.ulb.be/app"
token = get_user_token()

if token:
    api_url = "https://stages-staff-med.polesante.ulb.be/app/fac/internships"
    status_code = check_api_status(api_url, token)
    if status_code:
        print(f"Code de statut de l'API : {status_code}")
else:
    print("Authentification échouée, impossible de vérifier le statut de l'API.")
