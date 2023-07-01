#!/usr/bin/env python
# coding: utf-8

# # Final Project
# 
# **By: Nashita Bhuiyan**

# # Introduction

# The goal of this project is to develop a model which can accurately predict a student's GPA given some student information. GPA stands for grade point average and is a numerical representation of a student's academic performance. GPA is measured over a 4.0 scale, with values closer to 4.0 associated with a higher proportion of A's across all course grades. 
# 
# The model will be trained and tested on the labeled dataset containing 1,000,000 sets of student information. The dataset contains information such as: student id, student gpa, average number of hours studied by a student, student's major, semester, year, student's age, whether a student recieves tutoring or not, number of credits taken by student in the given semester, student's parent's income, and location of student's home in longitude and latitude. It is unclear where this dataset came from so it is possible that the sample data is not representatitve of the population of college and high school students we are trying to predict from, which may lead to innaccurate predictions. 
# 
# An issue that may be encountered in developing the model is that it may take a long time for the model to be trained and tested due to the large size of the dataset. The dataset may also contain missing data or duplicates which must be accounted for during the data cleaning process. It may also be difficult to produce accurate predictions since the model may be underfitting because it may be missing features that greatly influence student's gpa. 
# 
# This model may be useful to teachers and schools. This model can be used to predict if a student is more likely to do poorly accademically, this way resources can be allocated to specific students at higher risk of academic failure. 

# In[1]:


import pandas as pd
import folium
import numpy as np
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# train data
train_data = pd.read_csv("my_data.csv")
train_data.head()


# # Data Exploration

# This section explores properties of every variable in the dataset. Specifically, for each varaible the minimimum, maximum, frequency of results, and usefulness as a predictive feature are evaluated. 

# In[3]:


train_data.nunique()


# The dataset contains 1,000,000 entries with 100,000 unique students with unique id's, home locations and parent income. 

# ## Student ID

# In[4]:


train_data['id'].min()


# In[5]:


train_data['id'].max()


# In[6]:


train_data.hist(column='id')


# The mimimum student id number is 13251 and the maximum is 113250. The frequency of each id number is evenly distributed across all possible id's. Every student has a unique id, we know this since there are 100,000 unique id's and each id occurs ten times in the dataset (apparent in the student_year section) which sums to 1,000,000 data points. Since student id identifies unique students it is not a good predictor of gpa. 

# ## Latitude

# In[7]:


train_data['lat'].min()


# In[8]:


train_data['lat'].max()


# In[9]:


train_data.hist(column='lat')


# In[10]:


correlation = train_data['gpa'].corr(train_data['lat'])
print("Correlation coefficient:", correlation)


# The minimum latitude is 31.89954590722222 and the maximum is 40.19658486280609. The latitude values are not evenly distributed with a cluster of values between 38-40 and 32-34. The correlation coefficient suggests that there is low negative correlation between latitude and gpa. This means that latitude alone may not be a good predictor of gpa. 

# ## Longitude

# In[11]:


train_data['lon'].min()


# In[12]:


train_data['lon'].max()


# In[13]:


train_data.hist(column='lon')


# In[14]:


correlation = train_data['gpa'].corr(train_data['lon'])
print("Correlation coefficient:", correlation)


# The minimum longitude is -94.75403348152076 and the maximum is -75.79067949290653. The longitude values are not evenly distributed with a cluster of values between -95-(-92), -91-(-87), and -77.5-(-75). The correlation coefficient suggests that there is low negative correlation between longitude and gpa. This means that longitude alone may not be a good predictor of gpa. 

# ## Latitude and Longitude

# Since the individual latitude and longitude measures alone did not seem to have significant correlation with gpa, we will look at how together latitude and longitude coordinates are correlated to gpa. We will also evaluate coordinate patterns found in the dataset. 

# In[15]:


# Assuming you have a DataFrame called 'df' with longitude and latitude columns
coordinate_counts = train_data.groupby(['lon', 'lat']).size().reset_index(name='count')

# Sort the counts in descending order
coordinate_counts = coordinate_counts.sort_values('count', ascending=False)

# Print the most frequently occurring coordinate groups
print(coordinate_counts.head())


# In[16]:


# Create a map centered on the coordinates of your choice
map = folium.Map(location=[37.0902, -50.7129], zoom_start=3)

# Iterate over the first 100 rows of the DataFrame
for index, row in train_data.head(1000).iterrows():
    # Extract the latitude and longitude values
    lat = row['lat']
    lon = row['lon']
    
    # Create a marker for each coordinate and add it to the map
    folium.Marker(location=[lat, lon]).add_to(map)

# Display the map
map


