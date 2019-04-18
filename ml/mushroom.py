import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics

# 데이터 준비하기                          https://archive.ics.uci.edu/ml/datasets/Mushroom
# - download csv dataset: agaricus-lepiota.data
# - 첫 컬럼이 label(p: poisonous, e: edible), 나머지 22개 컬럼이 특징

df = pd.read_csv("./data/mushroom.csv")  

#print(df)       # 저장한 파일 읽기

#exit()
allLabel=[]
allData=[] # [[1, 2, 3]]

for rowidx, row in df.iterrows():
    
	allLabel.append(row.iloc[0])
	ords=[]
	for c in row.iloc[1:]:
		ords.append(ord(c))
		allData.append(ords)


                   
	     


       

trainData, testData, trainLabel, testLabel = train_test_split(allData, allLabel)

# 학습 시키기
from sklearn.ensemble import RandomForestClassifier       # 앙상블 > 랜덤포레스트
# RandomForestClassifier 수행
# n_estimators : 모형의 정밀도(추정의 정밀도)
# n_jobs: 사용 CPU Core수 (-1: 모두 사용)
# random_state: 난수값(난수표) 
clf = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=4096)       

clf.fit(trainData, trainLabel)

pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)
report = metrics.classification_report(testLabel, pred)

