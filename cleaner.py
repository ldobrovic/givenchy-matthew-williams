import pandas as pd
import numpy as np
import re

df = pd.read_csv("empyre.csv")
df = df.drop(["Unnamed: 0"], 1)

df_total = df.groupby("Date")
print(df.head())


def month_switch(number):
    switcher = {
        1: "May '20",
        2: "April '20",
        3: "March '20",
        4: "February '20",
        5: "January '20",
        6: "December '19",
        7: "November '19",
        8: "October '19",
        9: "September '19",
        10: "August '19",
        11: "July '19" }
    return switcher.get(number)

def year_switch(number):


counter = 0
for row in df.iterrows():
    date = df.at[counter, "Date"]
    if "days" in date:
        df.at[counter, "Month"] = "June '20"
    if "month" in date:
        matches = re.findall(r'\d+', date)
        if len(matches) != 0:
            df.at[counter, "Month"] = month_switch((int(matches[0])))
        else:
            df.at[counter, "Month"] = month_switch(1)

    counter +=1
    # print(date)

print(df.to_string())


df_data = pd.DataFrame(columns=["No. Sales", "GMV", "AV"])




