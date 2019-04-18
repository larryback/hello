from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import pandas as pd

# csv 파일 읽기 (속도를 위해 정해진 양만 읽음)
def readCsv(file, maxcnt):
    labels = []
    images = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt: break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))      # 첫번째 자리가 label
            images.append(list(map(lambda b: int(b) / 256, cols))) # 실수 벡터화
    return {"labels": labels, "images": images}


train = readCsv('./data/train.csv', 2000)   # 학습용 데이터가 많아질수록 스코어 상승!
test = readCsv('./data/t10k.csv', 500)


# train 2000개로 학습, test 100개로 검증
clf = svm.SVC(gamma='auto')
clf.fit(train['images'], train['labels'])
pred = clf.predict(test['images'])

score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)

print("-----------------------------------------")
report = metrics.classification_report(test['labels'], pred)
print(report)
