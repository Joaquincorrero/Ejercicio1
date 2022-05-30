# Definimos el DataFrame
import pandas as pd
name = ["800", "110", "208", "Atlas", "Mustang", "C500", "Prius", "Landcruiser", "Accord", "C200", "Corrolla"]
company = ["BMW", "Bugatti", "Peugeot", "Volkswagen", "Ford", "Mercedes", "Toyota", "Toyota", "Honda", "Mercedes",
           "Toyota"]
power = [8000, 8000, 5400, 5000, 5000, 5000, 3200, 3000, 2000, 2000, 1800]
df = pd.DataFrame(list(zip(name,company, power)), columns = ['Name','Company', 'Power'])
print(df)

# Pasamos de DataFrame a spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Windowing_pyspark").getOrCreate()
df=spark.createDataFrame(df)

# Realizamos el ejercicio de windowing incluyendo 3 tablas en las que se mostrarán rank, dense_rank y row_number,
# respectivamente.

rank=df.select("name", "company", "power")
rank.show()