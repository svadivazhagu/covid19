#This file is designed for cleaning the extracted CSVs from the SQlite database.
import pandas as pd


def choropleth_prep(fp):
    '''
    Modifies the file f to be in line with the format for the Choropleth D3.js map
        0+fips, confirmed_deaths/confirmed_cases
    :param f:
    :return: cleaned dataframe.
    '''
    df =  pd.read_csv(fp)
    df.insert(4, 'death_rate', 0.0)
    for i, row in df.iterrows():
        cases, deaths, death_rate = row[2], row[3], 0.0
        if cases == 0 or deaths == 0:
            death_rate = 0.0
        else:
            death_rate = round((deaths / cases * 100), 2 )
        df.at[i, 'death_rate'] = death_rate
    df.to_csv('data/cleaned/cleaned_counties.csv', index=False)




if __name__ == '__main__':
    choropleth_prep('data/extracted/counties.csv')


