import pandas
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

colors = data["Primary Fur Color"].unique()
count = []
for color in colors:
    count.append(len(data[data["Primary Fur Color"] == color]))

data_dict = {
    "Primary Fur Color": colors,
    "Count": count
}

df = pd.DataFrame(data_dict)
df = df.dropna()
df.to_csv("squirrel_count.csv")


# import csv
#
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
#     print(temperatures)

#
# data = pd.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)

# print(data['temp'].mean())
# print(data.temp.max())
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp = monday_temp * 9/5 + 32
# print(monday_temp)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }
#
# df = pd.DataFrame(data_dict)
# print(df)