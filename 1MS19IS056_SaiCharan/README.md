
# DL first assignment
### Anomaly percent - 85%

## Steps Followed
- pandas and other packages are imported
- Given text file is first read using read_fwf
- Column names are added
- Only numeric valued columns are retained
- Stats like mean and median are found
- Necessary plots are made and anomalies are plotted in red

## Formulas used
- Mean is ```sum(X)/len(X)```
- Median is ```mid(sorted(X))```
- Min Max Scaler is ```x' = (x - min(X)) / (max(X) - min(X))```
- Z Scaler is ```x' = (x - mean(X)) / std(X)```
- Max Absolute Scaler is ```x' = x / max(abs(X))```
