# DL first assignment
The anomaly percent is about 80%

## Steps Followed
The below steps are carried out:
- pandas and other packages are imported
- Given text file is first read using read_fwf
- Column names are added
- Only numeric valued columns are retained
- Stats like mean,mode and median are found
- Necessary plots are made and anomalies are plotted in red

## Formulas used
- Mean is ```sum(X)/len(X)```
- Median is ```mid(sorted(X))```
- Min Max Scaler is ```x' = (x - min(X)) / (max(X) - min(X))```
- Standard Scaler / Z Scaler is ```x' = (x - mean(X)) / std(X)```
- Max Absolute Scaler is ```x' = x / max(abs(X))```
