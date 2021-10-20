import yaml
import os
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt

class Trainer:

    def create_df(self, name):
        self.df = pd.read_excel ('data\\'+name+'.xlsx')
    
    def add_moving_avg(self, ):
        self.df['moving'] = self.df.iloc[:,2].rolling(window=3).mean()
        self.df = self.df.dropna(subset=['moving']) # remove data points with null moving average
        print(self.df)



if __name__ == "__main__":

    script_dir = os.path.dirname(__file__)
    rel_path = "yamls\\training.yaml"
    abs_file_path = os.path.join(script_dir, rel_path)
    
    with open(abs_file_path, 'r') as f:
        config = yaml.safe_load(f)
    
    t = Trainer()
    t.create_df(config['training_stock'])
    t.add_moving_avg()