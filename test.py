import pandas 
import csv

hh = pandas.read_csv('/home/dev003/Documents/Chidchanok.p.nf/Exam1.csv')
print(hh)
reader = csv.reader(hh) #List

saved_column = hh.salary

df = pandas.DataFrame(hh)
df.head()

Who_Max = df.loc[df['salary'] == max(saved_column)]
print('Who_Max', Who_Max)
Who_Min = df.loc[df['salary'] == min(saved_column)]
print('Who_Min', Who_Min)
AV = df['salary'].mean()
print('AVG', AV )

sort_by = df.sort_index(by=['name'])
print('Sort_Name', sort_by)

DD = df.groupby('name')['salary'].count()	
print('DD',DD)


