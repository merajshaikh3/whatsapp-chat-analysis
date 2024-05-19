# Whatsapp Chat Analysis

This project is a WhatsApp chat analyzer that allows you to analyze and visualize trends in your WhatsApp group chats. You can see who messages the most, how frequently they message, and more. The analysis can be done at both group and individual member levels. This project is implemented by following the [YouTube tutorial by CampusX](https://www.youtube.com/watch?v=Q0QwvZKG_6Q&ab_channel=CampusX).

![Screenshot-2](https://github.com/merajshaikh3/whatsapp-chat-analysis/assets/47921927/acbafd06-8f42-46d2-b221-472badf2f544)

![Screenshot-3](https://github.com/merajshaikh3/whatsapp-chat-analysis/assets/47921927/f72220b3-c18f-4ef3-8f0d-e278a2c9e402)

## Features
* **Message Frequency Analysis:** Determine who messages the most and how frequently.
* **Individual Member Analysis:** Analyze messaging patterns of individual members.
* **Data Visualization:** Create various charts to visualize chat data using matplotlib, seaborn, and wordcloud.

## Technology Stack
* **Streamlit:** Used to create the interactive dashboard.
* **Pandas:** Used for data analysis.
* **Matplotlib/Seaborn/Wordcloud:** Used to create data visualizations.

## File Structure
* **main.py:** Contains the Streamlit code required to create the dashboard. To run the program, open your terminal and type: ```streamlit run main.py```
* **pre_processor.py:** Takes raw data from ```data.txt``` and converts it into a consumable DataFrame.
* **stop_hinglish.txt:** List of Hinglish (Hindi & English mix) stop words that are removed from the data to make the results more meaningful.
* **data.txt:** Place your WhatsApp raw data in this file. It contains 2-3 lines of dummy data to show you the format of the data.

## How to Download Data Dump from WhatsApp
* Open the WhatsApp group chat.
* Tap the More options menu (three dots).
* Tap More.
* Tap Export chat.
* Choose whether to export with media or without media.
* Choose the save destination on your device storage.

## Setup Instructions
* **Clone the Repository:** Type the below commands in your terminal

  ```git clone <repository_url>```

  ```cd <repository_directory>```


