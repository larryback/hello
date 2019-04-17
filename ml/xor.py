from sklearn import svm, metrics
import pandas as pd

xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# data 준비 (pandas)
df = pd.DataFrame(xor_data)

print(df)
print("_______________________________________________________________")
print(df.head)
print("_______________________________________________________________")
print(df.shape)
print("_______________________________________________________________")
print(list(df.columns))
print("_______________________________________________________________")
print(len(df.index))
print("_______________________________________________________________")

# XOR 학습시키기
clf = svm.SVC(gamma='auto')   # Support Vector Classification
clf.fit(df.loc[:, 0:1], df.loc[:, 2]) # 학습시켜 최적의 cost 찾기

print(df.loc[:, 0:1])
print("_______________________________________________________________")
print(df.loc[:, 0:2])
print("_______________________________________________________________")

# 정답률 구하기
pred = clf.predict([[0, 1], [1, 0], [1, 1], [2, -1]])
score = metrics.accuracy_score([1, 1, 0, 1], pred)
print("score=", score)

testset = [[0,1]]
testset = [[0,1], [1,0], [1,1], [2, -1], [3, 1]]
pred = clf.predict(testset)
print("pred=", pred)

#score = metrics.accuracy_score([1, 0], pred)

score = metrics.accuracy_score([1, 1, 0, 1, 1], pred)

print("score=", score)

while True:
    cmd = input("Input x y>> ")
    if not cmd: break
        
    x, y = cmd.split(' ')
    t = [[int(x), int(y)]]
    p = clf.predict(t)[0]
    print("pred=", "참" if p == 1 else '거짓')

# print("head=", df.head)
# print("shape=", df.shape)
# print("colums=", list(df.columns))
# print("nrow=", len(df.index))