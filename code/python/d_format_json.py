from bs4 import BeautifulSoup # library to parse HTML documents
import json
import numpy as np
import os
import pandas as pd # library for data analysis
import random
import requests # library to handle requests


def format_json():
    """
    make readable by Chart.JS as bubble chart
    """

    print("begin formatting")

    a_list = []

    # read json
    f = open(establish_src())
    data = json.load(f)
    f.close()


    print(data["Albania"])


    for key in data.keys():

        country = key
        print("country = ")
        print(country)

        content = data[key]
        print(content)

        a = {}

        try:
            a["label"] = str(content["list_of_countries_by_gdp__nominal_"]["UN region"] + " | " + str(key))
            a["region"] = content["list_of_countries_by_gdp__nominal_"]["UN region"]

        except:
            a["label"] = str(key)
            a["region"] = "Unspecified"

        print("a = ")
        print(a)


        values = {}
        try:
            values["x"] = content["list_of_countries_by_number_of_households"]["% 1 Member"]
            print("values = ")
            print(values)
        except:
            continue

        try:
            values["y"] = content["list_of_countries_by_suicide_rate"]["All"]
        except:
            continue

        try:
            values["r"] = content["list_of_countries_by_alcohol_consumption_per_capita"]["2016[8]"]
        except:
            values["r"] = 3

        print("values = ")
        print(values)


        a["data"] = [values]

        # assign color based on UN region

        r, g, b = 255*random.random(), 255*random.random(), 255*random.random()


        if "Africa" in str(a["region"]):
            r, g, b = r*0.25, g*1, b*0.8

        elif "America" in str(a["region"]):
            r, g, b = r*0.25, g*1, b*0.8

        elif "Asia" in str(a["region"]):
            r, g, b = r*1, g*0.1, b*0.2

        elif "Europe" in str(a["region"]):
            r, g, b = r*.1, g*0.8, b*0.8

        elif "Oceania" in str(a["region"]):
            r, g, b = r*.8, g*0.1, b*0.8

        else:
            r, g, b = 100, 100, 100


        color = str("rgb(" + str(int(r)) + ", " + str(int(g)) + ", " + str(int(b)) + ")")
        a["backgroundColor"] = color

        a_list.append(a)


    print(len(a_list))

    print(a_list)

    bubble = {}
    bubble["datasets"] = a_list

    """
    json_obj = bubble
    sorted_obj = dict(json_obj)
    sorted_obj = sorted(json_obj["datasets"], key="data" : x['r'], reverse=True)
    """


    # create destination json
    dst_fol = os.path.join("code", "json")
    if not os.path.exists(dst_fol): os.makedirs(dst_fol)
    dst_fil = os.path.join(dst_fol, "bubble.json")
    f = open(dst_fil, 'w')
    f.close()


    js = json.dumps(bubble, ensure_ascii=False, indent=4)
    fp = open(dst_fil, 'a')
    fp.write(js)
    fp.close()


    # create destination json
    dst_fol = os.path.join("docs", "js")
    if not os.path.exists(dst_fol): os.makedirs(dst_fol)
    dst_fil = os.path.join(dst_fol, "bubble.js")
    f = open(dst_fil, 'w')
    f.close()


    js = json.dumps(bubble, ensure_ascii=False, indent=4)
    fp = open(dst_fil, 'a')
    fp.write("const bubble = " + "\n")
    fp.write(js)
    fp.write(";")
    fp.close()




def establish_src():
    """
    establish dst file
    """

    # create destination json
    dst_fol = os.path.join("code", "json")
    if not os.path.exists(dst_fol): os.makedirs(dst_fol)
    dst_fil = os.path.join(dst_fol, "info.json")

    return(dst_fil)
