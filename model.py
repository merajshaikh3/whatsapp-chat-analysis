import pandas as pd
import re

with open('data.txt', 'r', encoding='utf-8') as f:
    data = f.read()

pattern = r"(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\sampm|\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s[ap]m) - ([^:]+): (.+)"

matches = re.findall(pattern, data)

#print(matches)

dates = [match[0] for match in matches]
users = [match[1] for match in matches]
messages = [match[2] for match in matches]

#print(dates)

df = pd.DataFrame({'date': dates, 'user': users, 'message': messages})
#print(df[['User','Message']].head())


#convert message_date type
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p')
#print(df.head())

#print(df.shape)

df['year'] = df['date'].dt.year
#print(df.head())

df['month'] = df['date'].dt.month_name()
# print(df.head())

df['day'] = df['date'].dt.day
df['hour'] = df['date'].dt.hour
df['minute'] = df['date'].dt.minute
# print(df.head())

media_message = df[df['message'] == '<Media omitted>']
# print(len(media_message))

x = df['user'].value_counts()
print(df.head())
