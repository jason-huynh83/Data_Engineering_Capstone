# DROP TABLES
us_demo_drop = 'DROP TABLE IF EXISTS us_demo'
I94_immigration_table_drop = 'DROP TABLE IF EXISTS I94_immigration_table'
airport_code_table_drop = 'DROP TABLE IF EXISTS airport_code_table'
global_temp_city_drop = 'DROP TABLE IF EXISTS global_temp_city'
global_temp_country_drop = 'DROP TABLE IF EXISTS global_temp_country'
global_temp_major_city_drop = 'DROP TABLE IF EXISTS global_temp_major_city'
global_temp_by_state_drop = 'DROP TABLE IF EXISTS global_temp_by_state'
global_temp_drop = 'DROP TABLE IF EXISTS global_temp'

# CREATE TABLES
us_demo_table = ("""CREATE TABLE IF NOT EXISTS us_demo (
                  City VARCHAR,
                  State VARCHAR,
                  Median_age FLOAT,
                  Male_Population FLOAT,
                  Female_Population FLOAT,
                  Total_Population INT,
                  Num_of_vets FLOAT,
                  Foreign_born FLOAT,
                  Avg_household_size FLOAT,
                  State_code VARCHAR,
                  Race VARCHAR,
                  Count INT
                  )
""")

I94_immigration_table = ("""CREATE TABLE IF NOT EXISTS I94_immigration_table (
                            cicid FLOAT,
                            i94yr FLOAT,
                            i94mon FLOAT,
                            i94cit FLOAT,
                            i94res FLOAT,
                            i94port VARCHAR,
                            arrdate FLOAT,
                            i94mode FLOAT,
                            i94addr VARCHAR,
                            depdate VARCHAR,
                            i94bir FLOAT,
                            i94visa FLOAT,
                            count FLOAT,
                            dtadfile INT,
                            visapost VARCHAR,
                            occup VARCHAR,
                            entedepd VARCHAR,
                            entdepu FLOAT,
                            matflag VARCHAR,
                            biryear FLOAT,
                            dtaddto VARCHAR,
                            gender VARCHAR,
                            insnum FLOAT,
                            airline VARCHAR,
                            admnum FLOAT,
                            fltno VARCHAR,
                            visatype VARCHAR
                            )
""")

airport_code_table = ("""CREATE TABLE IF NOT EXISTS airport_code (
                         ident VARCHAR,
                         type VARCHAR,
                         type VARCHAR,
                         name VARCHAR,
                         elevation_ft FLOAT,
                         continent VARCHAR,
                         iso_country VARCHAR,
                         iso_region VARCHAR,
                         municipality VARCHAR,
                         gps_code VARCHAR,
                         iata_code VARCHAR,
                         local_code VARCHAR
                         coordinates VARCHAR
                         )
""")

global_temp_city_table = ("""CREATE TABLE IF NOT EXISTS global_temp_city (
                       dt VARCHAR,
                       AverageTemperature FLOAT,
                       AverageTemperatureUncertainty FLOAT,
                       City VARCHAR,
                       Country VARCHAR,
                       Latitude VARCHAR,
                       Longitude VARCHAR
                       )
""")

global_temp_country_table = ("""CREATE TABLE IF NOT EXISTS global_temp_country (
                          dt VARCHAR,
                          AverageTemperature FLOAT,
                          AverageTemperatureUncertainty FLOAT,
                          Country VARCHAR
                          )
""")

global_temp_major_city_table = ("""CREATE TABLE IF NOT EXISTS global_temp_major_city (
                             dt VARCHAR,
                             AverageTemperature FLOAT,
                             AverageTemperatureUncertainty FLOAT,
                             City VARCHAR,
                             Country VARCHAR,
                             Latitude VARCHAR,
                             Longitude VARCHAR
                             )
""")

global_temp_by_state_table = ("""CREATE TABLE IF NOT EXISTS global_temp_state (
                           dt VARCHAR,
                           AverageTemperature FLOAT,
                           AverageTemperatureUncertainty FLOAT,
                           State VARCHAR,
                           Country VARCHAR
                           )
""")

global_temp_table = ("""CREATE TABLE IF NOT EXISTS global_temp (
                  LandAverageTemperature VARCHAR,
                  LandAverageTemperatureUncertainty FLOAT,
                  LandMaxTemperature FLOAT,
                  LandMinTemperature FLOAT,
                  LandMinTemperatureUncertainty FLOAT,
                  LandAndOceanAverageTemperature FLOAT,
                  LandAndOceanTemperatureUncertainty FLOAT
                  )
""")
# QUERY LISTS

create_table_queries = [us_demo_table, I94_immigration_table, airport_code_table, global_temp_city_table, global_temp_country_table, global_temp_major_city_table, global_temp_by_state_table, global_temp_table]
drop_table_queries = [us_demo_drop, I94_immigration_table_drop, airport_code_table_drop, global_temp_city_drop, global_temp_country_drop, global_temp_major_city_drop, global_temp_by_state_drop, global_temp_drop]

copy_table_queries = [staging_events_copy, staging_songs_copy]
## Facts and Dimension tables
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
