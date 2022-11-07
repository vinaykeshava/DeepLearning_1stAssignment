DL Assignment 1

The anomaly percent observed is 80%

Dataset used : Dataset 4

Steps Taken :

1 - Import required libraries and read the file
2 -Useful columns to consider are identified
3 - Only numeric valued columns are retained
4 - Columns are renamed .
4 - Stats like mean and median are calculated
5 - Necessary plots are made and anomalies are plotted in red

Formulas 
> Mean = sum(X)/len(X)
> MinMaxScaler x' = (x - min(X)) / (max(X) - min(X))
> Median is mid(sorted(X))
> Standard Scaler / Z Scaler is x' = (x - mean(X)) / std(X)
> Max Absolute Scaler is x' = x / max(abs(X))