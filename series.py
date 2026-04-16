# import pandas as pd

# # Series = A Pandas 1 - Dimensional labeled array that can hold any data type
# # Single column in a spreadsheet (1-Dimensional)

# data1 = [1, 10, 100]
# data2 = [1.1, 10.1, 100.1]
# data3 = ["A", "B", "C"]
# data4 = [True, False, True]
#
# series1 = pd.Series(data1)
# series2 = pd.Series(data2)
# series3 = pd.Series(data3)
# series4 = pd.Series(data4)
#
# print(series1)
# print(series2)
# print(series3)
# print(series4)

# data = [1, 10, 100]

# series = pd.Series(data, index=["a", "b", "c"]) # changing the index

# print(series)

# print(series.loc["a"]) # accessing to value directly

# print(series.iloc[0]) # accessing to value by indexk

# series.loc["a"] = 200 # changing the value

# # filtering

# data = [1, 10, 100, 202, 204]
#
# series = pd.Series(data, index=["a", "b", "c", "d", "e"])
#
# print(series[series >= 200])
#
# print(series[series <= 200])

# # dictionaries

# calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 2100}
#
# series = pd.Series(calories)
#
# print(series)
