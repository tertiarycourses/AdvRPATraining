import pandas as pd
import numpy as np

def filtercsv():
    df = pd.read_csv('E:\\_Training\\RPA_UiPath_Adv\\code\\AdvRPACode_V1\\Modele5_2_PythonPamdas\\score.csv')
    print(df)
    elderly = df[df.age > 50]
    print(elderly)
    elderly.to_csv("E:\\_Training\\RPA_UiPath_Adv\\code\\AdvRPACode_V1\\Modele5_2_PythonPamdas\\result.csv",sep=',')
    return "done"
