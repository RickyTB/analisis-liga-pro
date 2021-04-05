import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from utils import load_json

teams = load_json("data/teams.json")
matches = load_json('data/matches.json')

positives = []
negatives = []

for i in range(1, 17):
    df = pd.read_csv(f"./tweets_3/equipo_{i}_fecha_5.csv")
    values = df.polarity.values

    unique_elements, counts_elements = np.unique(values, return_counts=True)
    positives.append(counts_elements[2] * 100 / len(values))
    negatives.append(counts_elements[0] * -100 / len(values))

results = np.arange(16)

for match in matches:
    local_id = match["localTeam"]
    visitor_id = match["visitorTeam"]
    local_score = match["localScore"]
    visitor_score = match["visitorScore"]
    results[local_id - 1] = local_score - visitor_score
    results[visitor_id - 1] = visitor_score - local_score

results = results * 10

ind = np.arange(16)  # the x locations for the groups
width = 0.35  # the width of the bars: can also be len(x) sequence
labels = [teams[str(i)]["shortName"] for i in np.arange(1, 17)]

fig, ax = plt.subplots()

p1 = ax.bar(ind, positives, width, label="Positivo", color="#6bd425")
p2 = ax.bar(ind, negatives, width, label="Negativo", color="#db1f48")
p3 = ax.plot(ind, results, 'o', label="Resultado del partido", color="#2176ae")
ax.plot(ind, results, '-', color="#2176ae50")

ax.axhline(0, color="grey", linewidth=0.8)
ax.set_ylabel("% del total de tweets")
ax.set_title(
    "Sentimiento de Tweets por Equipo Previo a los Partidos de la Fecha 5 LigaPro 2021"
)
ax.set_xticks(ind)
ax.set_xticklabels(labels)
for tick in ax.get_xticklabels():
    tick.set_rotation(25)
ax.legend()

# Label with label_type 'center' instead of the default 'edge'
ax.bar_label(p1, label_type='center', fmt='%.0f%%')
ax.bar_label(p2, label_type='center', fmt='%.0f%%', color="white")
#ax.bar_label(p2)

plt.show()
