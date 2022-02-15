import os
import csv
import psycopg2
import pandas as pd
#import numpy as np


dir = "C:/Users/sucheol/Desktop/archive/"
train_csv = pd.read_csv(dir + 'train.csv')
test_csv = pd.read_csv(dir + "test.csv")

# 결측치 제거
train_csv = train_csv.dropna()
test_csv = test_csv.dropna()


conn = psycopg2.connect(
    host="localhost",
    port = 5432,
    database="postgres",
    user="postgres",
    password="sc507546")

cur = conn.cursor()


sql = """
    INSERT INTO train (
        id,
        gender,
        ever_married,
        age,
        graduated,
        profession,
        work_experience,
        spending_score,
        family_size,
        var_1,
        segmentation
    ) VALUES (
        %s, /* id */
        %s, /* gender */
        %s, /* ever_married */
        %s, /* age */
        %s, /* graduated */
        %s, /* profession */
        %s, /* work_exp */
        %s, /* spending_score */
        %s, /* family_size */
        %s, /* var_1 */
        %s /* segmentation */
    );
"""

print(train_csv)

for index, row in train_csv.iterrows():
    cur.execute(sql, (
        row.ID,
        row.Gender,
        row.Ever_Married,
        row.Age,
        row.Graduated,
        row.Profession,
        row.Work_Experience,
        row.Spending_Score,
        row.Family_Size,
        row.Var_1,
        row.Segmentation,
    ))


sql = """
    INSERT INTO test (
        id,
        gender,
        ever_married,
        age,
        graduated,
        profession,
        work_experience,
        spending_score,
        family_size,
        var_1,
        segmentation_truth
    ) VALUES (
        %s, /* id */
        %s, /* gender */
        %s, /* ever_married */
        %s, /* age */
        %s, /* graduated */
        %s, /* profession */
        %s, /* work_exp */
        %s, /* spending_score */
        %s, /* family_size */
        %s, /* var_1 */
        %s /* segmentation_truth */
    );
"""

print(test_csv)

for index, row in test_csv.iterrows():
    cur.execute(sql, (
        row.ID,
        row.Gender,
        row.Ever_Married,
        row.Age,
        row.Graduated,
        row.Profession,
        row.Work_Experience,
        row.Spending_Score,
        row.Family_Size,
        row.Var_1,
        row.Segmentation,
    ))

conn.commit()
conn.close()

