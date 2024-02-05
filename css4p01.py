#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt

# Load the movie csv file using pandas
df=pd.read_csv("movie_dataset.csv")

# Fill NAN cells in the columns with average of the column in csv file
df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace = True)
df['Metascore'].fillna(df['Metascore'].mean(), inplace = True)



# Q1
high_rating = df[df["Rating"] == df["Rating"].max()]
print("Name of the movie with high rating is ", high_rating["Title"])


# Q2
average_revenue = df['Revenue (Millions)'].mean()
print("Average revenue of all movies is", int(average_revenue), "Million")


# Q3
_2015,  _2016 = df[df['Year'] == 2015], df[df['Year'] == 2016]

rev_2015,  rev_2016 = _2015["Revenue (Millions)"], _2016["Revenue (Millions)"]

average_rev = round((rev_2015.mean() + rev_2016.mean())/2, 2)
print("Average revenue of movies done from 2015 to 2017", average_rev, "Millions")



# Q4
_2016 = df[df["Year"] == 2016]
print("The number of movies released in 2016 is", len(_2016))

# Q5
chris_n = df[df['Director'] == "Christopher Nolan"]
print("Number of movies directed by Christopher Nolan is", len(chris_n))    


# Q6
rating_over_8 = df[df["Rating"] > 7.9]     
print("Number of movies with rating at least 80.", len(rating_over_8))


# Q7
chris_rating = chris_n["Rating"]
print("Average Christopher Nolan rating is ", round(chris_rating.mean(),2))
 

# Q8

max_rating = df[df["Rating"] == df['Rating'].max()]
max_rat_year = max_rating['Year']
print("The year with maximun rating is", max_rat_year)



# Q9

_2006 = df[df['Year'] == 2006]      
perc_in = ((len(_2016) - len(_2006))/(len(_2006)))*100
print("Percentage increase from 2006 to 2016 is", int(perc_in), "%")


# Q10



# Q11



# Q12

x = df['Rating']
y = df['Revenue (Millions)']

plt.scatter(x, y)
plt.title('Revenue as a function of rating')
plt.xlabel('Rating')
plt.ylabel('Revenue [Millions]')
plt.savefig("rating_revenue.png")
plt.show()

