# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:09:43 2020

@author: User
"""
#importing necessary libraries
import pandas as pd

file_path = 'C:\\Users\\User\\Documents\\School\\code\\UDACITY\\Udacity-Data-Engineering-Projects\\Data_Engineering_Capstone\\'

########################################################################################################
#                              STEP 1 Scope of the Project and Gather Data
""" For this project, I will be demonstrating various skills associated with the data engineering projects. 
    In particular, developing ETL pipelines using Airflow, constructing data warehouses through Redshift databases,
    and S3 data storage as well as defining efficient data models (e.g. Star Schema). As an example I will perform a 
    deep dive into US immigration, primarily focusing on _______ and _______. The scope of the project is accomplished with the following
    data sources below being aggregated."""
########################################################################################################
   
#reading all necessary files    
us_demo = pd.read_csv(file_path+'us-cities-demographics.csv')
I94_immigration_data = pd.read_csv(file_path+'immigration_data_sample.csv')
airport_code_table = pd.read_csv(file_path+'airport-codes_csv.csv')
global_temp_city = pd.read_csv(file_path+'GlobalLandTemperaturesByCity.csv')
global_temp_country = pd.read_csv(file_path+'GlobalLandTemperaturesByCountry.csv')
global_temp_major_city = pd.read_csv(file_path+'GlobalLandTemperaturesByMajorCity.csv')
global_temp_by_state = pd.read_csv(file_path+'GlobalLandTemperaturesByState.csv')
global_temp = pd.read_csv(file_path+'GlobalTemperatures.csv')
I94_sas = pd.read_sas(file_path+'I94_SAS_Labels_Descriptions.sas')

#renaming column to data
us_demo = us_demo.rename(columns={"""City;State;Median Age;Male Population;Female Population;Total Population;
                                  Number of Veterans;Foreign-born;Average Household Size;State Code;Race;Count""":'data'})

#parse out data in u.s. city demographics into separate columns
us_demo['City'] = us_demo['data'].apply(lambda x: x.split(';')[0])
us_demo['State'] = us_demo['data'].apply(lambda x: x.split(';')[1])
us_demo['Median Age'] = us_demo['data'].apply(lambda x: x.split(';')[2])
us_demo['Male Population'] = us_demo['data'].apply(lambda x: x.split(';')[3])
us_demo['Female Population'] = us_demo['data'].apply(lambda x: x.split(';')[4])
us_demo['Total Population'] = us_demo['data'].apply(lambda x: x.split(';')[5])
us_demo['Number of Veterans'] = us_demo['data'].apply(lambda x: x.split(';')[6])
us_demo['Foreign-born'] = us_demo['data'].apply(lambda x: x.split(';')[7])
us_demo['Average Household Size'] = us_demo['data'].apply(lambda x: x.split(';')[8])
us_demo['State code'] = us_demo['data'].apply(lambda x: x.split(';')[9])
us_demo['Race'] = us_demo['data'].apply(lambda x: x.split(';')[10])
us_demo['Count'] = us_demo['data'].apply(lambda x: x.split(';')[11])

########################################################################################################
#                              STEP 2 Explore and Assess the Data

df_clean_I94_immigration_data = I94_immigration_data.isnull()
I94_immigration_data.columns
airport_code_table.info()