# Based on the min max data, all of the students are located within the bounds of the US, mostly in the east coast with the furthest west coordinate being Texas. We only graphed the first 1,000 coordinate points in the dataset but if the rest of the datset follows the same pattern, most of the students cluster around the same three regions. So instead of using latitude and longitude data directly, we can cluster the coordinates and make predictions based on the what cluster group the student to predict falls under. 

# ## Average Hours Studied

# In[17]:


train_data['avg_hours_studied'].min()


# In[18]:


train_data['avg_hours_studied'].max()


# In[19]:


train_data.hist(column='avg_hours_studied')


# In[20]:


train_data['avg_hours_studied'].value_counts()


# In[21]:


correlation = train_data['gpa'].corr(train_data['avg_hours_studied'])
print("Correlation coefficient:", correlation)


# In[22]:


# Exclude outliers
filtered_data = train_data[train_data['avg_hours_studied'] != 10000]

# Calculate correlation
correlation = filtered_data['gpa'].corr(filtered_data['avg_hours_studied'])
print("Correlation coefficient:", correlation)


# The minimum average number of hours studied per week is 0 and the maximum is 10,000 which is impossible. If we calculate the correlation between hours studied and gpa the correlation is low. However, if we account for the fact that an individual cannot study 10,000 hours in a week hours studied actually has a medium correlation with gpa. This means that average hours studied per week is a good indicator of gpa. 

# ## Parents Income

# In[23]:


train_data['parents_income'].min()


# In[24]:


train_data['parents_income'].max()


# In[25]:


train_data.hist(column='parents_income')


# In[26]:


correlation = train_data['gpa'].corr(train_data['parents_income'])
print("Correlation coefficient:", correlation)


# The minimum value of parents income is 18229.30176674215, and the maximum value is 196273.33724594. Parent income is relatively normally distributed with most students' parent income centered around 62,500. Parent income has a low correlation with gpa. ALthough parent income has a low correlation, it can be used in conjuction with other features to predict gpa. 

# ## Major

# In[27]:


train_data['major'].min()


# In[28]:


train_data['major'].max()


# In[29]:


import matplotlib.pyplot as plt

# Plot the histogram
plt.hist(train_data['major'])

# Show the plot
plt.show()


# The minimum value in major is CS and the maximum is Physics. The number of datapoints under each major category is evenly distributed. Since the majors are evenly dstributed, it is unclear whehter or not major would be a good predictor of gpa. 

# ## Tutoring

# In[30]:


print("Minimum tutoring value:", train_data['tutoring'].unique())


# There are null values in this column so we will determine min, max, and freuquency for now excluding the null values in the list. 

# In[31]:


# Drop NaN values in the 'tutoring' column and find the minimum value
min_tutoring = np.min(train_data['tutoring'].dropna())

print("Minimum tutoring value (excluding NaN):", min_tutoring)


# In[32]:


# Drop NaN values in the 'tutoring' column and find the minimum value
min_tutoring = np.max(train_data['tutoring'].dropna())

print("Maximum tutoring value (excluding NaN):", min_tutoring)


# In[33]:


# Plot the histogram
plt.hist(train_data['tutoring'].dropna())

# Show the plot
plt.show()


# The minimum value in the tutoring column is No and max is Yes. The tutoring values are unevely distributed, with most datapoints falling under the 'no' category. Since the results are unevenly distributed, it could be a decent predictor of gpa assuming the datapoints within the 'yes' group follow a similar pattern. 

# ## Semester

# In[34]:


train_data['semester'].min()


# In[35]:


train_data['semester'].max()


# In[36]:


# Plot the histogram
plt.hist(train_data['semester'])

# Show the plot
plt.show()


# The minimum value in the semester column is 'Fall' and the maximum is 'Spring.' The semester values are distributed evenly, therefore it is unclear whether semester alone is a good indicator of gpa. 

# ## Credits

# In[37]:


train_data['credits'].min()


# In[38]:


train_data['credits'].max()


# In[39]:


train_data.hist(column='credits')


# In[40]:


correlation = train_data['gpa'].corr(train_data['credits'])
print("Correlation coefficient:", correlation)


# The minimum value of credits is 9 and hte maximum is 18. The number of credits is evenly distributed across the different credit options. Credits and gpa have a low negative correlation, but it may be used to predict gpa with other variables. 

# ## Student Age

# In[41]:


train_data['student_age'].min()


# In[42]:


train_data['student_age'].max()


# In[43]:


train_data.hist(column='student_age')


# In[44]:


correlation = train_data['gpa'].corr(train_data['student_age'])
print("Correlation coefficient:", correlation)


