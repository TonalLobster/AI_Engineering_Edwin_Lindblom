# Exercise 2 - classification

In this exercise, you get to work with classification in machine learning

---

## 0. Iris flower dataset (\*)

In the whole exercise, we will work with the famous Iris flower dataset, which was collected in 1936 by Ronald Fisher, a statistician and biologist. Use the `datasets` module from scikit-learn to load the iris dataset.

&nbsp; a) Check keys on the loaded data and check what the different values for each key are.

&nbsp; b) Now insert the data into a DataFrame.

&nbsp; c) Do some EDA to get an understanding of the dataset.

&nbsp; d) Make a correlation heatmap to see how each feature is correlated to each other. What do the numbers mean?

&nbsp; e) Make a boxplot. The points outside of the boxplot are statistically calculated outliers using Tukey's rule for boxplot.

&nbsp; f) Now remove the outliers in data. (\*\*)

- Lower bound outlier: $Q_1 - 1.5\cdot IQR$
- Upper bound outlier: $Q_3 + 1.5\cdot IQR$

where $Q_1$ is the 1st quartile or 25 percentile, $Q_3$ is the 3rd quartile or 75 percentile and $IQR = Q_3-Q_1$ is the interquartile range.

&nbsp; g) Do train|test split on the dataset and then scale it with feature standardization.

&nbsp; h) Classify using logistic regression

&nbsp; i) Classify the first 10 values of your $X_{test}$ and compare it manually with your labels.

&nbsp; j) Evaluate your model using classification report and confusion matrix. 

---

## 1. KNN for classification and regression

a) Use KNN to classify iris dataset 

b) Use KNN to predict house prices for the dataset you used in exercise1 


## 2. Random forest for classification and regression

a) Use random forest to classify the iris dataset and evaluate afterwards

b) Use random forest to predict house prices for the dataset you used in exercise1 

--- 

## 3. Implement your own KNN 

Check out exercise pikachu_pichu under the folder extra. This is quite good exercise to do to understand how KNN works and to learn how to work without libraries such as scikit-learn. I usually give out this exercise as a lab for the first python course for data science. 


---
if you have time over and want to explore some simple image processing do this exercise.

## 4. MNIST data (\*)

In the whole exercise, we will work with the famous MNIST dataset. Start by installing `tensorflow` to your virtual environment if you haven't already. Import `keras` from tensorflow and load the dataset using `keras.mnist.load_data()`.

&nbsp; a) Check help() on `keras.datasets.mnist.load_data` and read to find out how to unpack the data properly.

&nbsp; b) Check the shapes of X_train, X_test, y_train, y_test. What does each dimension mean?

&nbsp; c) How many images are there in X_train?

&nbsp; d) Check smallest and largest value of a sample image of your choice. What do these numbers in the matrix represent? Plot this image using `plt.imshow()` and set cmap to "gray" to get the correct representation of the grayscale image.

&nbsp; e) Plot 20 sample images.

&nbsp; f) When you checked the shapes of the data you noticed that X_train, X_test are 3D tensors (generalization of a matrix to more dimensions). However KNN classifier in scikit-learn requires a 2D tensor or a matrix. Reshape X_train and X_test to appropriate shapes.

&nbsp; g) Do train|val|test split and scale the data using feature standardization. Check mean and standard deviation of the training and test data.

&nbsp; h) Train the models for a set of $k$-values using the training data and make predictions on validation data. Plot the validation accuracy against different $k$-values. Based on your plot, which $k$ do you choose?

&nbsp; i) Now train the KNN model using the $k$ value you have chosen. Don't waste any training samples, so use all the original 60000 of the X_train for training the KNN model. Predict on the test data.

&nbsp; j) Do a classification report and based on the report, can you figure out which number had highest proportions of false negatives. False negative in this case means that the true label is $i$ but the model predicted not $i$.

&nbsp; k) Plot a confusion matrix, does this confirm your answer in a?

&nbsp; l) Compute the number of misclassifications for each number. Which number had most misclassifications, do you have any suggestions on why this would be the case?

## Theory

a) What is supervised learning and give 2-3 examples of supervised learning?
a) Supervised learning is when you have training data that you show the model. two examples are: 1. if you want to predict house prices you actually give the model training data that includes test data(the correct house prices). example 2 is the iris dataset. when we used that we actually gave the model test images so it knew what race each flower belonged to.


b) What are the differences between classification and regression?
b) regression uses numerical values, quantative data(1,2 or 3 etc.), and classification uses qualitative data(a,b or c etc.)


c) Why split into train/validation/test sets?
c) To prevent data leakage. and also to give the model some data that isnt related to the test data. lets say you want to practice for an exam and dont want the real exam before you do it. then you use old exams to train yourself to know whre you lack any knowledge or where you have weakpoints.


d) How does feature scaling impact KNN?
d) Scaling is really importan to not give certain features more importance than others. For a house with kvm2(high values like 200) would have a higher impact than lets say number of bedrooms(lower numbers like 3). So why scaling is a must is that it gives each feature a similar "value". 


e) How to find a k value for KNN?
e) You manually try different k values and find out which one that gives you the best result(lowest error).


f) What are common metrics for evaluating classifcation?
f) Accuracy, Precision and Recall. Accuracy is the simplest and answers a broad question(how many where right?). Precision and Recall are more like specialists that focus specifically on how the model handled the "positive" class.


g) A fire alarm has 98% accuracy, but gets false positives, how could this impact if it is a good fire alarm or not?
g) It will make people believe it is a fire but when there is no fire. if it has to many false positives, people might not react to when an actual fire is happening.


h) For a covid quick screening test, what metric out of accuracy, recall and precision would you choose and why?
h) Recall. This is the best one because the priority is to minimize the number of missed cases(false negatives). Rather do an extra test on a person who has been told he's not sick, than let a sick person go home and infect others.

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology    | explanation |
| -------------- | ----------- |
| target         |What we want to achieve.                                                                                          |
| training set   |The data we train the model on.                                                                                   |
| validation set |"Practice" data to find where the model preforms poorly so we can fine tune those parts of the model.             |
| test set       |Used to get a final, unbiased evaluation of how the fully trained model performs on new, unseen data.             |
| recall         |Measures the models ability to find relevant positive cases. Important when you want to minimize false negatives. |
| f1 score       |A single score that represents the balance between precision and recall.                                          |
| regularization |             |
| hyperparameter |             |
| overfitting    |             |
| underfitting   |             |
| feature        |             |
| precision      |             |
