# Udacity Data Engineering Nanodegree Capstone Project
## Introduction
For the Udacity Data Engineering Capstone project, I developed an end-to-end ETL pipeline that creates a database for analytical queries on immigration into the US on a monthly basis. The analytical tables are hosted on a Amazon Web Services (AWS) Redshift database.

## Datasets
The following datasets are included in the project workspace. We purposely did not include a lot of detail about the data and instead point you to the sources. This is to help you get experience doing a self-guided project and researching the data yourself. If something about the data is unclear, make an assumption, document it, and move on. Feel free to enrich your project by gathering and including additional data sources.

-   **I94 Immigration Data:**  This data comes from the US National Tourism and Trade Office. A data dictionary is included in the workspace.  [This](https://travel.trade.gov/research/reports/i94/historical/2016.html)  is where the data comes from. There's a sample file so you can take a look at the data in csv format before reading it all in. You do not have to use the entire dataset, just use what you need to accomplish the goal you set at the beginning of the project.
-   **World Temperature Data:**  This dataset came from Kaggle. You can read more about it  [here](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data).
-   **U.S. City Demographic Data:**  This data comes from OpenSoft. You can read more about it  [here](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/).
-   **Airport Code Table:**  This is a simple table of airport codes and corresponding cities. It comes from  [here](https://datahub.io/core/airport-codes#data).

## Data Model
## Setup
- Create a Redshift Database to host your analytical tables
- Run create_tables.py to ensure the necessary tables
- Enter necessary information in capstone.cfg
 ~~~
[CLUSTER]
HOST=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_PORT= 

[IAM_ROLE]
ARN=''

[S3]
airport_data ='s3://capstonebucketdata/airport_data_cleaned.csv'
us_demo_data = 's3://capstonebucketdata/us_demo_clean.csv'
global_temp_data = 's3://capstonebucketdata/global_temp_clean.csv'
immigration_data = 's3://capstonebucketdata/immigration_data_cleaned.csv'
i94addr_data = 's3://capstonebucketdata/i94addr.csv'
i94cit_res_data = 's3://capstonebucketdata/i94cit_res.csv'
i94mode_data = 's3://capstonebucketdata/i94mode.csv'
i94port_data = 's3://capstonebucketdata/i94port.csv'
i94visa_data = 's3://capstonebucketdata/i94visa.csv'


~~~
- Explore the data using Capstone Projecy.ipynb