# The minimum student age is 17 and the maximum is 33. The student ages seem to follow a bimodal distribution, with peaks at 19 and 23. The correlation between age and gpa is very small, therefore it may not be a good predictor for gpa.

# ## Student Year

# In[45]:


train_data['student_year'].min()


# In[46]:


train_data['student_year'].max()


# In[47]:


# Plot the histogram
plt.hist(train_data['student_year'])

# Show the plot
plt.show()


# The minimum value in student year is Freshman and the maximum is Sophomore. There are the same number of freshman, sophomores, and juniors in the dataset and the number of seniors is twice of that. It is not clear if student year is a good predictor for gpa. 

# ## Year

# In[48]:


train_data['year'].min()


# In[49]:


train_data['year'].max()


# In[50]:


train_data.hist(column='year')


# In[51]:


correlation = train_data['gpa'].corr(train_data['year'])
print("Correlation coefficient:", correlation)


# The minimum year value is 2005 and the maximum year value is 2025. The year data seems to be normally distributed. Year and gpa has a low correlation so it may not be a good predictor. 

# ## Questions

# ### Does this school have transfer students?
# 

# In[52]:


# Group the DataFrame by 'id' and sum the 'credits' column
credits_counts = train_data.groupby('id')['credits'].sum()

# Print the credits counts
print(min(credits_counts))


# The fewest credits a student has is 96 which is lower than the total number of required credits to get a bachelor's degree which is 120. So this school likely has transfer students.

# ### What is the median length of attendence at this university?

# In[53]:


# Group the DataFrame by 'id', 'year', and 'semester' and count the occurrences
counts = train_data.groupby(['id', 'year', 'semester']).size().reset_index(name='count')

# Count the number of unique combinations of 'id', 'year', and 'semester'
unique_counts = counts.groupby('id').size().reset_index(name='unique_count')

# Create a list of the unique counts
unique_counts_list = unique_counts['unique_count'].tolist()

# Find the maximum count in the list
median_count = np.median(unique_counts_list)

# Print the maximum count0
print("Median count:", median_count/2)


# The median length of attendance is 5 years.

# ### Do you think this university has any one credit classes?
# 

# In[54]:


train_data['credits'].unique()


# There is no one credit class in the list of unique number of credits so it is unclear if there is one credit class offered. Also, all the unique values in the number of credist list can be found by some combination of 3 and 4 credits so it is unlikely that a one credit class is offered. 

# ### Is grade inflation a problem at this university?
# 

# In[55]:


# Group the dataframe by year and calculate the average GPA for each year
gpa_by_year = train_data.groupby('year')['gpa'].mean()

# Create a line plot of GPA over the years
plt.plot(gpa_by_year.index, gpa_by_year.values, marker='o')

# Set the plot title and labels
plt.title("Student GPA over the Years")
plt.xlabel("Year")
plt.ylabel("GPA")

# Show the plot
plt.show()


# There is a grade inflation problem since gpa has been generally increasing over the years.

# ### In what area do you think the Univesrity might be located?
# 

# In[56]:


# typically located near where most of the student's homes are, so the median latitude and longitude
import numpy as np

# Find the median longitude and latitude
median_longitude = np.median(train_data['lon'])
median_latitude = np.median(train_data['lat'])

# Print the median longitude and latitude
print("Median Longitude:", median_longitude)
print("Median Latitude:", median_latitude)

# Create a map centered on the coordinates of your choice
map = folium.Map(location=[37.0902, -50.7129], zoom_start=3)
 
# Create a marker for each coordinate and add it to the map
folium.Marker(location=[median_latitude, median_longitude]).add_to(map)

# Display the map
map


# Most students in a university live near the university. The university is likely in the DC, Maryland, Virginia region since the median longitude and latitude is in that area. 

# ### Does tutoring make a stastically significant difference in grade?
# 

# In[57]:


from scipy import stats

# Separate the data into tutoring and non-tutoring groups
tutoring_group = train_data[train_data['tutoring'] == 'Yes']['gpa']
non_tutoring_group = train_data[train_data['tutoring'] == 'No']['gpa']

# Perform the t-test
t_statistic, p_value = stats.ttest_ind(tutoring_group, non_tutoring_group)

# Check the p-value to determine statistical significance
alpha = 0.05  # significance level
if p_value < alpha:
    print("There is a statistically significant difference between tutoring and non-tutoring groups.")
else:
    print("There is no statistically significant difference between tutoring and non-tutoring groups.")

# Print the t-statistic and p-value
print("T-Statistic:", t_statistic)
print("P-Value:", p_value)


