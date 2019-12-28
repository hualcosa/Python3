# This was a project i've made during pandas course in Codecademy


import pandas as pd
pd.set_option('display.max_colwidth', -1)

# Loading the data
dataset = pd.read_csv('jeopardy.csv')
#print(dataset.columns)

# Renaming misformatted data
dataset = dataset.rename(columns = {
' index': 'index', ' Show Number': 'Show Number', ' Air Date': 'Air Date', ' Round': 'Round', ' Category': 'Category', ' Value':'Value', ' Question': 'Question', ' Answer': 'Answer' 
})
#print(dataset[" Question"])

# Filtering the dataset by a list of rows
def filter_data(data, words):
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    # Applies the lambda function to the question Column
    return data.loc[data["Question"].apply(filter)]

# testing the filter function
filtered = filter_data(dataset, ["King", "England"])
# print(filtered['Question'])

# cleaning the value column and putting it into a new column
l_function = lambda x: float(x[1:].replace(',','')) if x != 'None' else 0  
dataset['Float value'] = dataset['Value'].apply(l_function)

# Filtering the dataset and finding the average value of questions that contain a certain keyword
filtered = filter_data(dataset, ['King'])
print(filtered["Float value"].mean())

# A function to find unique answers of a set of data 
def get_answer_counts(data):
    return data['Answer'].value_counts()

# testing the count function
print(get_answer_counts(filtered))