#####>=>>◱◲ Created on Tue Feb 22 05:33:43 2022 ◱◲<<=<#####
#####==>>==| =//= Robert P. Armstrong =//= |==<<==#####
#####==>>==| Project :  |==<<==#####
#####==>>==| Modified : 2022.00.00 |==<<==#####
#%% Import Libraries
import os
import sys
import xlwings as xw
import pandas as pd
import numpy as np
#%% List of Tuples
empoyees = [('jack', 34, 'Sydney', 155),
            ('Riti', 31, 'Delhi', 177),
            ('Aadi', 16, 'Mumbai', 81),
            ('Mohit', 31, 'Delhi', 167),
            ('Veena', 81, 'Delhi', 144),
            ('Shaunak', 35, 'Mumbai', 135),
            ('Shaun', 35, 'Colombo', 111)
            ]
#%%k Create a DataFrame object
empDfObj = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Marks'])
print(empDfObj)


#%% - https://thispointer.com/python-find-indexes-of-an-element-in-pandas-dataframe/


def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos


#%%

# Get list of index positions i.e. row & column of all occurrences of 81 in the dataframe
listOfPositions = getIndexes(empDfObj, 81)
print('Index positions of 81 in Dataframe : ')
for i in range(len(listOfPositions)):
    print('Position ', i, ' (Row index , Column Name) : ', listOfPositions[i])
    
#%%
import pandas as pd
def getIndexes(dfObj, value):
    ''' Get index positions of value in dataframe i.e. dfObj.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj.isin([value])
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos
def main():
    # List of Tuples
    empoyees = [('jack', 34, 'Sydney', 155),
                ('Riti', 31, 'Delhi', 177),
                ('Aadi', 16, 'Mumbai', 81),
                ('Mohit', 31, 'Delhi', 167),
                ('Veena', 81, 'Delhi', 144),
                ('Shaunak', 35, 'Mumbai', 135),
                ('Shaun', 35, 'Colombo', 111)
                ]
    # Create a DataFrame object
    empDfObj = pd.DataFrame(empoyees, columns=['Name', 'Age', 'City', 'Marks'])
    print('Original Dataframe : ')
    print(empDfObj)
    print('**** Find all indexes of an item in pandas dataframe ****')
    # Get list of index positions i.e. row & column of all occurrences of 81 in the dataframe
    listOfPositions = getIndexes(empDfObj, 81)
    print('Index positions of 81 in Dataframe : ')
    for i in range(len(listOfPositions)):
        print('Position ', i, ' (Row index , Column Name) : ', listOfPositions[i])
    print('How did it worked ??')
    print('Break down of steps...')
    # Get bool dataframe with True at positions where value is 81
    result = empDfObj.isin([81])
    print('Bool Dataframe representing existance of value 81 as True')
    print(result)
    # Get list of columns that contains the value i.e. 81
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    print('Names of columns which contains 81:', columnNames)
    # Iterate over each column and fetch the rows number where
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
        for row in rows:
            print('Index : ', row, ' Col : ', col)
    print('-- Find the position of multiple elements in DataFrame')
    listOfElems = [81, 'Delhi', 'abc']
    # Use dict comprhension to club index positions of multiple elements in dataframe
    dictOfPos = {elem: getIndexes(empDfObj, elem) for elem in listOfElems}
    print('Position of given elements in Dataframe are : ')
    for key, value in dictOfPos.items():
        print(key, ' : ', value)
if __name__ == '__main__':
    main()