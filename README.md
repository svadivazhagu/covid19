# Visualizing Covid-19
Data science projects to visualize coronavirus data. I aim to use data generated from the New York Times' data [repository](https://github.com/nytimes/covid-19-data) 
to create a queriable API using Flask. After that, a web interface for the data will be created for easy user
navigation, with data visualizations being provided alongside.

## TODO
   - organize the data to be ready for the choropleth map
   - write the choropleth map
 

## Changelog
- Update DbHandler.py with the rest of the NYT data
- Added support for cleaning the data 
    - removing the 'Unknown' counties that had no fips/name
        - `select fips, county, cases, deaths from counties where county != 'Unknown';
`
 

