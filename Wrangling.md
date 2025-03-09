# Data Preprocessing

**Cleaning Steps**
- Effective data preprocessing is crucial for ensuring the accuracy and reliability of the analysis. The following cleaning steps were undertaken: Handling Missing or Null Values: Missing data, such as incomplete information on theft locations or bike types, was identified and addressed. Depending on the field, missing values were either imputed using relevant averages or medians or removed if deemed insignificant to the analysis.
- Removing Duplicates or Irrelevant Entries: Duplicate entries, where the same theft was recorded multiple times, were identified and removed. Similarly, irrelevant entries, such as incomplete or inconsistent records, were excluded to maintain data quality.
- Addressing Outliers in Theft Frequency or Time: Outliers, such as unusually high theft counts in specific locations or unreasonably reported times, were flagged and reviewed. These anomalies were corrected if identified as data entry errors or excluded if deemed untrustworthy.

By implementing these steps, the dataset was refined to ensure accurate and meaningful insights could be derived from the analysis.


**Creating New Features**

To enhance the dataset and enable deeper analysis, new features were created based on existing data attributes. These include:

- Theft Density: Using geographical data, a theft density metric was calculated to identify areas with a high concentration of reported bicycle thefts. This metric was derived by aggregating theft counts within specific geographic boundaries (e.g., neighborhoods or grid squares).
- Seasonality: A seasonal indicator was created by grouping thefts into seasons (e.g., Spring, Summer, Fall, Winter) based on the date of occurrence. This allowed for the identification of seasonal patterns, such as increased thefts during warmer months.

**Encoding Categorical Variables**

To make categorical data usable for analysis, categorical variables were encoded into numerical formats:

- Type of Bike: The types of bikes (e.g., mountain, road, hybrid) were encoded using one-hot encoding or label encoding, depending on the analysis requirements. This enabled comparisons between theft rates for different bike types.
- Neighborhood or Region: Geographical data (e.g., neighborhood names) was encoded into numerical or categorical bins to facilitate spatial analysis and visualization.