# **Null Hypothesis**: The mean gpa is the same with and without tutoring. 
# 
# **Alternative Hypothesis**: The mean spa is different with and without tutoring. 
# 
# The p-value is 0.0 which is less than any standard alpha level, we can therefore reject the null hypothesis and conclude that there is a significant difference in grades with and without tutoring. 
# 
# This means that tutoring can be a good predictor for gpa. 

# ### How often do students switch majors?
# 

# In[58]:


# Group the dataframe by 'id' and count the number of unique majors
unique_major_changes = train_data.groupby('id')['major'].nunique().reset_index()

# Get a list of the number of different majors per student
num_majors_list = unique_major_changes['major'].tolist()

# Print the list
print("Students change majors average: ", np.mean(num_majors_list))


# On average students change majors 1.06954 times throughout their academic career. 

# ### Do different majors have different GPA distributions? (Hyp test

# In[59]:


from scipy import stats

# Create a dictionary to store GPA data for each major
major_gpa = {}

# Iterate over unique majors
for major in train_data['major'].unique():
    major_gpa[major] = train_data[train_data['major'] == major]['gpa']

# Perform the ANOVA test
f_statistic, p_value = stats.f_oneway(*major_gpa.values())

# Check the p-value to determine statistical significance
alpha = 0.05  # significance level
if p_value < alpha:
    print("There is a statistically significant difference in GPA distributions between majors.")
else:
    print("There is no statistically significant difference in GPA distributions between majors.")

# Print the F-statistic and p-value
print("F-Statistic:", f_statistic)
print("P-Value:", p_value)


# **Null Hypothesis**: GPA has the same distribution for every major.
# 
# **Alternative Hypothesis**: There is at least one major with a different distribution from the other majors.
# 
# The p-value is 0.0 which is less than any standard alpha level, we can therefore reject the null hypothesis and conclude that there is at least one major with a different distribution for gpa compared to the other majors.
# 
# This means that major could be a good predictor for gpa.

# # Data Cleaning

# ## Missing Data

# The tutoring column is the only column with missing values. Typically, a student seeks tutoring if they have been tutored before and remain without tutoring if they do not often go for tutoring. Therefore, we fill the missing values with the mode for tutoring for a specific student. 

# In[60]:


train_data.isnull().sum()


# In[61]:


# Group the train_data by student ID and fill NaN values in tutoring with mode within each group
train_data['tutoring'] = train_data.groupby('id')['tutoring'].apply(lambda x: x.fillna(x.mode().iloc[0]))


# In[62]:


train_data.isnull().sum()


# ## Outliers

# The average hours studied group has the outlier 10,000 hours. Students tend to study for the same number of hours per week as the previous year. So we replace the 10,000 hours with the average hours studied by the particular student in a prior semester.

# In[63]:


train_data['avg_hours_studied'] = train_data.groupby('id')['avg_hours_studied'].apply(lambda x: x.mask(x == 10000).ffill().astype(float).fillna(0).astype(int))


# In[64]:


train_data['avg_hours_studied'].value_counts()


# In[65]:


train_data.isnull().sum()


# ## One Hot Encoding

# ### Student Year, Semester, Major, Tutoring

# In[66]:


train_data_encoded = pd.get_dummies(train_data, columns=['student_year', 'semester', 'tutoring', 'major'])


# In[67]:


train_data_encoded.head()


# ## Latitude and Longitude

# As we saw in data exploration, the latitude and longitude values seem to cluster around three groups. We can assign latitude and longitude coordinates to specific location clusters using k-means. 

# In[68]:


train_data_encoded.isnull().sum()


# In[69]:


from sklearn.cluster import KMeans

# Select the latitude and longitude columns from train_data
coordinates = train_data_encoded[['lat', 'lon']]

# Specify the number of clusters
num_clusters = 3

# Perform K-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(coordinates)

# Add the cluster labels as a new column in train_data
train_data_encoded['cluster'] = clusters


# In[70]:


train_data_encoded['cluster'].value_counts()


# # Evaluation

# An issue with the model is that the values in the dataset are ordered based on id and year/semester. This means that if we simply apply k-fold cross validation splitting the dataset given the order it is in, the training set might retain some unique features related to the ordering of the data and may not predict new datapoints accurately. We can avoid this issue by creating testing sets through randomly selecting points from the original dataset to test on. To evaluate the model I will randomly select datapoints to oconstruct a training set then test on a different subset of the original dataset and score the predicted results using mean absolute error. 

# # Modeling

# ## Random Forest

# In[74]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Select the features and target variable
features = ['cluster', 'avg_hours_studied', 'parents_income', 'credits', 'tutoring_No', 'tutoring_Yes', 'credits', 'year']
target = 'gpa'

