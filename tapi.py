# -*- coding: UTF-8 -*-
from tinder_api_sms import *
from time import sleep
import urllib.request, os, json, datetime, random

try:
    recs = get_recommendations()["results"]
except KeyError:
    print("no recommendations found")


def settings():
    # Default settings
    try:
        dset = input(
            "Current settings are: \n> Age range from 18 to 22 \n> Distance: 2 mile(s) \n> Seeking for Female \n -------------- \nDo you want to change? ( y/n ): "
        )
        if dset == "y":
            raise SyntaxError
        elif dset == "n":
            print("Okay then")

        else:
            print("you must choose yes ( y ) or no ( n )")

    except SyntaxError:
        # get distance
        distance = int(input("\n Filter distance ( 1 > 100 Mile ): "))
        if distance <= 0 or distance >= 100:
            print("distance must be higher than 0 and less than 101 mile")
            settings()

        # get min age
        min_age = int(input("\n Filter min age ( >= 18 ): "))
        if min_age < 18:
            print("min age must be higher or equal to 18")
            settings()

        # get max age
        max_age = int(input("\n Filter max age ( >= 18 ) "))
        if max_age < 18:
            print("max age must be higher or equal to 18")
            settings()

        # seeking for ...
        gender = int(input("\n Seeking for male ( 0 ) , female ( 1 ): "))
        if gender not in range(0, 2):
            print("Type 0 if you are looking for male, and 1 for female")
            settings()
        change_preferences(
            age_filter_min=min_age, age_filter_max=max_age, distance_filter=distance
        )

        print(
            "Filter age range from {} to {} \n Distance: {} mile(s) ".format(
                min_age, max_age, distance
            )
        )


def fetch_data():
    settings()
    print("found {} girls - start fetching images".format(len(recs)))
    i = 1
    # get each recommend in recs
    for person in recs:
        imagecount = 0
        i += 1
        print("{}___________{} - {}___________".format("\033[5m", i, person["name"]))
        print("\033[0m")
        # make directory
        try:
            os.mkdir("images/{}".format(person["_id"]))
        except FileExistsError:
            pass
        data = {}
        data["info"] = []
        data["info"].append(
            {
                "id": person["_id"],
                "name": person["name"],
                "birth_year": person["birth_date"][:4],
                "distance": person["distance_mi"] * 1.6,
                "school": person["schools"],
                "bio": person["bio"],
            }
        )
        print("writing info")
        with open(
            os.path.join(
                "images/{}".format(person["_id"]), "{}.json".format(person["name"]),
            ),
            "w",
            encoding="utf8",
        ) as outfile:
            json.dump(data, outfile, ensure_ascii=False)
        # download highlight photo of recommended's person
        for photo in person["photos"]:
            urllib.request.urlretrieve(
                photo["url"],
                os.path.join(
                    "images/{}".format(person["_id"]), "{}.jpg".format(imagecount)
                ),
            )
            print("fetching: images/{}/{}.jpg".format(person["name"], imagecount))
            imagecount += 1
        print(" ")
    print("{}DONE!!!".format("\033[92m"))


def get_match_id():
    i = 0
    count = 70
    matches_dict = all_matches(count)
    matches = matches_dict["data"]["matches"]
    for user in matches:
        person = user["person"]
        i += 1
        print(i, user["id"], person["name"])
        matchage = int(str(datetime.date.today())[:4]) - int(person["birth_date"][:4])
        print("age: {} ({}) ".format(matchage, person["birth_date"][:4]))
        print("__________________________________________")


def auto_like():

    # Auto Like
    i = 0
    print("Found {} girls - start botting".format(len(recs)))
    for girl in recs:
        sleeptime = random.randint(1, 2)
        i += 1
        like(girl["_id"])
        print("{}. liked  {}".format(i, girl["name"]), end="\n\n")
        sleep(sleeptime)
    print("liked {} in total".format((i)))
