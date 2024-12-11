# Appeler l'API Meta et retourner la réponse
import requests
from datetime import datetime


instagram_token = "EAAH3RcJ43q8BO6CF8kAEHUXPI9FRtEzPEoMJUeZBoQhl61oiWvFmcZBmvYLruTjOiHNkfVvn9z6yb0XITol4JwEGkM7YZCS66Y8BL14a22y18UZB2wU9J6ZCvDyUyxC8ymDMPGqEvN10ZBrH9EKbVc5ZB5fa2M3qEFWDX5EhuE0UFOkStLILCdlDaS7HqYc1jd7rsvKvgyuHkjSkUeWofsJsoVZB" 

token = "EAAVdPLvAoZBoBO2drElZAA3lzJraqfsBBsZBEOCESmaqqD92978j2ZCJkPrqXfKMiyJct0CksAgnZCDWhI0ZBm3qz6wZAiL8eturpyaVkBg1zSq6vJ8j1cgqmJ5jkRdYWg4PQHaoLfXuYL4jB2pQTZAh8evegJUeI5dfZCVEDsz5w0g7JZATloDRoWWeszds8ZD"
account_id = "act_190090974920462"

def get_instagram_posts(access_token, user_id):
    # on fait le call à l'API Meta 
    url = f"https://graph.instagram.com/{user_id}/media"
    params = {
        "fields": "id,caption,media_type,media_url,timestamp",
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print ("Posts instagram récupérés et retournés")
        return response.json()
    else: 
        print (f"erreur : {response.status_code}, {response.text}")
        return []
    

instagram_posts = get_instagram_posts(instagram_token, account_id)
print (f"voici les posts instagram : {instagram_posts}")


def call_meta_api(token, id):
    print("Calling the META API")
    # URL de base sans le token
    url = f'https://graph.facebook.com/v18.0/{id}/campaigns'
    # Paramètres de la requête
    params = {
        "fields": "id,name,status",
        'access_token': token,
    }
    # Faire la requête avec les paramètres
    r = requests.get(url, params=params)
    # Afficher la réponse
    if r.status_code == 200:
        # Si la réponse est un JSON
        try:
            campaigns = (r.json())
            return campaigns
        except ValueError:
            print("Erreur : La réponse n'est pas un JSON valide.")
    else:
        print(f"Error: {r.text}")

def get_active_campaigns(campaigns):
    # Si le JSON contien un élément 'data'
    if "data" in campaigns:
        activeCampaigns = []
        for campaign in campaigns['data']:
            # ne retourner que les campagnes actives
            if campaign['status'] == "ACTIVE":
                # push les campagnes actives dans l'array
                activeCampaigns.append(campaign)
        return activeCampaigns
    else:
        print("Pas de data")
        
# Appeler la fonction
# Le problème que j'ai c'est que la fonction fait tout là. il faut faire d'autres fnctions
campaigns = call_meta_api(token, account_id)
active_campaigns = get_active_campaigns(campaigns)
print (active_campaigns)

