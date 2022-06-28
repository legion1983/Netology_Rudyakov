import requests
from pprint import pprint
# ___________________________Task N1_Super heroes_______________________

def test_request_hulk():
    url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
    # "Hulk": 332
    response = requests.get(url=url)
    response.json()

    for items in response.json()["results"]:
        # print(items)
        for params in items.values():
            if params == "Hulk":
                print("")
                # print("Hulk_id:", items["id"])
                Hulk_intelligence = int(items["powerstats"]['intelligence'])
                # print("Hulk_intelligence", Hulk_intelligence)

        break
    return {"Hulk_intelligence": Hulk_intelligence}


def test_request_Captain_America():
    url = "https://superheroapi.com/api/2619421814940190/search/Captain America"
    # "Captain_America": 149
    response = requests.get(url=url)
    response.json()
    for items in response.json()["results"]:
        # print(items)
        for params in items.values():
            if params == "Captain America":
                print("")
                # print("Captain_Americ_id:", items["id"])
                Captain_America_intelligence = int(items["powerstats"]['intelligence'])
                # print("Captain_America_intelligence", Captain_America_intelligence)
        break
    return {"Captain_America_intelligence": Captain_America_intelligence}

def test_request_Thanos():
    url = "https://superheroapi.com/api/2619421814940190/search/Thanos"
    # "Thanos": 655
    response = requests.get(url=url)
    response.json()
    for items in response.json()["results"]:
        # print(items)
        for params in items.values():
            if params == "Thanos":
                print("")
                # print("Thanos_id:", items["id"])
                Thanos_intelligence = int(items["powerstats"]['intelligence'])
                # print("Thanos_intelligence", Thanos_intelligence)
        break
    return {"Thanos_intelligence": Thanos_intelligence}


def max_intelligence_hero():
    dict_of_heroes = test_request_hulk() | test_request_Captain_America() | test_request_Thanos()
    # print(dict_of_heroes)
    max_intelligence_hero = max(dict_of_heroes.values())
    # print(max_intelligence_hero)
    final_dict = {k: v for k, v in dict_of_heroes.items() if v == max_intelligence_hero}
    print("Самый умный герой", final_dict)


if __name__ == '__main__':
    max_intelligence_hero()

    # print(test_request_Thanos())









