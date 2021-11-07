import matplotlib.pyplot as plt
from main import first_query_data, second_query_data, third_query_data

first_data = first_query_data()
second_data = second_query_data()
third_data = third_query_data()

data_battleground = first_data['Battlegrounds']
data_alliance_players = first_data['Alliance Players']

fig, ax = plt.subplots()

ax.bar(data_battleground, data_alliance_players)

ax.set_facecolor('seashell')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)
fig.set_figheight(6)

plt.show()

fig1, ax1 = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)

data = second_data["Players"]
categories = second_data["Class"]

wedges, texts = ax1.pie(data,
                        textprops=dict(color="w"),
                        colors=plt.cm.Dark2.colors,
                        startangle=140)

ax1.legend(wedges, categories, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()

data_class = third_data['Class']
data_kills = third_data['Kills']

fig2, ax2 = plt.subplots()

ax2.bar(data_class, data_kills, color='red')

ax2.set_facecolor('seashell')
fig2.set_facecolor('floralwhite')
fig2.set_figwidth(12)
fig2.set_figheight(6)

plt.show()
