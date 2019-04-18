from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import pandas as pd

# data 준비
csv = pd.read_csv('./data/iris.csv')       # csv[:4] : 0 ~ 4행
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

# 75% TrainingSet, 25% TestSet

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)

#print(trainLabel)

clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel)  #훈련(학습)

pred = clf.predict(testData)   #검증(테스트)
score = metrics.accuracy_score(testLabel, pred)
print("score=", score)

print("____________________________________________")

r = clf.predict([[6.4,2.8,5.6,2.1]])
print("품종:", r[0])

