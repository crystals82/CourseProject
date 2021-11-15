import openpyxl
import pandas as pd

wb = openpyxl.load_workbook('T20_Worldcup_tweets.xlsx')

ws = wb['Sheet1']

data = ws.values
# Get the first line in file as a header line
columns = next(data)[0:]
# Create a DataFrame based on the second and subsequent lines of data
t20_world_cup = pd.DataFrame(data, columns=columns)

Australia = t20_world_cup[
    (t20_world_cup['text'].str.contains('Australia|Aus')) & (t20_world_cup['text'].str.contains('NZvsAUS|AUSvsNZ'))]
# print(Australia.text)

Australia.to_csv(r'Australia.txt', index=None, sep=' ', mode='a', encoding='utf-8')

NewZealand = t20_world_cup[
    (t20_world_cup['text'].str.contains('Zealand| NZ ')) & (t20_world_cup['text'].str.contains('NZvsAUS|AUSvsNZ'))]
# print(Australia.text)
NewZealand.to_csv(r'NewZealand.txt', index=None, sep=' ', mode='a', encoding='utf-8')
