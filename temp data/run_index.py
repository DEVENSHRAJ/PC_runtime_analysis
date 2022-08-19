import pandas as pd
from datetime import datetime, timedelta
df = pd.read_csv('run_data_csv - per day total.csv')
print(int(df["started"][1][8:10]))
print(len(df))
#print(df["started"][1:412])
lstcl=len(df)-3
print(df["started"][lstcl])


data=[]

start_date = datetime.strptime(df["started"][1], '%Y-%m-%d , %H:%M:%S')
end_date = datetime.strptime(df["started"][lstcl], '%Y-%m-%d , %H:%M:%S')
print(start_date,end_date)
total_days=(end_date-start_date).days

current_index=1
for i in range(total_days+1):
    ths_date=start_date+timedelta(days=i)
    #runtime calculation
    org_file_date=datetime.strptime(df["started"][current_index], '%Y-%m-%d , %H:%M:%S')
    runtimehr=0
    while org_file_date.day==ths_date.day:
        runtimehr += df["total"][current_index]
        current_index+=1
        org_file_date = datetime.strptime(df["started"][current_index], '%Y-%m-%d , %H:%M:%S')
    #print(i,current_index)
    data.append([ths_date.date(),runtimehr])

print(data)


#saving to csv creation
svto=pd.DataFrame(data,columns=['date', 'total runtime'])

svto.to_csv('per day runtime_py filtered.csv', index=False)
