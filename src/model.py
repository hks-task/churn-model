def run_lgb(df):

    y = df['is_returning_customer']
    X = df.drop(columns=['customer_id', 'order_date', 'date', 'is_returning_customer',
                         'first_order_date', 'index', 'order_date_shift'])

    clf = xgboost.XGBClassifier(objective='binary:logistic', n_jobs=-1, scale_pos_weight=3,
                                )
    clf.fit(X, y)

    y_pred = cross_val_predict(clf, X, y, cv=kfold)

    predicted = pd.DataFrame(y_pred, index=df.customer_id, columns=['y_pred']).reset_index()
    predicted['y_actual'] = y
    predicted = predicted.merge(df[['customer_id', 'customer_order_rank', 'recency']], on='customer_id')
    # predicted.to_csv('pred.csv')

    print('Accuracy Score:  ', round(metrics.accuracy_score(y, y_pred), 2))
    print('Roc Auc Score:  ', round(roc_auc_score(y, y_pred), 2))
    print('Classification Report: \n', classification_report(y, y_pred, target_names=['0', '1']))
    return predicted