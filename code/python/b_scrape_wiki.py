from bs4 import BeautifulSoup # library to parse HTML documents
import json
import numpy as np
import os
import pandas as pd # library for data analysis
import requests # library to handle requests


def scrape_wiki():
    """

    Introducing python webscraping of Wikipedia
    https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/



    """

    print("scraped wiki for data")

    # urls saved in a .csv
    urls = retrieve_urls()

    # retrieve the title and table for each url
    for url in retrieve_urls():

        print(url)
        response = requests.get(url=url,)
        print(response.status_code)

        # parse data from the html into a beautifulsoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find(id="firstHeading")
        print(title.string)

        indiatable=soup.find('table',{'class':"wikitable"})

        df=pd.read_html(str(indiatable))

        # convert list to dataframe
        df=pd.DataFrame(df[0])
        print(df.head())

        for name in df.columns:
            print(name)
            if "country" in str(name).lower():

                for i in range(len(df[name])):

                    country_name = str(df.loc[i, name])

                    if " *" in country_name:
                        country_name = country_name.replace(" *", "")


                    df.loc[i, name] = country_name







        # save data as a csv
        dst_fol = os.path.join("code", "data")
        if not os.path.exists(dst_fol): os.makedirs(dst_fol)

        # prepare filename without spaces
        # all lowercase
        chars = [" ", "(", ")"]
        filename = str(title.string)
        for char in chars:
            filename = filename.replace(char, "_").lower()

        # save data as a dataframe
        dst_fil = os.path.join(dst_fol, filename + ".csv")
        print(dst_fil)
        df.to_csv(dst_fil)




    """
    response = requests.get(url="https://en.wikipedia.org/wiki/Web_scraping",)
    print(response.status_code)

    # code of 200 means page found
    if response.status_code != 200: return()

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.string)

    # get the response in the form of html
    wikiurl="https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
    table_class="wikitable sortable jquery-tablesorter"
    response=requests.get(wikiurl)
    print(response.status_code)

    # parse data from the html into a beautifulsoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    indiatable=soup.find('table',{'class':"wikitable"})

    df=pd.read_html(str(indiatable))
    # convert list to dataframe
    df=pd.DataFrame(df[0])
    print(df.head())

    # drop the unwanted columns
    data = df.drop(["Rank", "Population(2001)"], axis=1)
    # rename columns for ease
    data = data.rename(columns={"State or union territory": "State","Population(2011)[3]": "Population"})
    print(data.head())
    """

    print("scraped wiki for data")



def retrieve_urls():
    """
    return list of urls
    """
    src_fil = os.path.join("urls" + ".csv")
    df = pd.read_csv(src_fil)
    urls = list(df.iloc[:,-1])
    print(urls)
    return(urls)



def list_record_path():
    """
    list paths to all records as a list
    """

    src = os.path.join("studies")
    print("src = " + str(src))
    for study in os.listdir(src):
        #print(study)

        record_paths = []

        recs = os.path.join(src, study, "user_provided")
        for rec in os.listdir(recs):
            #print(rec)
            record_path = os.path.join(recs, rec)
            record_paths.append(record_path)

            rec_json = {}

            # assign the record a name
            rec_name = str(study) + str(len(record_paths)).zfill(3)
            print(rec_name)

            for fil in os.listdir(record_path):
                print(fil)

                fil_src = os.path.join(record_path, fil)

                if "TEMP" not in fil: continue

                sensor = fil.split(".")[0]

                df = pd.read_csv(fil_src)
                rec_json[sensor] = build_temp(df)


            rec_json['name'] = rec_name.split(".")[0]

            fol_json = os.path.join(src, study, "json")
            if not os.path.exists(fol_json): os.makedirs(fol_json)
            fil_json = os.path.join(fol_json, rec_name + ".json")
            with open(fil_json, 'w', encoding='utf-8') as outfile:
                json.dump(rec_json, outfile, ensure_ascii=False, indent=4)

    return(record_paths)


def build_temp(df):
    """
    return json describing temperature information
    """

    # define intial time
    #time_begin = str(round(float(df.columns[0])))
    #print(time_begin)

    # list all temperatures
    #temps = list(df[df.columns[0]])
    #int = temps[0]
    #temps = temps[1:]
    #print(temps)

    temp_json = timestamp(df)


    #temp_json["max"] = max(temps)
    #temp_json["min"] = min(temps)
    #temp_json["mean"] = round(np.mean(temps), 2)
    #temp_json["median"] = np.median(temps)

    #
    #mins = timestamp(temps, time_begin, int)
    #temp_json["polyfit"] = np.polyfit(mins, temps)
    #temp_json["meas"] = temps
    #temp_json["mins"] = mins
    #temp_json["dur"] = max(mins)

    return(temp_json)

def timestamp(df):
    """
    return list of time
    """

    # organize variables
    begin = df.columns[0]
    int = df[begin].iloc[0]
    meas = list(df[begin])[1:]

    # create list of minutes timestamps
    mins = []
    unis = []
    for mea in meas:
        sec = len(mins)*1/int
        min = sec/60
        min = round(min,3)
        mins.append(min)

        uni = round(sec + float(begin), 3)
        unis.append(uni)
    #times["mins"] = mins

    # establish times json
    times = {}
    times["interval"] = int
    times["begin"] = round(float(begin))
    times["end"] = max(unis)
    times["duration"] = max(mins)
    times["len"] = len(meas)

    # statistics
    times["mean"] = np.mean(meas)
    times["median"] = np.median(meas)
    times["min"] = np.min(meas)
    times["max"] = np.max(meas)

    assert len(mins) == len(meas)

    # regression analysis
    times["slope"] = list(np.polyfit(mins, meas, 1))

    # timestamped measurements
    times["mins"] = mins
    times["unix"] = unis
    times["meas"] = meas


    return(times)



if __name__ == "__main__":
    a_main()
