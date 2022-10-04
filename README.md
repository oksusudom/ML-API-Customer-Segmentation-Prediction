Customer Segmentation Prediction
===============================



## 프로젝트 배경
- 고객별 마케팅 전략 수립을 위해서는 고객 세분화가 필수적으로 여겨진다.

- 프로젝트에 사용된 데이터는 고객 정보(성별, 결혼 여부, 연령, 대학 졸업 여부, 직종, 경력 연차, 소비 점수, 가족 구성원 수 등)를 통해 고객을 A,B,C,D로 분류하는 목표를 가지고 있다.

- 데이터 분석을 통해 어떤 기준으로 A,B,C,D로 분류되는지 살펴보고


## 문제 정의

## 데이터셋 설명
Kaggle의 [Customer Segmentation](https://www.kaggle.com/datasets/vetrirah/customer) 데이터셋.

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