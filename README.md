Customer Segmentation Prediction
===============================



## 프로젝트 배경

- 고관여 제품을 판매중인 회사들은 고객의 성향을 파악하여 세분화하고 새로운 아이템/서비스를 기획할 때 이를 반영하는 것이 필수적이다.

- 프로젝트에 사용된 데이터는 고객 정보(성별, 결혼 여부, 연령, 대학 졸업 여부, 직종, 경력 연차, 소비 점수, 가족 구성원 수 등)를 통해 고객을 A,B,C,D로 분류하는 목표를 가지고 있다. 

- 고객 그룹 예측에 앞서, 회사 내부에서 고객의 성향을 예측해 빠르게 대응할 수 있도록 돕는 API 서비스를 구축하는 것을 목표로 진행했다. 데이터베이스, 대시보드 제작, API서비스 개발 및 배포 등 기술적인 부분을 구현해보는 것을 중점으로 진행했다.

- **해당 프로젝트는 클라우드 데이터베이스인 PotgreSQL에 데이터를 저장, Metabase를 사용한 데이터분석용 대시보드 개발, Flask한 사용해 API 서비스 개발, Heroku를 사용한 서비스 배포 등 APi 서비스 구축이 중점입니다.**


## 문제 정의

- 가상의 자동차 회사 회원 데이터셋을 사용해, 고객을 A~D 그룹으로 분류하고 신규 고객에 대해 기존 데이터를 토대로 고객별 그룹을 예측하는 다중 분류 모델.

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


## 파이프라인
<img width="656" alt="파이프라인" src="https://user-images.githubusercontent.com/81462099/197112574-e0402b97-45b2-4459-bb35-966cabc0ebb2.png">

## Metabase 데이터분석용 대시보드
추가할 것.


## 서비스 시연
<img width="434" alt="api" src="https://user-images.githubusercontent.com/81462099/197116936-114d7938-1c09-41db-bd42-661deaae5e4a.png">

<img width="434" alt="api2" src="https://user-images.githubusercontent.com/81462099/197116946-6fe39f94-25bc-47a9-830c-6b71768077d4.png">


## 마무리

- API 개발 및 배포에 대한 전반적인 이해도를 올릴 수 있는 프로젝트였다.
- 짧은 기간에 진행된 프로젝이이기 때문에 분석에 깊이가 부족한 점이 아쉬웠다.
- 데이터를 크롤링하지 못한 점이 아쉽다.
- 다중분류에 대한 이해도가 부족했다. 추가 학습할 부분이다.
- HTML, CSS에 대한 경험이 없어 API 서비스 화면 구성에서 각 입력 구분하기 어려웠다.
