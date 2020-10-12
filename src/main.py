from data_access import read_data
from utils import reduce_mem_usage
from functions import transform_data, feature_engineering
from model import run_lgb
import constants


if __name__ == "__main__":

    df = read_data()
    df = reduce_mem_usage(df, True)
    df = transform_data(df)
    df = feature_engineering(df, constants.break_point)
    predicted = run_lgb(df)