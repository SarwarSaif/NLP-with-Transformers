import pandas as pd
from sklearn.model_selection import KFold,StratifiedKFold
import os

def create_folds(data, num_splits):
    data["kfold"] = -1
    kf = KFold(n_splits=num_splits, shuffle=True, random_state=2021)
    for f, (t_, v_) in enumerate(kf.split(X=data)):
        data.loc[v_, 'kfold'] = f
    return data


if __name__ == "__main__":
    print(os.getcwd())
    # Read train dataset
    train_df = pd.read_csv("kaggle-commonlit-redability-competition/input/train.csv")

    # Cretae KFolds 
    train_folds = create_folds(train_df, num_splits=5)

    print(train_folds)
    # Save the file
    train_folds.to_csv("kaggle-commonlit-redability-competition/input/train_folds.csv")