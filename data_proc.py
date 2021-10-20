import yaml
import os
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def extract_yahoo(tickers, inter):
    period = (int(time.mktime(datetime.datetime(2021, 8, 1, 23, 59).timetuple())),int(time.mktime(datetime.datetime(2021, 9, 1, 23, 59).timetuple())))
    for t in tickers:
        pre_df = f'https://query1.finance.yahoo.com/v7/finance/download/{t}?period1={period[0]}&period2={period[1]}&interval={inter}&events=history&includeAdjustedClose=true'
        df = pd.read_csv(pre_df)
        script_dir = os.path.dirname(__file__) 
        rel_path = "data\\" +t+".xlsx"
        abs_file_path = os.path.join(script_dir, rel_path)
        with pd.ExcelWriter(abs_file_path) as writer:
            df.to_excel(writer)
    print('done')
    
def visualize(name):
    df = pd.read_excel ('data\\'+name+'.xlsx')
    df.plot(x =0, y=2, kind = 'line') #open
    df.plot(x =0, y=3, kind = 'line') #high    
    df.plot(x =0, y=4, kind = 'line') #low
    df.plot(x =0, y=5, kind = 'line') #close
    plt.show()

if __name__ == "__main__":

    script_dir = os.path.dirname(__file__)
    rel_path = "yamls\data_extract.yaml"
    abs_file_path = os.path.join(script_dir, rel_path)
    
    with open(abs_file_path, 'r') as f:
        config = yaml.safe_load(f)
    if config['extract_data']:
        extract_yahoo(config['stocks'], config['interval'])
    else:
        visualize(config['vis_data_name'])
    