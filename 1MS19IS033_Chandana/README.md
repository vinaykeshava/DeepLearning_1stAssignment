
# Deep Learning Assignment 1

### The percentage of anomalies is 80%

#### Alloted dataset: 2.txt

Following are the steps:                                   
1. All necessary packages are imported.
2. The dataset is read using pd.read_csv
3. Statistics like mean, median and mode are found.
4. Found outliers using percentile method.
5. Only numeric columns are retained.
6. performed normalization:                                      
    Maximum Absolute Scaling                                   
    MinMax Scaling                                              
    Z-Score
7. necessary plots are made and anomalies are plotted in black.
8. Also used distplot to find outliers.

### Formulas used
#### Mean = sum(X) / len(X)
#### Median = mid(sorted(X))
#### Min Max Scaler x' = (x - min(X)) / (max(X) - min(X))
#### Standard Scaler / Z Scaler is x' = (x - mean(X)) / std(X)
#### Max Absolute Scaler is x' = x / max(abs(X))

