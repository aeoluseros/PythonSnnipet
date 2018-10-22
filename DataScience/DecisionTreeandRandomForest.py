import numpy as np
import pandas as pd
from sklearn import tree

input_file = "C:/Users/xh0728/Desktop/DataScience/DataScience-Python3/PastHires.csv"
df = pd.read_csv(input_file, header = 0)

d = {'Y': 1, 'N': 0}
df['Hired'] = df['Hired'].map(d)       #pandas map!
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d = {'BS': 0, 'MS': 1, 'PhD': 2}
df['Level of Education'] = df['Level of Education'].map(d)
df.head()

features = list(df.columns[:6])  #panda! get column index and then convert to list!
features

# construct the decision tree
y = df["Hired"]
X = df[features]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,y)

from IPython.display import Image  
from sklearn.externals.six import StringIO  
import pydotplus      #a Python Interface to Graphviz’s Dot language

dot_data = StringIO()  
tree.export_graphviz(clf, out_file=dot_data,  feature_names=features)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())  



