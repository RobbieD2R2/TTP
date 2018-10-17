from matplotlib import pyplot as plt

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()



# from matplotlib import pyplot as plt
# from matplotlib import style

# style.use('ggplot')

# x = [5,8,10]
# y = [12,16,6]

# x2 = [6,9,11]
# y2 = [6,15,7]


# plt.bar(x, y, align='center')

# plt.bar(x2, y2, color='g', align='center')


# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# plt.show()




# from matplotlib import pyplot as plt
# from matplotlib import style

# style.use('ggplot')

# x = [5,8,10]
# y = [12,16,6]

# x2 = [6,9,11]
# y2 = [6,15,7]

# plt.scatter(x, y)

# plt.scatter(x2, y2, color='g')


# plt.title('Epic Info')
# plt.ylabel('Y axis')
# plt.xlabel('X axis')

# plt.show()





# import pandas as pd
# import matplotlib.pyplot as plt

# raw_data = {'officer_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
#         'jan_arrests': [4, 24, 31, 2, 3],
#         'feb_arrests': [25, 94, 57, 62, 70],
#         'march_arrests': [5, 43, 23, 23, 51]}
# df = pd.DataFrame(raw_data, columns = ['officer_name', 'jan_arrests', 'feb_arrests', 'march_arrests'])
# df


# # Create a column with the total arrests for each officer
# df['total_arrests'] = df['jan_arrests'] + df['feb_arrests'] + df['march_arrests']
# df


# # Create a list of colors (from iWantHue)
# colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

# # Create a pie chart
# plt.pie(
#     # using data total)arrests
#     df['total_arrests'],
#     # with the labels being officer names
#     labels=df['officer_name'],
#     # with no shadows
#     shadow=False,
#     # with colors
#     colors=colors,
#     # with one slide exploded out
#     explode=(0, 0, 0, 0, 0.15),
#     # with the start angle at 90%
#     startangle=90,
#     # with the percent listed as a fraction
#     autopct='%1.1f%%',
#     )

# # View the plot drop above
# plt.axis('equal')

# # View the plot
# plt.tight_layout()
# plt.show()