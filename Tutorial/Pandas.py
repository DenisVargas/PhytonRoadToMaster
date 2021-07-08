#Es una herramienta de alto nivel que permite visualizar data usando una estructura llamada DataFrame.
#Utiliza NumPy
#Dataframes nos permite manipular data tabular en filas y columnas
#https://www.learnpython.org/en/Pandas_Basics

#Example Using Dictionaries
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

#Supongamos que queremos cambiar los índices numéricos por algún dato personalizado.
# Set the index for brics
# brics.index = ["BR", "RU", "IN", "CH", "SA"]

# # Print out brics with new index values
# print(brics)

#Example using CSV file.
# import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('cars.csv')

# Print out cars
print(cars)

#Indexing DataFrames
#Usa [] para seleccionar une elemento utilizando su índice
# Import pandas and cars.csv
# import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
# print(cars['cars_per_cap'])

# # Print out country column as Pandas DataFrame
# print(cars[['cars_per_cap']])

# # Print out DataFrame with country and drives_right columns
# print(cars[['cars_per_cap', 'country']])


# Import cars data
# import pandas as pd
# cars = pd.read_csv('cars.csv', index_col = 0)

# # Print out first 4 observations
# print(cars[0:4])

# # Print out fifth and sixth observation
# print(cars[4:6])
