# Churn Prediction Model #

This repository is a general template for the churn prediction model.

### Getting Started ###

```
$ git clone https://github.com/hks-task/churn-model.git
$ cd churn-model/src
$ python main.py
```

### Usage ###

The service template can be executed by running main.py, with the precondition that necessary requirements are provided.
The general pipeline for this service template is the following:

* Fetch the necessary data from files
* Explanatory data analysis (+notebooks)
* Feature engineering
* Model & parameter selection (+notebooks)
* Performance evaluation and monitoring
* Export the model to a S3 bucket

The template in this repository has functions that successfully and efficiently execute all of these steps.

### Components ###

The pipeline consists of 5 components:

* data_access.py: read order, label datasets and merge them
* utils.py: reduce memory usage
* functions.py: data transformation&engineering 
* model.py: run the xgb model
* main.py: execute all pipeline

The notebooks consists of 5 components:

Most functions in notebooks are similar. We could import them from a helper file.

#### 1. Explanatory Data Analysis ####

- Import libraries & datasets
- Check datatypes,  duplicative and distinct values 
- Check missing values and impute them
- Check anomalies and handle with them
- Visualize orders in year, month, day, hour breakdowns
- Check revenue distribution by client 
- Visualize target variable
- Create order vs recency matrix
- Create correlation matrix

#### 2a. Baseline Model (similar for 2b and 2c) ####

- Import libraries & datasets
- Change data types and reduce memory usage
- Label encode categorical features
- Fill null values with the forward-filling method
- Convert raw data to a session format
- Run different models
- Calculate scores

#### 2b. Baseline Model+Time Features ####

#### 2c. Baseline Model+Time Features+Rolling Features ####

#### 3. Final Model+Parameter Selection ####

#### 4. Model Results+Interpretation ####

We could spend more time on different models (NN, CatBoost, etc.) or tuning hyper-parameters but there is a trade-off between time you spent and improvement in the model. Data quality and extra features would increase model performance as below: 

- Rating
- Comment
- Delivery time
- Live chat experience
- Cancel reasons (courier, rest, user, etc.)
- Age, gender, device type, district, OS type

For further analysis, it would be also good to get geolocation data because it helps to understand whether a customer in our service area currently. (holiday, business trip, etc.)

### Author ###
Hakkı Kaan Şimşek