import unittest
import helpers
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


class Test(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'numbers': [3, 16, 33, 45, 51],
            'strings': ['lorem', 'ipsum', 'dolor', 'sit', 'amet'],
            'categories': ['cat1', 'cat2', 'cat1', 'cat2', 'cat1']
        }) 

    def test_set_cols_dtype_number_col(self):
        df_numeric = helpers.set_cols_dtype(self.df, ['numbers'], 'numeric')
        self.assertTrue(pd.api.types.is_numeric_dtype(df_numeric['numbers']))

    def test_set_cols_dtype_string_col(self):
        df_strings = helpers.set_cols_dtype(self.df, ['strings'], 'numeric')
        self.assertTrue(pd.api.types.is_numeric_dtype(df_strings['strings']))

    def test_set_cols_dtype_string_col(self):
        df_numeric = helpers.set_cols_dtype(self.df, ['strings'], 'numeric')
        self.assertTrue(pd.api.types.is_numeric_dtype(df_numeric['strings']))

    def test_set_cols_dtype_invalid_col(self):
        with self.assertRaises(KeyError):
            helpers.set_cols_dtype(self.df, ['non_existent_col'], 'numeric')
    
    def test_standardize(self):
        standardized = helpers.standartize(self.df['numbers'])
        self.assertAlmostEqual(standardized.mean(), 0, places = 5)
        self.assertAlmostEqual(standardized.std(), 1, places = 5)

    def test_normalize(self):
        col = self.df['numbers']
        normalized = helpers.normalize(col)
        self.assertAlmostEqual(normalized.min(), 0, places = 5)
        self.assertAlmostEqual(normalized.max(), 1, places = 5)

    def test_encode_cols(self):
        encoded = helpers.encode_cols(self.df, ['categories'])
        np.testing.assert_array_equal(encoded['categories'], LabelEncoder().fit_transform(self.df['categories']))

    def test_encode_cols(self):
        encoded = helpers.encode_cols(self.df, ['categories'])
        self.assertTrue(
            all(encoded['categories'] == LabelEncoder().fit_transform(self.df['categories']))
        )