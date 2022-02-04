#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf
po.init_notebook_mode(connected=True)
cf.go_offline()


# In[2]:


def createdata(data):
    if(data == 1):
        x = np.random.rand(100, 5)
        df1 = pd.DataFrame(x, columns=['A', 'B', 'C', 'D', 'E'])
    elif(data == 2):

        x = [0, 0, 0, 0, 0]
        r1 = [0, 0, 0, 0, 0]
        r2 = [0, 0, 0, 0, 0]
        r3 = [0, 0, 0, 0, 0]
        r4 = [0, 0, 0, 0, 0]
        print("Enter the Value For Columns")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            x[i] = input()
            i = i+1
        print("Enter the Value For 1st Row")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r1[i] = int(input())
            i = i+1
        print("Enter the Value For 2nd Row")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r2[i] = int(input())
            i = i+1
        print("Enter the Value For 3rd Row")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r3[i] = int(input())
            i = i+1
        print("Enter the Vaue For 4th Row")
        i = 0
        for i in [0, 1, 2, 3, 4]:
            r4[i] = int(input())
            i = i+1
        df1 = pd.DataFrame([r1, r2, r3, r4], columns=x)
    elif(data == 3):
        file = input("Enter the file name")
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
    else:
        print("DataFrame creation Failed please enter in between 1 to 3 and try again!!!")
    return df1


# In[3]:


def plotter1(plot):
    if(plot == 1):
        finalplot = df1.iplot(kind='scatter')
    elif(plot == 2):
        finalplot = df1.iplot(kind='scatter', mode='markers',
                              symbol='x', colorscale='paired')
    elif(plot == 3):
        finalplot = df1.iplot(kind='bar')
    elif(plot == 4):
        finalplot = df1.iplot(kind='hist')
    elif(plot == 5):
        finalplot = df1.iplot(kind='box')
    elif(plot == 6):
        finalplot = df1.iplot(kind='surface')
    else:
        finalplot = print("Select Only Between 1 to 6")
    return finalplot


# In[4]:


def plotter2(plot):
    col = input(
        "Enter the number of columns you want to plot by selecting only 1, 2 or 3")
    col = int(col)
    if(col == 1):
        colm = input(
            "Enter the Column you want to plot by selecting any column from dataframe head")
        if(plot == 1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot == 2):
            finalplot = df1[colm].iplot(
                kind='scatter', mode='markers', symbol='x', colorscale='paired')
        elif(plot == 3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot == 4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot == 5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot == 6 or plot == 7):
            finalplot = print(
                "Bubble Plot and Surface Plot require more than one column arguments")
        else:
            finalplot = print("Select only between 1 to 7")
    elif(col == 2):
        print("Enter the column you want to plot by selecting from dataframe head")
        x = input("first column ")
        y = input("secound column ")
        if(plot == 1):
            finalplot = df1[[x, y]].iplot(kind='scatter')
        elif(plot == 2):
            finalplot = df1[[x, y]].iplot(
                kind='scatter', mode='markers', symbol='x', colorscale='paired')
        elif(plot == 3):
            finalplot = df1[[x, y]].iplot(kind='bar')
        elif(plot == 4):
            finalplot = df1[[x, y]].iplot(kind='hist')
        elif(plot == 5):
            finalplot = df1[[x, y]].iplot(kind='box')
        elif(plot == 6):
            finalplot = df1[[x, y]].iplot(kind='surface')
        elif(plot == 7):
            size = input("please Enter the size column for bubble plot")
            finalplot = df1.iplot(kind='bubble', x=x, y=y, size=size)
        else:
            finalplot = print("Select Only between 1 to 7")
    elif(col == 3):
        print("Enter the column you want to plot by selecting from dataframe head")
        x = input("first column ")
        y = input("secound column ")
        z = input("third column ")
        if(plot == 1):
            finalplot = df1[[x, y, z]].iplot(kind='scatter')
        elif(plot == 2):
            finalplot = df1[[x, y, z]].iplot(
                kind='scatter', mode='markers', symbol='x', colorscale='paired')
        elif(plot == 3):
            finalplot = df1[[x, y, z]].iplot(kind='bar')
        elif(plot == 4):
            finalplot = df1[[x, y, z]].iplot(kind='hist')
        elif(plot == 5):
            finalplot = df1[[x, y, z]].iplot(kind='box')
        elif(plot == 6):
            finalplot = df1[[x, y, z]].iplot(kind='surface')
        elif(plot == 7):
            size = input("please Enter the size column for bubble plot")
            finalplot = df1.iplot(kind='bubble', x=x, y=y, z=z, size=size)
        else:
            finalplot = print("Select Only between 1 to 7")

    else:
        finalplot = print("Please enter only 1,2 or 3")
    return finalplot


# In[5]:


def main(cat):
    if(cat == 1):
        print("Select The Type Of Plot You need to Plot by Writing 1 to 6")
        print("1.Line Plot")
        print("2.Scatter Plot")
        print("3.Bar Plot")
        print("4.Histogram")
        print("5.Box Plot")
        print("6.Surface Plot")
        plot = int(input())
        output = plotter1(plot)
    elif(cat == 2):
        print("Select The Type Of Plot You need to Plot by Writing 1 to 7")
        print("1.Line Plot")
        print("2.Scatter Plot")
        print("3.Bar Plot")
        print("4.Histogram")
        print("5.Box Plot")
        print("6.Surface Plot")
        print("7.Bubble Plot")
        plot = int(input())
        output = plotter2(plot)
    else:
        print("please 1 or 2 and Try Again!!")


# In[ ]:
print('Select the type of data you need to plot (By writing 1,2 0r 3)')
print('1.Random data with 100 rows and 5 columns')
print('2.Customize dataframe with 5 columns')
print('3.Upload csv/json/txt file')
data = int(input())
df1 = createdata(data)


# In[7]:


print("Your DataFrame Head is given Below check the column to plot using cufflinks")
df1.head()


# In[8]:


print("What kind of plot You Need , The Complete data plot or Column plot")
cat = input(
    "press 1 for plotting all columns or Press 2 for Specifiying columns to plot ")
cat = int(cat)


# In[15]:


main(cat)


# In[ ]:
