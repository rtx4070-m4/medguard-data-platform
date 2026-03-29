
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class MortalityModel:

    def train(self,df):

        X=df[['age']]
        y=(df['age']>70).astype(int)

        model=RandomForestClassifier()
        model.fit(X,y)

        return model
