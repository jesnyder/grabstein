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

    # tasks
    # 1 estblish file to save data
    # 2 build json from scraped data
    # 3 build dataframe
    # 4 save both

    tasks = [3]


    # aggregate source data into a single dataframe
    if 1 in tasks: aggregate_df()

    # count the unique values in each df columns
    if 2 in tasks: summarize_df()

    # build json for js plotly
    if 3 in tasks: json_plotly()

    # establish destimation file
    if 4 in tasks: dst_fil = establish_dst()

    # build json
    if 5 in tasks: js = build_json(dst_fil)

    # from json, build a dataframe
    if 6 in tasks: df = json_to_df(js)

    # save files
    if 7 in tasks:
        js = json.dumps(a, ensure_ascii=False, indent=4)

        # Open new json file if not exist it will create
        fp = open(dst_fil, 'a')

        # write to json file
        fp.write(js)

        # close the connection
        fp.close()


def json_plotly():
    """

    """





    js = {}

    # retrieve the
    src_fil = os.path.join("code", "df", "all.csv")
    df = pd.read_csv(src_fil)
    del df["Unnamed: 0"]

    for name in df.columns:

        #print(name)
        if "--UN region" not in name: continue
        #print(name)

        un_regions = []
        for value in list(df[name]):
            if value in un_regions: continue
            un_regions.append(value)

    dst_fil = os.path.join("docs", "js", "region.js")
    fp = open(dst_fil, 'w')
    #fp.write("var region = " + str(un_regions) + "; \n \n")
    fp.close()

    for name in df.columns:

        #print(name)
        if "--UN region" not in name: continue
        #print(name)


        for un_region in un_regions:
            print(un_region)
            df_temp = df[df[name] == un_region]
            #print(df_temp)

            region = {}

            region["mode"] = 'markers'
            region["type"] = 'scatter'
            region["name"] = un_region
            region["text"] = list(df_temp["country"])
            region["x"] = list(df_temp["list_of_countries_by_number_of_households.csv--% 1 Member"])
            region["y"] = list(df_temp["list_of_countries_by_suicide_rate.csv--All"])
            marker = {}
            marker["size"] = list(df_temp["list_of_countries_by_alcohol_consumption_per_capita.csv--2016[8]"])
            region["marker"] = marker

            """
            for col_name in df_temp.columns:
                print(col_name)

                src_name = col_name.split(".")[0]
                data_name = col_name.split("--")[-1]

                if src_name not in region.keys():
                    region[src_name] = []

                region[col_name] = list(df_temp[col_name])
            """

            js = region



            js_plotly = json.dumps(js, ensure_ascii=False, indent=4)
            fp = open(dst_fil, 'a')
            fp.write("var " + str(un_region) + " = ")
            fp.write(js_plotly)
            fp.write("; " + "\n" + "\n")
            fp.close()







def summarize_df():
    """
    save
    """

    src_fil = os.path.join("code", "df", "all.csv")
    df = pd.read_csv(src_fil)
    del df["Unnamed: 0"]


    for name in df.columns:

        a = list(df[name])

        summary = pd.DataFrame()
        values, counts = [], []

        for value in a:
            if value in values: continue
            values.append(value)
            counts.append(a.count(value))

        summary["value"] = values
        summary["count"] = counts
        summary.sort_values(by=["count"], ascending=False)

        print(name)

        fil_name = name
        chars = ["/"]
        for char in chars:
            fil_name = fil_name.replace(char, " ")

        # save summary dataframe
        dst_fol = os.path.join("code", "summary")
        if not os.path.exists(dst_fol): os.makedirs(dst_fol)
        dst_fil = os.path.join(dst_fol, str(fil_name) + ".csv")
        summary.to_csv(dst_fil)



def aggregate_df():
    """
    make one dataframe with all the data
    """

    # establish data frame for coregistered
    all = pd.DataFrame()
    all["country"] = list_countries()

    for country in list(all["country"]):

        # identify the row in the dataframe
        print(country)
        row = all[all['country'] == country].index
        print("row = " + str(row))

        # look through all the source files
        src_fol = os.path.join("code", "data")
        for fil in os.listdir(src_fol):

            # retrieve the dataframe
            #print(fil)
            src_fil = os.path.join(src_fol, fil)
            temp = pd.read_csv(src_fil)
            del temp["Unnamed: 0"]

            # identify column with country name
            country_column = find_col(temp, "country")
            #print(country_column)


            if country not in list(temp[country_column]): continue

            row_src = temp[temp[country_column] == country].index
            print("row_src = " + str(row_src))

            #tempi = temp[temp[country_column] == country]
            #assert len(list(tempi[country_column])) == 1
            #print(tempi)

            #print(all[all["country"] == country])

            for name in temp.columns:

                dst_col_name = str(fil + "--" +  str(name))

                if dst_col_name not in all.columns:
                    all[dst_col_name] = [None]*len(list(all["country"]))

                print(name)
                print("row = " + str(row))
                print("value = ")
                value = list(temp[name].iloc[row_src])
                print(value)
                all[dst_col_name].iloc[row] =  value

            all.sort_values(by=["country"], ascending=False)

            # save summary df
            dst_fol = os.path.join("code", "summary")
            print(dst_fol)
            if not os.path.exists(dst_fol): os.makedirs(dst_fol)
            all.to_csv(os.path.join(dst_fol, "all.csv"))


def find_col(df, term):
    """
    return name of country column
    """

    for name in df.columns:

        if term in str(name).lower():
            #print(name)
            return(name)




def build_json(dst_fil):
    """
    return json
    """

    # establish empy dictionary and dataframe
    a, df = {}, []


    for country in list_countries():

        print(country)

        aa, dfi = add_keys(country)

        df = df.append(dfi)

        a[country] = aa

    return(a, df)


def json_to_df(js):
    """
    return df from json
    """
    df = pd.DataFrame.from_dict(pd.json_normalize(js), orient='columns')

    print(df)
    return(df)


def add_keys(country):
    """
    build nested json for each country
    """

    aa= {}

    src_fol = os.path.join("code", "data")
    for fil in os.listdir(src_fol):

        print(fil)
        src_fil = os.path.join(src_fol, fil)
        df = pd.read_csv(src_fil)
        del df["Unnamed: 0"]

        columns = df.columns

        for name in df.columns:

            if "country" in name.lower():

                dfi = df[df[name] == country]

                if len(dfi[name]) < 1: continue

                i_dict = {}
                for namei in dfi.columns:

                    i_dict[namei] = list(dfi[namei])[0]

                aa[fil.split(".")[0]] = i_dict

    print(aa)
    return(aa, dfi)


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
