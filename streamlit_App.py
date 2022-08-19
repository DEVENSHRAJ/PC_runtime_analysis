import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta
import numpy as np


st.set_page_config(page_title='PC run time analysis', page_icon='🕔')
st.markdown("<h1 style='text-align: center;font-size: calc(2.4rem + 1.8vw);color: grey;'>PC run time</h1>", unsafe_allow_html=True)
st.text('To better understand how much the computer has run till date')

# Create file uploader object
upload_file = st.file_uploader('Upload a file containing PC excel run time data')

# structuring the runtime file properly
def st_describe_display(start,end):
    col1.header('Statistics of Runtime')
    col1.write(df[start:end].describe())
    # matplotlib work
    fig, ax = plt.subplots(1, 1)
    A=df[start:end]['date']
    B=df[start:end]['total runtime']
    data_line = ax.scatter(x=A, y=B)
    ax.set_xlabel('Date')
    ax.set_ylabel('Total PC runtime')
    y_mean = [np.mean(B)]*len(A)
    mean_line = ax.plot(A, y_mean, label='Mean', linestyle='--',color='red')
    col2.header("Graph view")
    col2.pyplot(fig)


if upload_file is not None:
    df = pd.read_csv(upload_file)
    date_filter = st.slider('Choose start date',min_value=datetime.strptime(df.iloc[0,0], '%Y-%m-%d'),value=[datetime.strptime(df.iloc[0,0], '%Y-%m-%d'), datetime.strptime(df.iloc[-1,0], '%Y-%m-%d')])
    str_idx=df.loc[df['date'] == str(date_filter[0])[0:10]].index.tolist()
    end_idx = df.loc[df['date'] == str(date_filter[1])[0:10]].index.tolist()
    col1, col2 = st.columns(2)
    st_describe_display(str_idx[0],end_idx[0])




# '''
# helpful links
#
# https://docs.streamlit.io/library/cheatsheet
#https://pythonhow.com/python-tutorial/pandas/Accessing-pandas-dataframe-columns-rows-and-cells/
#https://docs.streamlit.io/library/api-reference/widgets/st.slider
#https://www.activestate.com/resources/quick-reads/how-to-access-a-column-in-a-dataframe-using-pandas/#:~:text=You%20can%20use%20the%20loc,Let's%20see%20how.&text=If%20we%20wanted%20to%20access,in%20order%20to%20retrieve%20it.
#https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
#https://devenum.com/how-to-find-index-of-value-in-pandas-dataframe/#:~:text=values%20to%20Find%20index%20of,Math'%20in%20the%20Subject%20column.
#https://docs.streamlit.io/library/api-reference/widgets/st.slider
    #https://www.geeksforgeeks.org/a-beginners-guide-to-streamlit/
# https://docs.streamlit.io/library/api-reference/charts
# '''


## rough

    #login window
    # with st.form(key='my_form'):
    #     username = st.text_input('Username')
    #     password = st.text_input('Password')
    #     st.form_submit_button('Login')


    # Create a section for the dataframe statistics
    # st.write(type(datetime.strptime(df.iloc[1,0], '%Y-%m-%d')))
    # trial_sld = st.slider('trial slider',min_value=100, value=[100,400])

    #st.write(type(upload_file))
    #filtering the uploaded file
    # file_filter(upload_file)
    # # Read the file to a dataframe using pandas

    #console logger
    # st.header('data print logger')
    # st.write(upload_file)
    # st.write(upload_file.name)
    # st.write(str_idx)
    # st.write(end_idx)
    # Create a section for the dataframe header
    # col2.header('Header of Dataframe')
    # col2.write(df[start:end].head())
# sidebar
# a = st.sidebar.radio('Select one:', [1, 2])