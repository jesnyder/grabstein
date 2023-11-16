from bs4 import BeautifulSoup # library to parse HTML documents
import json
import numpy as np
import os
import pandas as pd # library for data analysis
import requests # library to handle requests


def coregister_df():
    """
    generate a single json file
    that lists countries, gdp, birthrate, and suicide rate

    """

    # establish destimation file
    dst_fil = establish_dst()


    a = {}
    #a["countries"] = list_countries()

    for country in list_countries():

        #a[country] = []

        print(country)
        aa = add_keys(country)

        a[country] = aa


    js = json.dumps(a, ensure_ascii=False, indent=4)

    # Open new json file if not exist it will create
    fp = open(dst_fil, 'a')

    # write to json file
    fp.write(js)

    # close the connection
    fp.close()




def add_keys(country):
    """

    """

    aa = {}

    src_fol = os.path.join("code", "data")
    for fil in os.listdir(src_fol):

        print(fil)
        src_fil = os.path.join(src_fol, fil)
        df = pd.read_csv(src_fil)
        del df["Unnamed: 0"]

        #print(df)

        columns = df.columns

        for name in df.columns:



            #fil = {}

            if "country" in name.lower():


                dfi = df[df[name] == country]
                #print(dfi)

                if len(dfi[name]) < 1: continue

                i_dict = {}
                for namei in dfi.columns:

                    #aa[namei] = list(dfi[namei])[0]

                    i_dict[namei] = list(dfi[namei])[0]


                aa[fil.split(".")[0]] = i_dict



    print(aa)
    return(aa)



def list_countries():
    """
    list countries
    """

    countries = []

    src_fol = os.path.join("code", "data")
    for fil in os.listdir(src_fol):

        print(fil)
        src_fil = os.path.join(src_fol, fil)
        df = pd.read_csv(src_fil)
        del df["Unnamed: 0"]

        print(df)

        columns = df.columns

        for name in df.columns:

            #fil = {}

            if "country" in name.lower():

                for country in list(df[name]):

                    if country not in countries:
                        countries.append(country)

        countries.sort()
        return(countries)


def establish_dst():
    """
    establish dst file
    """

    # create destination json
    dst_fol = os.path.join("code", "json")
    if not os.path.exists(dst_fol): os.makedirs(dst_fol)
    dst_fil = os.path.join(dst_fol, "info.json")
    f = open(dst_fil, 'w')
    f.close()

    return(dst_fil)
