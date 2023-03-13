import numpy as np
import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
from pgmpy.inference import VariableElimination

columns = {
    "age": {'meaning': 'age in years',
            'num': 3},
    "sex": {'meaning': 'sex (1 = male; 0 = female)',
            'num': 4},
    "cp": {'meaning': 'chest pain type 1: typical angina; 2: atypical angina; 3: non-anginal pain; 4: asymptomatic',
           'num': 9},
    "trestbps": {'meaning': 'resting blood pressure (in mm Hg on admission to the hospital)',
                 'num': 10},
    "chol": {'meaning': 'serum cholestoral in mg/dl',
             'num': 12},
    "fbs": {'meaning': '(fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)',
            'num': 16},
    "restecg": {'meaning': 'resting electrocardiographic results 0: normal; 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV); 2: showing probable or definite left ventricular hypertrophy by Estes criteria',
                'num': 19},
    "thalach": {'meaning': 'maximum heart rate achieved',
                'num': 32},
    "exang": {'meaning': 'exercise induced angina (1 = yes; 0 = no)',
              'num': 38},
    "oldpeak": {'meaning': 'ST depression induced by exercise relative to rest',
                'num': 40},
    "slope": {'meaning': 'the slope of the peak exercise ST segment 1: upsloping; 2: flat; 3: downsloping',
              'num': 41},
    "ca": {'meaning': 'number of major vessels (0-3) colored by flourosopy',
           'num': 44},
    "thal": {'meaning': '3 = normal; 6 = fixed defect; 7 = reversable defect',
             'num': 51},
    "num": {'meaning': 'diagnosis of heart disease (angiographic disease status) 0: < 50% diameter narrowing; 1: > 50% diameter narrowing',
            'num': 58},
}

df = pd.read_csv("Data/processed.cleveland.data", names=[i for i in columns.keys()])

df.age = df.age.astype(int)
df.sex = df.sex.astype(int)
df.cp = df.cp.astype(int)
df.trestbps = df.trestbps.astype(int)
df.chol = df.chol.astype(int)
df.fbs = df.fbs.astype(int)
df.restecg = df.restecg.astype(int)
df.thalach = df.thalach.astype(int)
df.exang = df.exang.astype(int)
df.slope = df.slope.astype(int)
df

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang', 'trestbps'),
                       ('trestbps', 'num'), ('chol', 'num'), ('fbs', 'num'),('num', 'restecg'),
                       ('num', 'thalach'), ('num', 'cp'),('num', 'exang'), ('num', 'oldpeak'), ('num', 'slope'),
                       ('num', 'ca'), ('num', 'thal')])

# Estimador de máxima verosimilitud
model.fit(df, estimator=MaximumLikelihoodEstimator)

# Estimador bayesiano
#model.fit(data, estimator=BayesianEstimator, prior_type='K2')

# ajustar el modelo a los datos
model.fit(df, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)

# predicción para una nueva muestra
q = infer.query(variables=['num'], evidence={'age': 28, 'sex': 1, 'cp': 1, 'trestbps': 130, 'chol': 250,
                                                      'fbs': 0, 'restecg': 0, 'thalach': 130, 'exang': 0,
                                                      'oldpeak': 1.6, 'slope': 2, 'ca': 0, 'thal': 3})

print(q['heartdisease'])

