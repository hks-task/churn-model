from datetime import datetime
from sklearn.model_selection import KFold


MODEL_PARAMETERS = {'n_jobs': -1, 'scale_pos_weight': 2,
                            'n_estimators': 800, 'min_child_weight': 2, 'max_depth': 6,
                            'learning_rate': 0.05, 'colsample_bytree': 0.7000000000000002, 'num_leaves': 30}
BREAK_POINT=datetime(2017, 2, 28)
K_FOLD = KFold(n_splits=5, random_state=42)