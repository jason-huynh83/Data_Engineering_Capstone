# CONFIG

import configparser
config = configparser.ConfigParser()
config.read('capstone.cfg')

# DROP TABLES
us_demo_drop = 'DROP TABLE IF EXISTS us_demo'
I94_immigration_table_drop = 'DROP TABLE IF EXISTS I94_immigration_table'
airport_code_table_drop = 'DROP TABLE IF EXISTS airport_code'
global_temp_city_drop = 'DROP TABLE IF EXISTS global_temp_city'
i94cit_res_table_drop = 'DROP TABLE IF EXISTS i94cit_res'
i94port_table_drop = 'DROP TABLE IF EXISTS i94port'
i94mode_table_drop = 'DROP TABLE IF EXISTS i94mode'
i94addr_table_drop = 'DROP TABLE IF EXISTS i94addr'
i94visa_table_drop = 'DROP TABLE IF EXISTS i94visa'

# CREATE TABLES
I94_immigration_table = ("""CREATE TABLE IF NOT EXISTS I94_immigration_table (
                            cicid VARCHAR PRIMARY KEY,
                            i94yr VARCHAR,
                            i94mon VARCHAR,
                            i94cit VARCHAR,
                            i94res VARCHAR,
                            i94port VARCHAR,
                            arrdate VARCHAR,
                            i94mode VARCHAR,
                            i94addr VARCHAR,
                            depdate VARCHAR,
                            i94bir VARCHAR,
                            i94visa VARCHAR,
                            count VARCHAR,
                            visapost VARCHAR,
                            biryear VARCHAR,
                            gender VARCHAR,
                            airline VARCHAR,
                            visatype VARCHAR
                            )
""")

us_demo_table = ("""CREATE TABLE IF NOT EXISTS us_demo (
                  City VARCHAR,
                  State VARCHAR,
                  Median_age VARCHAR,
                  Male_Population VARCHAR,
                  Female_Population VARCHAR,
                  Total_Population VARCHAR,
                  Num_of_vets VARCHAR,
                  Foreign_born VARCHAR,
                  Avg_household_size VARCHAR,
                  State_code VARCHAR,
                  Race VARCHAR,
                  Count VARCHAR
                  )
""")

airport_code_table = ("""CREATE TABLE IF NOT EXISTS airport_code (
                         ident VARCHAR PRIMARY KEY,
                         type VARCHAR,
                         name VARCHAR,
                         elevation_ft VARCHAR,
                         continent VARCHAR,
                         iso_country VARCHAR,
                         iso_region VARCHAR,
                         municipality VARCHAR,
                         gps_code VARCHAR,
                         iata_code VARCHAR,
                         local_code VARCHAR,
                         Longitude VARCHAR,
                         Latitude VARCHAR
                         )
""")

global_temp_city_table = ("""CREATE TABLE IF NOT EXISTS global_temp_city (
                       dt VARCHAR,
                       AverageTemperature VARCHAR,
                       AverageTemperatureUncertainty VARCHAR,
                       City VARCHAR,
                       Country VARCHAR,
                       Longitude VARCHAR,
                       Latitude VARCHAR
                       )
""")

# INSERT RECORDS
us_demo_table_insert = ("""COPY us_demo
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['us_demo_data'], config['IAM_ROLE']['ARN'])

I94_immigration_insert = ("""COPY I94_immigration_table
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['immigration_data'], config['IAM_ROLE']['ARN'])

airport_code_insert = ("""COPY airport_code
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['airport_data'], config['IAM_ROLE']['ARN'])


global_temp_insert = ("""COPY global_temp_city
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['global_temp_data'], config['IAM_ROLE']['ARN'])
                                       

#Dimension tables 
i94cit_res_table = ("""CREATE TABLE IF NOT EXISTS i94cit_res (
                       code VARCHAR PRIMARY KEY,
                       country VARCHAR
                       )
""")
i94cit_res_copy = ("""COPY i94cit_res
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['i94cit_res_data'], config['IAM_ROLE']['ARN'])

i94port_table = ("""CREATE TABLE IF NOT EXISTS i94port (
                    code VARCHAR PRIMARY KEY,
                    port VARCHAR
                    )
""")

i94port_copy = ("""COPY i94port
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['i94port_data'], config['IAM_ROLE']['ARN'])

i94mode_table = ("""CREATE TABLE IF NOT EXISTS i94mode (
                    code VARCHAR PRIMARY KEY,
                    mode VARCHAR
                    )
""")

i94mode_copy = ("""COPY i94mode
                           FROM {}
                           IAM_ROLE {}
                           csv
                           """).format(config['S3']['i94mode_data'], config['IAM_ROLE']['ARN'])

i94addr_table = ("""CREATE TABLE IF NOT EXISTS i94addr (
                    code VARCHAR PRIMARY KEY,
                    addr VARCHAR
                    )
""")

i94addr_copy = ("""COPY i94addr
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['i94addr_data'], config['IAM_ROLE']['ARN'])

i94visa_table = ("""CREATE TABLE IF NOT EXISTS i94visa (
                    code VARCHAR PRIMARY KEY,
                    type VARCHAR
                    )
""")

i94visa_copy = ("""COPY i94visa
                           FROM {}
                           IAM_ROLE {}
                           csv;
                           """).format(config['S3']['i94visa_data'], config['IAM_ROLE']['ARN'])


# QUERY LISTS
create_table_queries = [I94_immigration_table, us_demo_table, airport_code_table, global_temp_city_table, i94cit_res_table, i94port_table, i94mode_table, i94addr_table, i94visa_table]
drop_table_queries = [us_demo_drop, I94_immigration_table_drop, airport_code_table_drop, global_temp_city_drop, i94cit_res_table_drop, i94port_table_drop, i94mode_table_drop, i94addr_table_drop, i94visa_table_drop]
copy_table_queries = [airport_code_insert, us_demo_table_insert, I94_immigration_insert,  global_temp_insert, i94cit_res_copy, i94port_copy, i94mode_copy, i94visa_copy, i94addr_copy]
