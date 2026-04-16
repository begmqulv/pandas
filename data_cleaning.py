# import pandas as pd

# # Data cleaning = the process of fixing/removing:
# # incomplete, incorrect and irrelevant data.
# # ~75% of work done with Pandas is data cleaning

# df = pd.read_csv("data.csv")

# # 1. Dropping irrelevant columns

# df = df.drop(columns=["Legendary","No"])

# # 2. Handling the missing data

# df = df.dropna(subset=["Type2"]) # removing the row missing data

# df = df.fillna({"Type2": "None"}) # filling the row missing data

# # 3. Fix inconsistent values

# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                    "Fire": "FIRE",
                                   # "Water": "WATER"})

# # 4. Standartize text
# df["Name"] = df["Name"].str.lower()

# # 5. Fix data types

# df["Legendary"] = df["Legendary"].astype(bool)

# # 6. Remove duplicate values

# df = df.drop_duplicates()

# print(df.to_string())