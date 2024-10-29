import pandas as pd
import common
import numpy as np
import os

print(os.getcwd())


df = common.load_data('database.xls')

print(df.head())