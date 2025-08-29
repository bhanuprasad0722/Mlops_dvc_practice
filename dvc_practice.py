import pandas as pd 
import os 

data = {
    'Name' : ['Bhanu','Vikas','Hemanth'],
    'Age' : [23,22,21],
    'City' : ['Hyd','Hyd','Mumbai']
}

df = pd.DataFrame(data)
# adding new data 1
new_row = {'Name':'Kiran','Age':27,'City':'Chennai'}
df.loc[len(df.index)] = new_row
# adding new data 2
new_row_2 = {'Name':'Nandu','Age':22,'City':'Amaravathi'}
df.loc[len(df.index)] = new_row_2
data_dir = 'Data'
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,'Sample_data.csv')
df.to_csv(file_path,index=False)

print(f"sample data created at location {file_path}")
