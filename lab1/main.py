import statistics
import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns # custom list
import pandas as pd # like table
import csv



df = pd.read_csv('countries.csv', names = ['index','rank','country','gdp_mil'])
print(f'mean: {df.mean()}')