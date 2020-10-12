import constants
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import lightgbm


def run_lgb(df):

    y = df['is_returning_customer']
    X = df.drop(columns=['customer_id', 'order_date', 'date', 'is_returning_customer',
                         'first_order_date', 'index', 'order_date_shift'])


    clf = lightgbm.LGBMClassifier(n_jobs=-1, scale_pos_weight=2,
                            n_estimators=800, min_child_weight=2, max_depth=6,
                            learning_rate=0.05, colsample_bytree=0.7000000000000002, num_leaves=30)

    y_pred = cross_val_predict(clf, X, y, cv=constants.kfold)

    print('Accuracy Score:  ', round(metrics.accuracy_score(y, y_pred), 2))
    print('Roc Auc Score:  ', round(roc_auc_score(y, y_pred), 2))
    print('Classification Report: \n', classification_report(y, y_pred, target_names=['0', '1']))

    #pickle.dump(clf, open(config.MODEL_FILENAME, 'wb'))
    #config.s3_client.upload_file(config.MODEL_FILENAME, config.S3_BUCKET_NAME, config.MODEL_FILENAME)
    #print('model uploaded to s3 bucket')