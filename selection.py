# import pandas as pd
#
# df = pd.read_csv("data.csv", index_col="Name")

# Selection by column

# print(df["Name"].to_string())

# print(df[["Name", "Height", "Weight"]])

# Selection by rows

# selecting range of rows and choosing columns

# print(df.loc["Charizard":"Pikachu", ["Height", "Weight"]])

# print(df.iloc[0:11:2, 0:3])

# # User input
#
# pokemon = input("Enter a Pokemon name: ")
#
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} is not found!")











