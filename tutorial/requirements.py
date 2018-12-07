import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble.forest import _generate_unsampled_indices
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from tqdm import tqdm_notebook
