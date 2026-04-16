# import pandas as pd

# # aggregate functions = Reduces a set of values into a single summary value
# # Used to summarize and analyze data
# # Ofter used with groupby() function

# df = pd.read_csv("data.csv")

# # Whole dataframe
#
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# # Single dataframe
#
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())


# # Grouping

# group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())



















