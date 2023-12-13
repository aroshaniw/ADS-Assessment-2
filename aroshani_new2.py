# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 07:17:35 2023

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


# Read the CSV file into a DataFrame
def read_data(filename):
    #Read and return the data frame
    climate_data = pd.read_csv(filename, skiprows=4)

    return climate_data


def transpose_and_clean_dataset(dataframe, column, value1, value2, value3):
    # Groups data with column value
    clim_data = dataframe.groupby(column, group_keys=True)
    clim_data = clim_data.get_group(value1)
    # Resets the index
    clim_data = clim_data.reset_index()

    clim_data.set_index('Country Name', inplace=True)
    clim_data = clim_data.loc[:, value2]
    clim_data = clim_data.loc[value3, :]
    # Clean the dataframe
    clim_data = clim_data.dropna(axis=1)
    # Reset the index
    clim_data = clim_data.reset_index()

    # Transposing the index of the dataframe
    transposed_data = clim_data.set_index('Country Name')
    transposed_data = transposed_data.transpose()

    return clim_data, transposed_data


#draw Bar Plots
def barplot(val):
    val.plot.bar(x='Country Name')
    plt.legend(fontsize=10)
    plt.title('Agricultural land (sq. km)')
    # save as png
    plt.savefig("barplot1.png")
    # Display the chart
    plt.show()
    return


def barplot1(val):
    val.plot.bar(x='Country Name')
    plt.legend(fontsize=10)
    plt.title('Urban population')
    # save as png
    plt.savefig("barplot2.png")
    # Display the chart
    plt.show()
    return


#draw Line Plots
def linplot(val, title):
    val.plot.line(figsize=(50, 30), fontsize=60, linewidth=6.0)
    plt.title(title.upper(), fontsize=60)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel(title, fontsize=40)
    plt.legend(fontsize=50)
    # save as png
    plt.savefig("lineplot1.png")
    # Display the chart
    plt.show()
    return


def linplot1(val, title):
    val.plot.line(figsize=(50, 30), fontsize=60, linewidth=6.0)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel(title, fontsize=40)
    plt.legend(fontsize=50)
    # save as png
    plt.savefig("lineplot2.png")
    # Display the chart
    plt.show()
    return


def heat_map(data):
    plt.figure(figsize=(80, 40))
    sns.heatmap(data.corr(), annot=True, annot_kws={"size": 32})
    plt.title("china's Heatmap".upper(), size=40, fontweight='bold')
    plt.xticks(rotation=90, horizontalalignment="center", fontsize=50)
    plt.yticks(rotation=0, fontsize=50)
    plt.savefig('Heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()
    return data


# Read data from csv file
dataframe = read_data("climatedataset.csv")

# Creating list of countries and years for plotting bar plots and line plots
year = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
country = ['Canada', 'China', 'United Kingdom', 'United States',
           'Brazil', 'India', 'Australia', 'Germany', 'France']
column = 'Agricultural land (sq. km)'

year1 = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
country1 = ['Canada', 'China', 'United Kingdom', 'United States',
            'Brazil', 'India', 'Australia', 'Germany', 'France']
column1 = 'Urban population'


# Calling bar plot and line plot function with indicator as Agricultural land (sq. km)
clean_df, transposed_df = transpose_and_clean_dataset(
    dataframe, 'Indicator Name', column, year, country)
barplot(clean_df)
linplot(transposed_df, column)

# Calling bar plot and line plot function with indicator as Urban population
clean_df1, transposed_df1 = transpose_and_clean_dataset(
    dataframe, 'Indicator Name', column1, year, country)
barplot1(clean_df1)
linplot1(transposed_df1, column)

# Print filterd and transposed data
print(clean_df.head(10))
print(transposed_df.head(10))
print(clean_df1.head(10))
print(transposed_df1.head(10))


# Heat Map
# Reads data from csv file
world_data = read_data("climatedataset.csv")
world_data1, transdata1 = transpose_and_clean_dataset(
    world_data, 'Indicator Name', 'Urban population', country1, year1)
# Prints filtered data and transposed data
print(world_data1)
print(transdata1)
world_data2, transdata2 = transpose_and_clean_dataset(
    world_data, 'Indicator Name', 'Agricultural land (sq. km)', country1, year1)
# Prints filtered data and trasposed data
print(world_data2)
print(transdata2)


# Creating variable with years
year_heat = ['2000', '2005', '2010', '2015', '2020']
# Creating variable for heat map
indicator1 = ['Urban population (% of total population)', 'Population, total', 'CO2 emissions from liquid fuel consumption (kt)',
              'Agricultural land (sq. km)', 'Cereal yield (kg per hectare)']
data_heat = stat_data(world_data, 'Country Name',
                      'China', year_heat, indicator1)
print(data_heat.head())
#calling function heat map
heat_map(data_heat)

start = 2000
end = 2020
yeardes = [str(i) for i in range(start, end+1)]
indicator2 = ['Urban population (% of total population)', 'Population, total',
              'CO2 emissions from liquid fuel consumption (kt)', 'Agricultural land (sq. km)']
des = stat_data(world_data, 'Country Name', 'China', yeardes, indicator2)
stats_summary = des.describe()
print(stats_summary)
skewness = des['Urban population (% of total population)'].skew()
print(f'Skewness: {skewness}')
