import numpy as np
from pylab import *

#Create fake income/age clusters for N people in k clusters
def createClusteredData(N, k):
    pointsPerCluster = float(N)/k
    X = []
    y = []
    for i in range (k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y



(X, y) = createClusteredData(100, 5)

plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
plt.show()


from sklearn import svm, datasets

C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X, y)  #default is rbf

#visualization
def plotPredictions(clf):
    xx, yy = np.meshgrid(np.arange(0, 250000, 10), np.arange(10, 70, 0.5))
    print(xx.shape, yy.shape, np.arange(0, 250000, 10).shape, np.arange(10, 70, 0.5).shape)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    plt.figure(figsize=(8, 6))
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu_r, alpha=0.8)   #plt.cm.datad.keys()   #All colormaps' names
    plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
    plt.show()
    
plotPredictions(svc)

#just use predict for a given point:
print(svc.predict([[200000, 40]]))
print(svc.predict([[50000, 65]]))