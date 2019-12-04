import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df1=pd.read_csv("filmtv_movies.csv")
df2=pd.read_csv("boxoffice.csv")
df3=pd.merge(df1, df2, on="title")
print(df3)
print(df3['year_x'].equals(df3['year_y']))
df3['is_year_equal'] = np.where(df3['year_x']==df3['year_y'], 'yes', 'no')
print(df3['is_year_equal'])
# plt.figure()
# plt.bar(df3['filmtv_id'], df3['lifetime_gross'], align='center')
# plt.axis([0, 150000, 0, 100000000])
# # plt.xlabel("Rank")
# # plt.ylabel("Total Gross")
# # plt.title("Total Gross Plot")
# # plt.grid()
# plt.show()
df3 = sns.load_dataset("df3")
#print(sns.relplot(x="avg_vote", y="lifetime_gross", hue="title"))