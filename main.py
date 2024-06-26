#start from 1:22:00

import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import seaborn as sns

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #will print the file data on streamlit console
    data = bytes_data.decode("utf-8")
    # st.text(data)
    df = preprocessor.preprocess(data)

    # st.dataframe(df)

    #fetech unique users
    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        #Stats Area
        st.title("Top Statistics")
        num_messages, num_words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(num_words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # monthly timeline
        st.title("Monthly Timeline")
        monthly_timeline = helper.monthly_timeline(selected_user, df)
        fig,ax = plt.subplots()
        ax.plot(monthly_timeline['time'], monthly_timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig,ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        #activity map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user,df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user,df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color = 'orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # activity heat map

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_heatmap)
        st.pyplot(fig)


        # finding the busiest users in the group (Group level)
        if selected_user == 'Overall':
            st.title("Most Busy Users")
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()
            

            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

        # WordCloud
        st.title("Word Cloud")
        df_wc = helper.create_word_cloud(selected_user, df)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # most common words
        st.title("Most common words")
        most_common_df = helper.most_common_words(selected_user, df)

        fig,ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # most common emoji
        st.title("Most common emoji")
        most_common_emoji = helper.most_common_emoji(selected_user, df)

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(most_common_emoji)
        with col2:
            fig,ax = plt.subplots()
            ax.pie(most_common_emoji[1].head(), labels=most_common_emoji[0].head() , autopct="%0.2f")
            st.pyplot(fig)
        




