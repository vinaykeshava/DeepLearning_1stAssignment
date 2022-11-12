The outliers have been identified and been extracted

Steps followed

1 - used boxplot to find outliers(Few columns were found to have outliers)

2 - checked for distribution using density plot (Some of column were non-gaussian distribution)

3 - Normalized data 


    a) using sklearn normailze function

    b) using sklearn MaxAbsScaler class
        scale each feature by its maximum absolute value.
        This estimator scales and translates each feature individually such
        that the maximal absolute value of each feature in the
        training set will be 1.0. It does not shift/center the data, and
        thus does not destroy any sparsity.

    c) using sklearn MinMaxScaler class
        The transformation is given by::
        X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
        X_scaled = X_std * (max - min) + min

    d) using user defined function to normaize by Z-score technique
        df_std[column] = (df_std[column] - df_std[column].mean()) / df_std[column].std()

4 - extracted outliers/anamoly using percentile method (.05 and .95 quartile were taken as anamoly)

5 - correaltion between data is visualized to find dependent variable in data
