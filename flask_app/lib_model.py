import pickle
import pandas as pd


def get_model():
    model = None
    
    with open('model.pkl', 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    return model

def predict(age, graduated, profession, spending_score):
    X_test = pd.DataFrame([[None, None, age, graduated, profession, None, spending_score, None, None]])
    X_test.columns = ('Gender', 'Ever_Married', 'Age', 'Graduated', 'Profession', 
    'Work_Experience','Spending_Score', 'Family_Size', 'Var_1')
    print(X_test)
    return get_model().predict(X_test)
