from datetime import datetime
from sklearn.model_selection import KFold


MODEL_PARAMETERS = {'n_jobs': -1,
                            'n_estimators': 700, 'min_child_weight': 5, 'max_depth': 9,
                            'learning_rate': 0.05, 'colsample_bytree':0.9000000000000001, 'num_leaves': 10}
BREAK_POINT=datetime(2017, 2, 28)
K_FOLD = KFold(n_splits=5, random_state=42)