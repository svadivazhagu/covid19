#Retriever app that scrapes the NYT csv for corona for 3 categories.
import requests as re

if __name__ == "__main__":  
    mapping = {'country': re.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'),
     'states' : re.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'),
     'counties' : re.get('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')}


for i in mapping.keys():
    with open ('data/'+i+'.csv', 'wb') as f:
        f.write(mapping[i].content)
    print(i + ' downloaded.')
