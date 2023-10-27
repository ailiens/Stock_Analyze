import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# def main():
#     st.title('Stock Data')
#     st.sidebar.title('Stock Chart')
#     ticker = st.sidebar.text_input('Enter a ticker', value='AAPL')
#     st.sidebar.markdown('Tickers Link : [All Stock Symbols]'
#                         '(https://stockanalysis/com/stocks/)')
#     start_date = st.sidebar.data_input('시작 날짜', value=pd.to_datetime('2023-01-01'))
#     end_date = st.sidebar.data_input('종료 날짜', value=pd.to_datetime('2023-10-25'))
#     data = yf.download(ticker, start=start_date, end=end_date)
#     st.dataframe(data)
#
# if __name__ == "__main__":
#     main()
def main():
    st.title("Stock Data")
    st.sidebar.title("Stock Chart")
    ticker = st.sidebar.text_input("Enter a ticker (e. g. AAPL)", value="AAPL")
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')
    # date
    start_date = st.sidebar.date_input("시작 날짜: ", value=pd.to_datetime("2023-01-01"))
    end_date = st.sidebar.date_input("종료 날짜: ", value=pd.to_datetime("2023-10-27"))
    data = yf.download(ticker, start=start_date, end=end_date)
    st.dataframe(data)
    # chart type
    chart_type = st.sidebar.radio('Select Chart Type', ('Candle_Stick', 'Line'))
    candle = go.Candlestick(x=data.index,
                            open=data['Open'],
                            high=data['High'],
                            low=data['Low'],
                            close=data['Close'])
    line = go.Scatter(x=data.index,
                      y=data['Close'],
                      mode='lines',
                      name='Close')

    if chart_type == 'Candle_Stick':
        fig = go.Figure(candle)
    elif chart_type == 'Line':
        fig = go.Figure(line)
    else:
        st.error('Error')

    fig.update_layout(title=f'{ticker} Stock {chart_type} Chart',
                      xaxis_title='Date',
                      yaxis_title='Price')
    st.plotly_chart(fig)

###
    st.markdown('<hr>', unsafe_allow_html=True)
    num_row = st.sidebar.number_input('Number of Rows', min_value=1, max_value=len(data))

    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index('Date'))

if __name__ == "__main__":
    main()