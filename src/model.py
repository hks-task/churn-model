import constants
from sklearn.model_selection import cross_val_score
import lightgbm
import pandas as pd


def run_lgb(df):

    y = df['is_returning_customer']
    X = df.drop(columns=['customer_id', 'order_date', 'is_returning_customer',
                         'first_order_date', 'index', 'order_date_shift'])

    clf = lightgbm.LGBMClassifier(**constants.MODEL_PARAMETERS)

    auc_mean = cross_val_score(clf, X, y, cv=constants.K_FOLD, scoring="roc_auc").mean()
    auc_std = cross_val_score(clf, X, y, cv=constants.K_FOLD, scoring="roc_auc").std()

    acc_mean = cross_val_score(clf, X, y, cv=constants.K_FOLD, scoring="accuracy").mean()
    acc_std = cross_val_score(clf, X, y, cv=constants.K_FOLD, scoring="accuracy").std()

    model_result = round(pd.DataFrame({'Roc-Auc Mean': auc_mean, 'Roc-Auc Std': auc_std,
                                       'Accuracy Mean': acc_mean, 'Accuracy Std': acc_std},
                                      index=['LGBM Classifier']), 4)
    print(model_result)

    #pickle.dump(clf, open(config.MODEL_FILENAME, 'wb'))
    #config.s3_client.upload_file(config.MODEL_FILENAME, config.S3_BUCKET_NAME, config.MODEL_FILENAME)
    #print('model uploaded to s3 bucket')