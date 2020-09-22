#------------------------------------------------------------------------------------------------------------
import numpy as np   # numpy
import pandas as pd  # pandas
import matplotlib.pyplot as plt # pyplot
import seaborn as sns# seaborn

%matplotlib inline   # python inline magic function # "%matplotlib notebook:" will lead to interactive plots embedded within the notebook, you can zoom and resize the figure

import pdpipe as pdp # Easy pipelines for pandas DataFrames # https://pdpipe.github.io/pdpipe/doc/pdpipe/
#dataframe_variable=pd.read_csv('C:/Users/W10_Desktop/Dropbox/Data_Science/Datasets/anime-recommendations-database/anime.csv')



#_In case version needed
print('Python: {}'.format(sys.version))
print('Scipy: {}'.format(scipy.__version__))
print('Numpy: {}'.format(numpy.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('Pandas: {}'.format(pandas.__version__))
print('Sklearn: {}'.format(sklearn.__version__))
#------------------------------------------------------------------------------------------------------------

Pandas BEST PRACTICES or MOST USED:

#importing file into panda's dataframe
dataframe_variable = pd.read_csv('anime-recommendations-database/anime.csv') # reading the file: full address and file name OR if local just file name
dataframe_variable = pd.read_csv("data/cereal.csv", skiprows = 1) # in case issues with headers on first line skipping 1st row

#manual setup of dataframe with column names
dataframe_variable = pd.DataFrame([[1,'Bob', 'Builder'],
                  [2,'Sally', 'Baker'],
                  [3,'Scott', 'Candle Stick Maker']], 
				  columns=['id','name', 'occupation'])


# doing a copy in case of backup needed
df_var_bak = dataframe_variable.copy(deep=True)

#Sample a data frame
dataframe_variable.sample(frac=0.25)

# getting columns names
dataframe_variable.columns
dataframe_variable.rename(columns = {'test':'TEST'}, inplace = True) # renaming in this case to all capital letters specific column

#Convert a column to another data type
dataframe_variable.variable.astype()

# getting top and bottom items from dataset, parenthesis will provide default # or desire can be indicated
dataframe_variable.head(3)
dataframe_variable.tail(1)

# dataframe transpose
dataframe_variable.T
# dataframe crosstab
pd.crosstab(index = mpg['origin'], columns = mpg['model_year'])

# not a dataframe function but useful
len(dataframe_variable)
# count unique values in a column
len(dataframe_variable['column_name'].unique())

# overview & stats of dataframe variable
dataframe_variable.shape  # rows x columns amount
dataframe_variable.info() # types of variables per column
dataframe_variable.describe() # stats based on dataframe

# counts of values for a particular column
#value_counts() does not count NaN (missing) values
dataframe_variable.column.value_counts()
#example: myList = df.artists.value_counts().nlargest(3).index # will store on myList top 3 values from dataframe column "artists"
#         df_new = df.where(df.artists.isin(myList),other='other artists') # and here will use same list to filter out any other into a grouping category on new dataframe
# subset of columns selection from original dataset
dataframe_variable[['column1','column2']]
# the oposite, dropping specific columns
dataframe_variable.drop(['column1','column2'],axis=1]

# adding new column based on condition or function
dataframe_variable['Address'] =  dataframe_variable['Bedrooms'].apply(aFunction) # aFunction previosly definited

# Conditional Label-based Selection
# a) Single Condition 
dataframe_variable.loc[dataframe_variable.property_name == 'ABC']
# b) Multiple conditions using AND
dataframe_variable.loc[dataframe_variable.property_name == 'ABC' & dataframe_variable.property_name == 'DEF']
# c) Multiple conditions using OR
dataframe_variable.loc[dataframe_variable.property_name == 'ABC' | dataframe_variable.property_name == 'DEF']


# Select where value is in a list of values
dataframe_variable.loc[dataframe_variable.property_name isin(['ABC','DEF']) # "aList" parameter can also be provided

#Retrieve rows where a column’s value is in a given list. 
dataframe_variable[dataframe_variable['column_name'].isin(['value_1', 'value_2'])] #will return rows were columns match list of values

# adding .tolist()
#most methods will allow you to see the results
dataframe_variable.columns.tolist()

#Retrieve rows with matching index values
dataframe_variable.loc[['Value_1','Value_2']]
#Retrieve rows by numbered index values
dataframe_variable.iloc[0:3] #from position 0 to 3 row in this case

#Slice a dataframe
dataframe_variable[1:3]

#Filter by value
dataframe_variable[dataframe_variable['column'] > 8] #similar to one above

#Sorting
dataframe_variable.sort_values('column1', ascending=False)
dataframe_variable.sort_values('column1','column2', ascending=False)

# Renaming a column
dataframe_variable.rename(columns={'ABC': 'DEF'})

# Most common missing value data labels: .(full stop), * (asterisk),N/A , NaN or -999
dataframe_variable.isnull().sum() # .isnull().sum() will provide a sum of null values per column # "notnull()" is another option too
dataframe_variable.isna().any()   # result will be a boolean if there is or not na on columns

# ways to address missing value can be removal of records, imputation with 0, central value imputation and other imputation methods as per below
variable_shorted=dataframe_variable.dropna() # default axis=0 by records,axis=1 will be on columns
                                             # thresh= can be used for a specif amount of na before deleting that record
                                             # how={‘any’, ‘all’}, default ‘any’, ‘all’ : If "all" values are NA, drop that row or column.
dataframe_variable.column.fillna(0) # 1. exchanging for 0 value will induce a lot of bias into the dataset
                                    # 2. dataframe_variable.column.max() replacing with the maximum value of that column
                                    # 3. method='ffill' or 'bfill' is used on time series to fill the missing values with the values that come before or after
                                    # 4. dataframe_variable.column.value_counts().index[0] will be using the most common value in the column
  dataframe_variable.column.replace("n/a", "unknown") # also used to replace"n/a" values with "unknown" for example


# GROUPBY function

#_ <df>.groupby(<columns & arguments>).<agregation function>.<additional functions> _#

df[[‘Country’, ‘Quantity’]].groupby(‘Country’).sum().head() #.head() added just to reduce outcome

df[[‘InvoiceDate’, ‘Quantity’]].groupby(df[‘InvoiceDate’].dt.date).sum().sort_values(by=’Quantity’, ascending=False).head() # .dt.date to get a more granular level on date type values
                                                                                                                            # .sort_values just sort the outcome

df[[‘InvoiceDate’, ‘Quantity’, ‘Country’]].groupby([df[‘InvoiceDate’].dt.month, df[‘Country’]]).sum().head() # multi level .groupby also possible

country_agg = df[[‘Country’, ‘Quantity’, ‘UnitPrice’]]  # using multiple aggregation functions
country_agg = country_agg.groupby([‘Country’]).agg({‘Quantity’:’sum’, ‘UnitPrice’:’mean’})country_agg.head()
country_agg = country_agg.groupby([‘Country’]).agg({‘Quantity’:[‘min’, ‘max’, ‘sum’], ‘UnitPrice’:’mean’})country_agg.head() # more complex and mixed aggregation
# for more details:
# https://towardsdatascience.com/pandas-groupby-aggregate-transform-filter-c95ba3444bbb


#_PANDAS EQUIVALENT OF 10 USEFULL SQL QUERIES_#

1. SELECT
SQL:    SELECT col1, col2, ... FROM table
PYTHON: dataframe_variable[['video_id', 'title']]
        dataframe_variable.loc[:,['video_id', 'title']]
        
SQL:    SELECT DISTINCT col1, col2, ... FROM table
PYTHON: dataframe_variable.loc[:, ['channel_title']].drop_duplicates()

SQL:    SELECT TOP number col1, col2, ... FROM table or SELECT col1, col2, ... FROM table LIMIT number
PYTHON: dataframe_variable.loc[:, ['video_id', 'title']].head(5) or dataframe_variable.loc[:, ['video_id', 'title']].tail(5)

SQL:    SELECT MIN(col) FROM table or SELECT MAX(col) FROM table or SELECT COUNT(col) FROM table
PYTHON: dataframe_variable.loc[:, ['views']].min() or dataframe_variable.loc[:, ['views']].max() or dataframe_variable.loc[:, ['views']].count()


#_PYTHON CLASSES_#
 
class Person:   
      
    def __init__(self, name):   # init method or constructor    
        self.name = name        # attribute

    def say_hi(self):           # Sample Method    
        print('Hello, my name is', self.name)   
      
p = Person('Nikhil')  #creating a variable type of class previously
p.say_hi() #calling method inside class
Output: Hello, my name is Nikhil


#example with default values preseted 
class Foo:
  DEFAULT_NUM = 1
  def __init__(num = None):
    self.num = num if num is not None else DEFAULT_NUM
   
#another examplewith default values
class Warehouse:
    def __init__(self, var_pur="default1",var_reg="default2"):
        self.mypurpose=var_pur
        self.myregion=var_reg


#_JUPYTER COSMETICS_#

# install jupyterthemes
!pip install jupyterthemes

#accessing all the jupyter themes!
!jt -l

#For example, I want to change it to monokai theme
!jt -t monokai

#Reset the change
#!jt -r
