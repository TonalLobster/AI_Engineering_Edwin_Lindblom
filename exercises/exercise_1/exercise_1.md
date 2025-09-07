# Exercise 1 - regression

In this exercise, you get to work with linear regression for supervised learning.

## 0. EDA (\*)

In the whole exercise, we will work with the "mpg" dataset from seaborn dataset. Start by loading dataset "mpg" from the `load_dataset` method in seaborn module. The goal will be to use linear regression to predict mpg - miles per gallon.

a) Start by doing some initial EDA such as info(), describe() and figure out what you want to do with the missing values.

b) Use describe only on those columns that are relevant to get statistical information from.

c) Make some plots on some of the columns that you find interesting.

d) Check if there are any columns you might want to drop.

## 1. Linear regression on mpg dataset

a) We want to predict the "mpg", split up X and y, and perform train|test split using scikit-learn. Choose test_size of 0.2 and random_state 42. Control the shapes of each X_train, X_test, y_train, y_test.

b) Create a function for training a regression model, predicting and computing the metrics MAE, MSE, RMSE. It should take in parameters of X_train, X_test, y_train, y_test, model. Now create a linear regression model using scikit-learns `LinearRegression()` (OLS normal equation with SVD) and call your function to get metrics.

## 2. Linear regression on house dataset

Use this dataset on [house price prediction in kaggle](https://www.kaggle.com/datasets/shree1992/housedata/data), perform EDA on it and then predict the house prices using linear regression. You can drop the categorical features and the date columns. Then try ElasticNetCV and RidgeCV on the same dataset. Record the scores in a dataframe with the columns mae, mse, rmse so you can compare the models.

## 3. Implement linear regression from scratch

If you want to dive deeper to understand linear regression you can implement it yourself following [these exercises here](https://github.com/kokchun/Machine-learning-AI22/blob/main/Exercises/E00_linear_regression.ipynb).

## 4. Theory questions

a) Draw an illustration of how machine learning, deep learning and artificial intelligence relate to each other and explain it with your own words.
a) AI is at the middle, inside of that is machine learning, and inside of that circle is deep learning. An AI is something you want to achieve with the help of machine learning, and if you want to make it more specific, you can use deep learning to make it better at solving a specific task.


b) What is the main difference between regression and classification?
b) The main difference between regression and classification is that regression(numerical) is used to predict numeric value. Lets say you want to make it guess how much you could earn based on your age, education and experience, then regression could give you an answer based on the training data.
Classification(categorical) is used to predict a categorical value. An example is, lets say based on the data it has been trained on, you want to make it guess if it is going to rain next week or not rain. 


c) Give an example of a problem that can be solved with regression
c) One example is to try and predict how fast the acceleration of a car is. you take in the weight, engine type, year of production and maybe horsepower of different car models. And with that data, you can try and get an estimate of how fast the car model you dont know the acceleration of.


d) What does scaling data mean, and why do some machine learning algorithm require data to be scaled?

e) What is the purpose to split the data into a training part and a test part?

f) What is data leakage, why is it bad and how can you avoid it?

g) What are some common evaluation metrics for regression models?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| Terminology          | Meaning |
| :------------------- | ------: |
| supervised learning  |         |
| machine learning     |         |
| data science         |         |
| data engineering     |         |
| algorithm            |         |
| regression           |         |
| classification       |         |
| qualitative data     |         |
| quantitative data    |         |
| independent variable |         |
| dependent variable   |         |
| label                |         |
| feature              |         |
| model                |         |
| training             |         |
| evaluation           |         |
| prediction           |         |
