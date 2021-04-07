import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

count = 0

for i in range(1, 17):
  df = pd.read_csv(f"./tweets_4/equipo_{i}_fecha_5.csv")
  count += len(df.polarity.values)

for i in range(1, 17):
  df = pd.read_csv(f"./tweets_4/equipo_{i}_fecha_6.csv")
  count += len(df.polarity.values)

print(count)