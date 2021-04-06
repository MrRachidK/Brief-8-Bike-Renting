# Import of all the libraries we need to analyze the data
import pandas as pd
import separator as sp

### 1 - Import and informations provided by the database ###

# Import of the database
vlib_analyze = pd.read_csv('data/01_raw/vlib.csv')

# Some infos about the database (columns and shape of database)
print('Nous étudions une base de données de {} lignes et de {} colonnes.'.format(vlib_analyze.shape[0], vlib_analyze.shape[1]))
sp.separator()
print('Voici la liste des colonnes de notre base de données : {}'.format(vlib_analyze.columns.tolist()))
sp.separator()

# Display of the five first entries of the database
print(vlib_analyze.head())
sp.separator()

# Some comments about the database :
# - Id type is object whereas vendor_id type is int
# - Columns pickup_datetime and dropoff_datetime are stored as objects which must be converted to DateTime
# - Column store_and_fwd_flag is stored as object

### 2 - Let's check the columns ###

# Check if there are missing values in the columns

for i in vlib_analyze.columns.tolist():
    part_missing_values = (vlib_analyze[i].isnull().sum() / vlib_analyze.shape[0]) * 100
    print('Dans la colonne {}, nous avons {} % de valeurs manquantes'.format(i, part_missing_values))
sp.separator()

### 3 - Let's check the duplicated entries ###

print(vlib_analyze.duplicated().value_counts()) # Output : 'False 10000', so there are no perfect duplicated entries
sp.separator()

### 4 - Let's check the missing values ###

# We checked previously that there are no missing values in each column, so we can move on to the next step

### 5 - Let's analyze the types of our datas

# Display of all the types of each variable
print(vlib_analyze.dtypes)
sp.separator()

# Conversion of the pickup_datetime and dropoff_datetime columns into datetime data type
vlib_analyze['datetime'] = pd.to_datetime(vlib_analyze['datetime'])
print(vlib_analyze.dtypes)

vlib_analyze['datetime_hour'] = vlib_analyze['datetime'].apply(lambda x : str(x)[11:13])
vlib_analyze['datetime_hour'] = vlib_analyze['datetime_hour'].apply(lambda x : int(x))

vlib_analyze['datetime_month'] = vlib_analyze['datetime'].apply(lambda x : str(x)[5:7])
vlib_analyze['datetime_month'] = vlib_analyze['datetime_month'].apply(lambda x : int(x))
print(vlib_analyze.tail(24))

### 6 - Let's analyze the relevance of our database ###

cleaned_vlib_analyze = vlib_analyze[['datetime', 'season', 'holiday', 'workingday', 'weather', 'temp', 'atemp', 'humidity', 'windspeed', 'count', 'datetime_hour', 'datetime_month']]
register_vlib_analyze = cleaned_vlib_analyze.to_csv('data/01_raw/cleaned_vlib.csv')