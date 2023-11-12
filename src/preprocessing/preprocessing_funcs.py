import numpy as np
import pandas as pd
from typing import List, Any
from src.config.config import Columns


def handle_nans(data: pd.DataFrame, column: str) -> List[float]:
    col = Columns()
    converted_values = []
    for value in data[column]:
        try:
            float_value = float(value)
            converted_values.append(float_value)
        except ValueError:
            converted_values.append(np.nan)
    for i in converted_values:
        if str(i) == 'nan':
            print(i)
    return converted_values


def prepare_df_for_analysis(data: pd.DataFrame) -> pd.DataFrame:
    col = Columns()
    data = data.replace(col.values_to_change)
    data = pd.get_dummies(data, columns=col.cols_to_encode)
    data = data.dropna(subset=[col.total_charges_col])
    data = data.replace({True: 1, False: 0})
    return data
