from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from scipy import stats
import numpy as np
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer

from dataloader import data


# Transforming qualitative variables

# #creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown = 'ignore')
# #perform one-hot encoding on 'team' column 
encoders = pd.DataFrame(encoder.fit_transform(data[['X4', 'X38']]).toarray())
# #merge one-hot encoded columns back with original DataFrame
final_data = data.join(encoders)


# Z score

z_scores = np.abs(stats.zscore(final_data['Y']))
threshold = 3
# Position of the outliers
outliers = np.where(z_scores > threshold)
# delecting of outliers
final_data.drop(outliers[0], inplace = True)


# slice data

seed = 12345
# kind of repartition 
kf = StratifiedKFold(n_splits = 10, shuffle = True, random_state = seed)

Y = final_data["Y"].copy()
X = final_data.drop(["Y", 'X4', 'X38'], axis = 1).copy()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = seed)


# Scaling data

# list of variables to scale
listes = X_train.iloc[:, 0:36].columns.to_list()
# scaler_sd = StandardScaler()
scaler_sd = ColumnTransformer([
        ('scaler', StandardScaler(), listes)
    ], remainder = 'passthrough')


# Get scaling parameters with the train sample exclusively, using the Scaler.fit() function
scaler_sd.fit(X_train)

# Scale data using Scaler.transform()
X_train_scaled = pd.DataFrame(scaler_sd.transform(X_train))
X_test_scaled = pd.DataFrame(scaler_sd.transform(X_test))