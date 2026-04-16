# import pandas as pd
#
# data = {"Name": ["Abdishukr", "Ali", "Vali"],
#         "Age": [18, 19, 20]}
#
# df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])
#
# # print(df.loc[0]) # accessing a valur directly
#
# df["Job"] = ["Ceo", "Cook", "Runner"] # adding a column
#
# new_rows = pd.DataFrame([{"Name": "Josh", "Age": 16, "Job": "Printer"},
#                         {"Name": "Robert", "Age": 28, "Job": "Lawyer"}],
#                        index=["Employee 4", "Employee 5"]) # creating new element
#
# df = pd.concat([df, new_rows])
#
# print(df)
