from itertools import count

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

from FinalProject import dataFrame


class DataCleaner:

    def replaceNullWithMedian(dataFrame: pd.DataFrame):

       columns_null_data = dataFrame.columns[dataFrame.isnull.any()].tolist()

       for i in columns_null_data:
           dataFrame[i] = dataFrame[i].fillna(dataFrame[i].median)

       if(dataFrame.isnull().sum().sum() > 0):
           print("EROOR -> Data frame with null values")

       return dataFrame