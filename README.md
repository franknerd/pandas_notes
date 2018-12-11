# pandas_notes
Pandas notes (data processing)

1. EDA (exploratory data analysis)
   - missing values
      * df.isnull().sum()
   - data types
      * df.dtypes
   - gengeral info
      * df.describe() for numerical features
      * df.describe(include=['O']) for categorical features
   - correlation
      * df.corr()
   - distribution
      * df[col].hist()
   - range and number of categorical features
      * df[col].unique & df[col].nunique
   - top frequency
      * df[col].value_counts().head()
   - shape
      * df.shape
   - check the info of dataframe including memory usage
      * df.info()

