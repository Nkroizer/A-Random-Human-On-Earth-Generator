import random
import stats
import math
import requests


def generate_human():
    # Randomly generating the country of the person
    country = random.choices(stats.country_list, weights=stats.country_percent)[0]

    # Getting the stats of the selected country
    country_stats = stats.all_stats[country]

    # Getting the average life expectancy of people (both male and female) in that country
    average_life_expectancy = math.ceil(country_stats["averageLifeExpectancy"])

    # This is a general estimation of the person's age, so we can find out
    # their sex distribution by the age group, Later we will figure out the exact age
    age = random.randint(5, average_life_expectancy)

    # Just A default value, in case something goes wrong along the way
    sex = "Male"
    
    # Determining the age group base on the age estimation
    age_group = ""
    if 0 <= age <= 14:
        age_group = "children"
    elif 15 <= age <= 64:
        age_group = "adults"
    elif 65 <= age <= 110:
        age_group = "elderly"

    sex = random.choices(
        stats.sex_list,
        weights=(
            country_stats[age_group]["male"],
            country_stats[age_group]["female"],
        ),
    )[0]

    # Adding a few extra years
    extra_years = random.randint(0, 20)

    if sex == "Male":
        gender = "m"
        if age_group == "elderly":
            age = random.randint(
                65, math.ceil(country_stats["averageLifeExpectancyMale"]) + extra_years
            )
    else:
        gender = "f"
        if age_group == "elderly":
            age = random.randint(
                65,
                average_life_expectancy_female=math.ceil(
                    country_stats["averageLifeExpectancyFemale"]
                )
                + extra_years,
            )

    api_key = "65b9b35a686fda98551c7a7fd50d5f16"
    country_code = country_stats["countryCode"]

    url = (
        "https://api.parser.name/?api_key="
        + api_key
        + "&endpoint=generate&country_code="
        + country_code
        + "&gender="
        + gender
    )

    response = requests.get(url)

    response_json = response.json()

    # print(response_json)

    first_name = response_json["data"][0]["name"]["firstname"]["name"]

    last_name = response_json["data"][0]["name"]["lastname"]["name"]

    return (
        first_name
        + " "
        + last_name
        + " a "
        + sex
        + " from "
        + country.capitalize()
        + " age "
        + str(age)
    )
