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

* 1. explanatory_data_analysis
- Import libraries & datasets
- Check datatypes,  duplicative and distinct values 
- Check missing values and impute them
- Check anomalies and handle with them
- Visualize orders in year, month, day, hour breakdowns
- Check revenue distribution by client 
- Visualize target variable
- Create order vs recency matrix
- Create correlation matrix

* 2a. baseline_model (similar for 2b and 2c)

- Import libraries & datasets
- Change data types and reduce memory usage
- Label encode categorical features
- Fill null values with the forward-filling method
- Convert raw data to a session format
- Run xgb model (cv)
- Tune hyper-parameters 
- Ensemble top 3 classifiers.
- Calculate scores

* 2b. 2a + time-related features (recency, number of days from the first order, day of week, etc.)

* 2c. 2b + consecutive and rolling features in 3 days, 1, 2, 4, 12, 24 weeks, and all time windows


We chose the tree-based xgboost model because it is easy to explain and implement for production in cloud services and also more successful in tabular datasets. 

We give more weights on class 1 using the scale pos weight parameter to label returned customers more correctly. In other words, we weight roc-auc rather than accuracy.

We could spend more time on different models (NN, CatBoost, LGBM, etc.) or tuning hyper-parameters but we should always keep in mind that it is impossible to predict all customers correctly. (Ex: predicts a customer with 1 order and 24+ week recency to give an order again.) 

Other features especially for the last order would increase model performance: 

- Rating
- Comment
- Delivery time
- Live chat experience
- Cancel reasons (courier, rest, user, etc.)
- Socio-economic: Device type & OS type & District

For further analysis, it would be also good to get geolocation data because it helps to understand whether a customer in our service area currently. (holiday, business trip, etc.)

Author
Hakkı Kaan Şimşek