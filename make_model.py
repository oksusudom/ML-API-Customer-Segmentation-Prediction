
from random import triangular
import psycopg2
import pandas as pd


conn = psycopg2.connect(
    host="localhost",
    port = 5432,
    database="postgres",
    user="postgres",
    password="sc507546")

cur = conn.cursor()

# Train 데이터 불러오기
sql_train = """
    SELECT 
        gender,         /* 0 성별: Male, Female */
        ever_married,   /* 1 결혼한 적이 한번이라도 있는지 여부: Yes, No */
        age,            /* 2 나이: 정수 */
        graduated,      /* 3 대학 졸업 여부: Yes, No */
        profession,     /* 4 직종: (Categorical Data) */
        work_experience,    /* 5 경력 연차: 정수 */
        spending_score,     /* 6 소비 점수: 정수 */
        family_size,    /* 7 가족 구성원 수 */
        var_1,          /* 8 카테고리?: (Categorical Data) */
        segmentation    /* 9 고객 등급: A, B, C, D */
    FROM train
"""


cur.execute(sql_train)

train_result = cur.fetchall()

# Test 데이터 불러오기
sql_test = """
    SELECT 
        gender,         /* 0 성별: Male, Female */
        ever_married,   /* 1 결혼한 적이 한번이라도 있는지 여부: Yes, No */
        age,            /* 2 나이: 정수 */
        graduated,      /* 3 대학 졸업 여부: Yes, No */
        profession,     /* 4 직종: (Categorical Data) */
        work_experience,    /* 5 경력 연차: 정수 */
        spending_score,     /* 6 소비 점수: 정수 */
        family_size,    /* 7 가족 구성원 수 */
        var_1,          /* 8 카테고리?: (Categorical Data) */
        segmentation_truth    /* 9 고객 등급: A, B, C, D */
    FROM test
"""
cur.execute(sql_test)

test_result = cur.fetchall()

# Train, Test DB 결과를 DataFrame으로 변환
df_train = pd.DataFrame(train_result)
df_test = pd.DataFrame(test_result)

conn.close()

df_train.columns = ('Gender', 'Ever_Married', 'Age', 'Graduated', 'Profession', 
    'Work_Experience','Spending_Score', 'Family_Size', 'Var_1', 'Segmentation')
df_test.columns = ('Gender', 'Ever_Married', 'Age', 'Graduated', 'Profession', 
    'Work_Experience','Spending_Score', 'Family_Size', 'Var_1', 'Segmentation_Truth')

from sklearn.model_selection import train_test_split

target = 'Segmentation'

features = df_train.columns.drop([target])

train, val = train_test_split(df_train, test_size=0.25, random_state=42)

test = df_test
test['Segmentation'] = test['Segmentation_Truth']

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]
X_test = test[features]
y_test = test[target]

print(X_test.head())

# print(train.shape, val.shape, test,shape)
# (3748, 10) (1250, 10) (1667, 10)

from sklearn.metrics import accuracy_score, confusion_matrix

major = y_train.mode()[0]
pred = [major] * len(y_train)
val_pred = [major] * len(y_val)

# Baseline
# print("training_accuracy_score: ", accuracy_score(y_train, pred))
# print("validation_accuracy_score ", accuracy_score(y_val, val_pred))
# training_accuracy_score:  0.25907150480256136
# validation_accuracy_score  0.244

# ML MODEL TEST
from sklearn.metrics import f1_score, accuracy_score, classification_report
from category_encoders import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint
from xgboost import XGBClassifier

xg = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(),
    XGBClassifier(n_jobs=-1, random_state=42))

xg.fit(X_train, y_train)
y_pred_01 = xg.predict(X_val)


'''
print('train accuracy:', xg.score(X_train, y_train))
print('validation accuracy:', xg.score(X_val, y_val))
print('report',classification_report(y_val, y_pred_01))
print('roc_auc_score: ', roc_auc_score(y_val, y_pred_01))

train accuracy: 0.8641942369263608
validation accuracy: 0.5184
report          precision    recall  f1-score   support

           A       0.43      0.42      0.42       310
           B       0.37      0.30      0.33       279
           C       0.55      0.59      0.57       305
           D       0.65      0.72      0.68       356

    accuracy                           0.52      1250
   macro avg       0.50      0.51      0.50      1250
weighted avg       0.51      0.52      0.51      1250
'''

pipe = make_pipeline(
    OrdinalEncoder(),
    SimpleImputer(),
    XGBClassifier(random_state=42)
)

dist = {
    'simpleimputer__strategy': ['most_frequent', 'constant'],
    'xgbclassifier__n_estimators' : randint(100,300),
    'xgbclassifier__max_depth' : [3, 5, 7, 10],
}

clf = RandomizedSearchCV(
    pipe,
    param_distributions=dist,
    n_iter=5,
    cv=3,
    scoring ='f1',
    verbose=1,
    n_jobs=-1
)

clf.fit(X_train, y_train)
clf.best_params_

#print('best_params: ', clf.best_params_)

'''
best_params:  {'simpleimputer__strategy': 'constant', 
            'xgbclassifier__max_depth': 7, 
            'xgbclassifier__n_estimators': 214}
'''

model = clf.best_estimator_

y_pred_train = model.predict(X_train)
y_pred_val = model.predict(X_val)


'''
print('train accuracy:', model.score(X_train, y_train))
print('validation accuracy:', model.score(X_val, y_val))
print('Report:',classification_report(y_val, y_pred_val))
print('roc_auc_score: ', roc_auc_score(y_val, y_pred_val))

train accuracy: 0.8321771611526148
validation accuracy: 0.524
Report:               precision    recall  f1-score   support

           A       0.46      0.45      0.46       310
           B       0.37      0.31      0.34       279
           C       0.54      0.57      0.56       305
           D       0.65      0.71      0.68       356

    accuracy                           0.52      1250
   macro avg       0.51      0.51      0.51      1250
weighted avg       0.51      0.52      0.52      1250
'''

y_pred = model.predict(X_test)

#print('test accuracy:', model.score(X_test, y_test))
print('Report:',classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# 다중 분류의 평가지표
print("micro 평균 f1 점수 : {:.3f}".format(f1_score(y_test, y_pred,average = "micro")))
print("macro 평균 f1 점수 : {:.3f}".format(f1_score(y_test, y_pred,average = "macro")))


'''
test accuracy: 0.47690461907618475
Report:               precision    recall  f1-score   support

           A       0.40      0.39      0.40       407
           B       0.35      0.33      0.34       385
           C       0.53      0.54      0.54       444
           D       0.59      0.62      0.61       431

    accuracy                           0.48      1667
   macro avg       0.47      0.47      0.47      1667
weighted avg       0.47      0.48      0.47      1667

[[160  97  59  91]
 [ 93 127 124  41]
 [ 51 102 241  50]
 [ 93  40  31 267]]
micro 평균 f1 점수 : 0.477
macro 평균 f1 점수 : 0.470
'''


'''
xgb = model.named_steps['xgbclassifier']
importances = pd.Series(xgb.feature_importances_, X_train.columns)

print(importances)

Gender             0.073828
Ever_Married       0.089765
Age                0.124042
Graduated          0.130939
Profession         0.132172
Work_Experience    0.073383
Spending_Score     0.212437
Family_Size        0.081587
Var_1              0.081848

'''
# feature importance가 높은 4개 특성만 골라서 진행

# model to pickle
import pickle

with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)

