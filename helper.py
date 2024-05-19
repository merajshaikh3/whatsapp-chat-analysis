from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

#instantiation
extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
         df = df[df['user'] == selected_user]
    
    # 1. fetch number of users
    num_messages = df.shape[0]

    # 2. fetch number of words
    words = []
    for message in df['message']:
         words.extend(message.split())
    
    # 3. fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>'].shape[0]

    # 4. fetch number of links shared
    links = []
    for message in df['message']:
         links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
     x = df['user'].value_counts()
     df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index':'name', 'user':'percent'})
     
     return x, df

def create_word_cloud(selected_user, df):

    filter_df = df[df['message'] != "<Media omitted>"]

    if selected_user != 'Overall':
        filter_df = filter_df[filter_df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    df_wc= wc.generate(filter_df['message'].str.cat(sep=" "))

    return df_wc

def most_common_words(selected_user, df):

     filter_df = df[df['message'] != "<Media omitted>"]

     if selected_user != 'Overall':
        filter_df = filter_df[filter_df['user'] == selected_user]

     f = open('stop_hinglish.txt','r')
     stop_words = f.read()

     words = []

     for message in filter_df['message']:
         for word in message.lower().split():
             if word not in stop_words:
                 words.append(word)

     most_common_df = pd.DataFrame(Counter(words).most_common(20))

     return most_common_df

def most_common_emoji(selected_user, df):
    
     if selected_user != 'Overall':
          df = df[df['user'] == selected_user]
     
     emojis = []
     for message in df['message']:
         emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
     
     most_common_emoji = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

     return most_common_emoji

def monthly_timeline(selected_user, df):
    
     if selected_user != 'Overall':
          df = df[df['user'] == selected_user]
     
     #creating a new df with only the year, month_num, month and message count
     timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()

     #creating a new column where month and year are concatenated (will become x-axis of time-series graph)
     time = []
     for i in range(timeline.shape[0]):
         time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

     timeline['time'] = time

     return timeline

def daily_timeline(selected_user, df):
    
     if selected_user != 'Overall':
          df = df[df['user'] == selected_user]

     daily_timeline = df.groupby('only_date').count()['message'].reset_index()

     return daily_timeline

def week_activity_map(selected_user, df):

     if selected_user != 'Overall':
          df = df[df['user'] == selected_user]

     return df['day_name'].value_counts()

def month_activity_map(selected_user, df):

     if selected_user != 'Overall':
          df = df[df['user'] == selected_user]

     return df['month'].value_counts()

def activity_heatmap(selected_user, df):

     if selected_user != 'Overall':
          df = df[df['user'] == selected_user]

     #creating a pivot table which has day names (i.e. Mon, Tue, Wed etc) as row headers and time period (0-1, 1-2, 2-3 etc) as column headers

     user_heatmap = df.pivot_table(index='day_name', columns = 'period', values = 'message', aggfunc = 'count').fillna(0)

     return user_heatmap
     
