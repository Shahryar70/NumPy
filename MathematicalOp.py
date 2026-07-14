import numpy as np
# 5. Vectorized arithmetic — the core idea
bills = np.array([5000,6000,7000,8000,12000])
ages = np.array([23,34,56,41,52])
# Scalar Operation
# print(bills*1.1)
# print(bills/1000)
# print(bills-500)
# print(ages+1)

# base_bills = ([20,30,40,40,90])
# base_ages = ([2,3,4,5,6])
# print(base_bills*bills)
# print(base_ages*ages)

# Aggregate functions
# print(np.sum(bills))
# print(np.mean(bills))
# print(np.median(bills))
# print(np.std(bills))
# print(np.min(bills))
# print(np.max(bills))
# print(np.var(bills))

# Rounding
# print(np.round(bills))
# print(np.floor(4500.3))
# print(np.ceil(4500.9))

# cumlative sum
# bills_total= np.cumsum(bills)
# print(bills_total)

#percentiles
p25= np.percentile(bills,25)
p50 = np.percentile(bills,50)
p75 = np.percentile(bills,75)
iqr = p75-p25  
print(f"Q1={p25} Q2={p50} Q3={p75} Iqr={iqr}")
#Outlier detection using IQR 
lower_fence = p25-1.5*iqr
upper_fence = p50+1.5*iqr
outlier = bills[(bills < lower_fence) | (bills > upper_fence)]
print(f"Outliers {outlier}")
# Normalisation — scale all values to 0-1 range
bills_norms = (bills - np.min(bills)) / (np.max(bills) - np.min(bills))
print(np.round(bills_norms,2))

#Standardisation 
bill_std = (bills - np.mean(bills)) / np.std(bills)
print(np.round(bill_std,2))

#Correlation 
# Correlation matrix — rows and columns are [ages, bills]
