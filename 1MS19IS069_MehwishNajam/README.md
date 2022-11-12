DEEP LEARNING ASSIGNMENT - 1

DATASET NUMBER - 19

The anamoly percent is 80%

STEPS :

- The required packages are imported
- Given text file is first read using read_fwf
- Column names for each column are added
- The columns with numerical values are retained
- Various stats such as mean, median etc., are calculated
- Necessary plots are made and anomalies are plotted in blue

FORMULAS :

- Mean is sum(X)/len(X)
- Median is mid(sorted(X))
- Min Max Scaler is x' = (x - min(X)) / (max(X) - min(X))
- Standard Scaler / Z Scaler is x' = (x - mean(X)) / std(X)
- Max Absolute Scaler is x' = x / max(abs(X))