import pandas as pd
import re

def preprocess(data):

    pattern = r"(\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\sampm|\d{2}/\d{2}/\d{2}, \d{1,2}:\d{2}\s[ap]m) - ([^:]+): (.+)"

    matches = re.findall(pattern, data)

    dates = [match[0] for match in matches]
    users = [match[1] for match in matches]
    messages = [match[2] for match in matches]

    df = pd.DataFrame({'date': dates, 'user': users, 'message': messages})

    #convert message_date type
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%y, %I:%M %p')

    df['only_date'] = df['date'].dt.date #nomenclature is slightly incorrect. This is needed for creating daily activity graph. Current date column has time also in it
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    #we will create a new column called "period". It will tell us the hour range in which a message was sent
    #ex: if the message was sent at hour 10 (i.e. 10 am), the period column will indicate 10 - 11 (indicating that the message was sent in between 10 am and 11 am)
    #this column will be required for us to create a heatmap of the time duration of when most messages are sent

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period
    
    return df