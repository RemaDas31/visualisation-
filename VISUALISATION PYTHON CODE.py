# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:18:42 2024

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt

# Line-plot(1st graph)


def line_plot(data, imgname='population_over_years.png'):

    
    """Creates a line graph and saves it to a file"""
    plt.figure(figsize=(12, 8))  # Sets the area to be plotted to 12 inches wide and 8 inches tall

    #specifying the countries to be plotted
    countries = ['Afghanistan', 'China', 'India', 'United States', 'United Kingdom', 'Zimbabwe', 'Mexico', 'Japan', 'Indonesia', 'France', 'Hong Kong']

    # plotting the graph
    for country in countries:
        population = data[country]
        years = data["Years"]
        plt.plot(years, population, label=country, marker='o')

    # Adding details to the graph
    plt.title('COUNTRIES POPULATION OVER YEARS')
    plt.xlabel('YEARS')
    plt.ylabel('POPULATION')
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')  # Adjusting legend position
    plt.grid(True)
    plt.xlim(1970, 2020)

    # Saving the plot to a file
    plt.savefig(imgname)

    # Displaying the plot
    plt.show()

data = pd.read_csv('Dataset.csv')  # Dataset is read
line_plot(data)

# Pie-chart(2nd graph)


def pie_chart(data, imgname='area_distribution.png'):

    
    """Creates a pie chart and saves it to a file"""
    plt.figure(figsize=(10, 8))  # Sets the area to be plotted to 10 inches wide and 8 inches tall

    # specifying the countries to be plotted
    countries = ['Afghanistan', 'China', 'India', 'United States', 'United Kingdom', 'Zimbabwe', 'Mexico', 'Japan', 'Indonesia', 'France', 'Hong Kong']

    total_area = data[countries].sum()

    # Adding details to the plot
    plt.pie(total_area, labels=countries, startangle=140)  # Plotting the pie-chart
    plt.title('Area distribution for specific Countries')

    # Saving the plot to a file
    plt.savefig(imgname)

    # Displaying the plot
    plt.show()

data = pd.read_csv('area(dataset).csv')  # Dataset is read
pie_chart(data)

# Bar-chart(3rd graph)


def bar_chart(data, imgname='growth_rate.png'):

    
    """Creates a bar chart for the mean growth rates of specified countries"""
    plt.figure(figsize=(12, 8))
    
    # Specifying the countries to be included in the bar chart
    countries = ['Afghanistan', 'China', 'United States', 'India', 'Japan', 'Mexico', 'United Kingdom', 'Zimbabwe', 'Indonesia', 'France', 'Hong Kong']
    
    # Extracting the specified columns
    growth_rates = data[countries]
    
    # Specifying different colors for each country
    colors = ['pink', 'purple', 'blue', 'green', 'orange', 'red', 'brown', 'cyan', 'magenta', 'yellow', 'gray']
    
    # Creating a bar chart with different colors for each country
    growth_rates.plot(kind='bar', color=colors, edgecolor='black')  

    # Adding details to the graph
    plt.title('Mean Growth Rates for Different Countries')
    plt.xlabel('Country')
    plt.ylabel('Mean Growth Rate')
    plt.ylim(0.01, 1.25)

    # Adjusting the legend position
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    
    # Adding space around the plot
    plt.tight_layout()
    
    # Displaying the plot
    plt.show()

data = pd.read_csv('growthrate(dataset).csv')  # Dataset is read
# Calling the function
bar_chart(data)

