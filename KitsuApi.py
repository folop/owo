import requests


class KitsuApi:
    def __init__():
        pass

    def hledat_anime(search):
        # dotaz na api
        odpoved = requests.get("https://kitsu.io/api/edge/anime?filter[text]=" + search)
        
        # parse jsonu s odpovedi
        data = odpoved.json()
        return data["data"]

    def zobrazit_detial(id):
        odpoved = requests.get("https://kitsu.io/api/edge/anime/" + id)
        data = odpoved.json()
        return data["data"]
    
    def zobrazit_epizody(id):
        odpoved = requests.get("https://kitsu.io/api/edge/anime/" + id + "/episodes")
        data = odpoved.json()
        return data["data"]
    