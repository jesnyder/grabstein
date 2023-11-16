import json
import os

#from admin import list_record_path
from b_scrape_wiki import scrape_wiki
from c_coregister_df import coregister_df
from d_format_json import format_json

def a_main():
    """

    """

    print("running main")

    # tasks for program to run
    # 1 scrape information from wikipedia
    # 2 coregister the information
    tasks = [3]

    # scrape information from wikipedia
    if 1 in tasks: scrape_wiki()

    # coregister information
    if 2 in tasks: coregister_df()

    # format json for Chart.JS
    if 3 in tasks: format_json()


    print("completed main")



if __name__ == "__main__":
    a_main()
