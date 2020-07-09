#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Dependencies and Setup
import pandas as pd 
import numpy as np 

# File to Load 
file_to_load_json = "raw_data/purchase_data.json"

#Read purchasing file and store into pandas data frame 
purchase_data = pd.read_json(file_to_load_json, orient="records")


# In[ ]:


#Calculate the number of players 
player_demographics = purchase_data.loc[:,["Gender", "SN","Age" ]]
Player_demographics = purchase_demographics.drop_duplicates()
num_players = player_demographics.count()[0]

#Total number of players
pd.DataFrame ({"Total Players": [num_players]})


# In[ ]:


# Run basic information
average_item_price = purchase_data["Price"].mean()
total_purchase_value = purchase_data["Price"].sum()
purchase_count = purchase_data["Price"].count()
item_count = len(purcahse_data["Item ID"].unique())

#Dataframe to hold results
summary_table = pd.DataFrame({"Number of Unique Items": item count,
                             "Total Revenue":[total_purchase_value],
                             "Number of Purchases": [purchase_count],
                             "Average Price": [average_item_price]})
#Minor Data
summary_table = summary_table.round(2)
summary_table ["Average Price"] = summary_table["Average Price"].map("${:,.2f}".format)
summary_table ["Number of Purchases"] = summary_table["Number of Purchases"].map("{:,}".format)
summary_table ["Total Revenue"] = summary_table["Total Revenue"].map("${:,.2f}".format)
summary_table = summary_table.loc[:,"Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"]

#Display the summary_table 
summary_table


# In[ ]:


#Number and Percentage by Gender
gender_demographics_totals = player_demographics["Gender"].value_counts()
gender_demographics_percents = gender_demographics_totals / num_players * 100
gender_demographics = pd.DataFrame({"Total Count": gender_demographics_totals, "Percentage of Players": gender_demographics_percents})

#Minor data
gender_demographics = gender_demographics.round(2)
gender_demographics["Percentage of Players"] = gender_demographics["Percentage of Players"].map(""{:,.2f}%.format)

gender_demographics


# In[ ]:


#Run basic information
gender_purchase_total = purchase_data.groupby(["Gender"]).sum()["Price"].rename("Total Purchase Value")
gender_average = purchase_data.groupby(["Gender"]).mean()["Price"].rename("Average Purchase Price")
gender_counts = purcahse_data.groupby(["Gender"]).count()["Price"].rename("Purchase Count")

#Normalize Purchasing 
normalized_total = gender_purchase_total / gender_demographics["Total Count"]

#Convert to data frame 
gender_data = pd.DataFrame({"Purchase Count": gender counts, "Average Purchase Price": gender_average, "Total Purchase Price": gender_purchase_total, "Normalized Totals": normalized_totals})

#minor data
gender_data["Average Purchase Price"] = gender_data["Average Purchase Price"].map("${:,.2f}".format)
gender_data["Total Purchase Value"] = gender_data["Total Purchase Value"].map("${:,.2f}".format)
gender_data["Purchase Count"] = gender_data["Purchase Count"].map("{:,}".format)
gender_data["Normalized Totals"] = gender_data["Normalized Totals"].map("${:,.2f}".format)
gender_data = gender_data.loc[:, ["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Purchase Count", "Normalized Totals"]]

#The Gender Table
gender_data


# In[ ]:


#Establish the bins
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#Existing players using the age bins
player_demographics["Age Ranger"] = pd.cut(player_demographics["Age"], age_bins, labels=group_names)

#Numbers and Percentages by age group 
age_demographics_totals = player_demographics["Age Ranges"].value_counts()
age_demographics_percents = age_demographics_totals / num_players * 100
age_demographics = pd.DataFrame ({"Total Count": age_demographics_totals, "Percentage of Players": age_demographics_percent})

#Minor data
age_demographics = age_demographics.round(2)
age_demogrpahics["Percenatge of Player"] = age_demographics["percentage of players"].map

#Age demographics table 
age_demogrpahics.sor_index()


# In[ ]:


#The Purchasing data
purcahse_data["Age Ranges"] = pd.cut(purchase_data["Age"], age_bins, labels=group_names)

#Run Basic information
age_purchase_total = purchase_data.groupby(["Age Ranges"]).sum()["Price"].rename("Total Purchase Value")
age_average = purcahse_data.groupby(["Age Ranges"]).mean()["Price"].rename("Average Purchase Price")
age_counts = purchase_data.groupby(["Age Ranges"]).count()["Price"].rename("Purchase Count")

#Normalized Purchasing
normalized_total = age_purchase_total / age_demographics["Total Count"]

#Convert to Dataframe 
age_data = pd.DataFrame ({"Purchase Count": age_counts, "Average Purcahse Price": age_average, "Total Purchase Value": average_purchase_total})

#Minor data
age_data["Average Purchase Price"]= age_data["Average Purchase Price"].map("${:,.2f}".format)
age_data["Total Purchase Value"]= age_data["Total Purchase Value"].map("${:,.2f}".format)
age_data["Purchase Count"]= age_data["Purchase Count"].map("{:,}".format)
age_data["Normalized Totals"]= age_data["Normalized Totals"].map("${:,.2f}".format)
age_data = age_data.loc[:,["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]

#The Age Table 
age_data