# Filter the dataset to include only the selected features and target
data = train_data_encoded[features + [target]].copy()

# Remove rows with missing values, if any
data.dropna(inplace=True)

# Split the data into training and testing sets using random sampling
train_data_sampled = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data_sampled.index)

# Separate the features and target variable in the training set
X_train = train_data_sampled[features]
y_train = train_data_sampled[target]

# Initialize and train the Random Forest model with specified hyperparameters
rf_model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
rf_model.fit(X_train, y_train)

# Predict on the test set
X_test = test_data[features]
y_test = test_data[target]
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = np.mean((y_pred - y_test) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_pred - y_test))
r2 = rf_model.score(X_test, y_test)

# Print evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared (R2):", r2)


# The random forest model has the hyperparameters number of estimaters and max depth. After testing several values for n_estimators and max_depth, the value 50 and 10 respectively were chosen because it miminized the MAE value and limited the processing time to a reasonable amount. The model has a mean absolute error of about 0.236 which means that the model's prediction for gpa is off by about 0.236 grade points. 

# ## Decision Tree

# In[83]:


from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Select the features and target variable
features = ['cluster', 'avg_hours_studied', 'parents_income', 'credits', 'tutoring_No', 'tutoring_Yes', 'credits', 'year']
target = 'gpa'

# Filter the dataset to include only the selected features and target
data = train_data_encoded[features + [target]].copy()

# Remove rows with missing values, if any
data.dropna(inplace=True)

# Split the data into training and testing sets using random sampling
train_data_sampled = data.sample(frac=0.8, random_state=42)
test_data = data.drop(train_data_sampled.index)

# Separate the features and target variable in the training set
X_train = train_data_sampled[features]
y_train = train_data_sampled[target]

# Initialize and train the Decision Tree model with a specified max_depth
max_depth = 10  # Adjust the desired max_depth value
dt_model = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
dt_model.fit(X_train, y_train)

# Predict on the test set
X_test = test_data[features]
y_test = test_data[target]
y_pred = dt_model.predict(X_test)

# Evaluate the model
mse = np.mean((y_pred - y_test) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_pred - y_test))
r2 = dt_model.score(X_test, y_test)

# Print evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared (R2):", r2)


# The decision tree model has the hyperparameter max depth. After testing several values for max_depth, the value 10 was chosen because it miminized the MAE value. The model has a mean absolute error of about 0.237 which means that the model's prediction for gpa is off by about 0.237 grade points. 

# ## Linear Regression

# In[84]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Select the features and target variable
features = ['cluster', 'avg_hours_studied', 'parents_income', 'credits', 'tutoring_No', 'tutoring_Yes', 'credits', 'year']
target = 'gpa'

# Filter the dataset to include only the selected features and target
data = train_data_encoded[features + [target]].copy()

# Remove rows with missing values, if any
data.dropna(inplace=True)

# Split the data into training and testing sets using random sampling
train_data_sampled, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Separate the features and target variable in the training set
X_train = train_data_sampled[features]
y_train = train_data_sampled[target]

# Initialize and train the Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict on the test set
X_test = test_data[features]
y_test = test_data[target]
y_pred = lr_model.predict(X_test)

# Evaluate the model
mse = np.mean((y_pred - y_test) ** 2)
rmse = np.sqrt(mse)
mae = np.mean(np.abs(y_pred - y_test))
r2 = lr_model.score(X_test, y_test)

# Print evaluation metrics
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared (R2):", r2)


# The linear regression model has no hyperparameters. The model has a MAE value of 0.329 which means that the model's prediction for gpa is off by 0.329 grade points. Note that this regression model assumes that there is a linear relationship between the features and gpa, which may not be true. 

# # Conclusion

# For this project we constructed several regression models to predict the gpa of a student given some set of student information. To construct the models we first performed some data exploration to determine what features significantly impacted gpa and how different variables were related to one another. We then performed feature engineering where we accounted for missing values and outliers and converted cateforical variables to numerical using one-hot encoding. After preparing the dataset through these steps we constructed three different regression models: random forest, decision tree, and linear regression. The most accurate model of those trained and tested was the random forest and decision tree with a MAE of around 0.24 grade points. I do not think the model is very successful since gpa is on a scale of 0-4 so 0.24 is a significant measure on this scale. However, depending on the goal of the model 0.24 MAE may be associated with a relatively successful model. Going forward, I may need information related to what the acceptable MAE may be. For future models we can also determine what other features to include or combination of features to include in the model so it performed better. Going forward we also need to understand the population we are trying to make predictions about and if the dataset provided is representative of that population. 

# In[ ]:




