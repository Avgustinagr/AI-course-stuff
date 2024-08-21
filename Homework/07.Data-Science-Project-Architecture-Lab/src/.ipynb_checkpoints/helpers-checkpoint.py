import pandas as pd
from sklearn.preprocessing import LabelEncoder

def set_cols_dtype(df, cols, dtype):
    """
    Sets the dtype of the given columns in the dataframe

    Args:
        df (pandas DataFrame): dataframe the columns of which will be updated
        cols (list of strings): names of columns in df to be updated
        dtype (str): the dtype the columns will be set to

    Returns:
        A new DataFrame, copy of df with updated column dtypes
    """
    new_df = df.copy()
    for col in cols:
        if dtype == 'numeric':
            new_df[col] = pd.to_numeric(new_df[col], errors = 'coerce')
        else:
            new_df[col] = new_df[col].astype(dtype)
    return new_df

def standartize(col):
    """ Takes a column (type Series) and returns it standartized """
    centered = col - col.mean()
    return centered / centered.std()

def normalize(col):
    """ Takes a column (type Series) and returns it normalized """
    start_at_zero = col - col.min()
    return start_at_zero / start_at_zero.max()

def encode_cols(df, cols):
    """ 
    Encodes the given columns in df

    Args:
        df (pandas DataFrame): dataframe whose columns will be encoded
        cols (list of strings): names of columns in df to be updated
    
    Returns: 
        A new DataFrame, copy of df with encoded columns
    """
    new_df = df().copy()
    cat_encoder = LabelEncoder()
    for col in cols:
        new_df[col] = cat_encoder.fit_transform(new_df[col])
    return new_df
