from data_access import read_data
from utils import reduce_mem_usage
from functions import transform_data, feature_engineering
from model import run_lgb
import constants
import traceback


if __name__ == "__main__":
    try:
        df = read_data()
        df = reduce_mem_usage(df, True)
        df = transform_data(df)
        df = feature_engineering(df, constants.BREAK_POINT)
        run_lgb(df)
    except Exception:
        err = traceback.format_exc()
        print(err)