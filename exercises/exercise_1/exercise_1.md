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
d) Scaling means that you want to standardize the numerical data so that all the data points has similar interval. the reason is that you dont want larger numerical values like salary (75000) to be more "important for the model compared to lower numerical values like age(31). so for short, by scaling you make all the numerical values as equally important to each other.
scaling is really important in distance-based algorithms, such as KNN. Just because they calculate the "distance" between two data points, it would be heavily influenced by the features with larger magnitudes if not scaled. 


e) What is the purpose to split the data into a training part and a test part?
e) the purpose to split the data is to not give the algorithm the right "answers" so the final result is not "infected" with faulty data.
the train data is used to obviously train the algorithm, while the test data is the "questions" and the "right answer" you want the algorithm to come as close as possible to.


f) What is data leakage, why is it bad and how can you avoid it?
f) data leakage is that you leak test data into the training data. this will give you an unrealistically optimistic result that creates an illusion that the algorithm works better than it actually does.  
you have to make sure that you DO NOT leak the test data into the train data. 
To avoid data leakage you must perform all data preprocessing steps AFTER you have made train|test split. You should always fit any preprocessing steps only on the training data, and then use that same transformation to process the test data. This ensures that the model doesnt learn from the test data during the training phase.

g) What are some common evaluation metrics for regression models?
the three most common ones are:
MAE (Mean Absolute Error)
MSE (Mean Squared Error)
RMSE (Root Mean Squared Error)

MAE calculates the average absolute difference between the predicted values and the actual values.
MSE calculates the average Squared error between the predicted values and the actual value.
RMSE(most common) Is used to calculate the square root of the MSE. It is often preferred because it is in the same value as the target value but it still penalizes large errors more heavily.

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| Terminology          | Meaning |
| :------------------- | ------: |
| supervised learning  |You train an algorithm using data that contains both the input and the correct answers (labels).                                                    |
| machine learning     |Where a computer is trained to learn from data without being explicitly programmed for every task.                                                  |
| data science         |Uses data to find insights and solve problems.                                                                                                      |
| data engineering     |Focuses on building and maintaining the system that collect and store data.                                                                         |
| algorithm            |Set of instructions or rules a computer follows to sole a problem or build a model.                                                                 |
| regression           |A type of machine learning problem where the goal is to predict a numerical value (for example, the price of a house).                              |
| classification       |A type of machine learning problem where the goal is to predict a category or a label (for example, whether an image shows a cat or a dog).         |
| qualitative data     |Descriptive information that is based on qualities and cant me measured with numbers, such as opinions etc.                                         |
| quantitative data    |Numerical information that can be counted or measured, such as height, weight, age, etc.                                                            |
| independent variable |         |
| dependent variable   |         |
| label                |         |
| feature              |         |
| model                |         |
| training             |         |
| evaluation           |The process of measuring how well a trained model performs on a given task by comparing its predictions to the actual answers.                      |
| prediction           |The result or guess that a trained model provides when it is given new data to work with.                                                           |
