import time
import pandas as pd

df = pd.read_excel("velo.xlsx")

objets = []
masse_tot = 0
i = 0
C = 0.6

start_time = time.time()
while masse_tot+df["Masse"][i] <= C+1e-5:
    objets.append(df.iloc[i])
    masse_tot += df["Masse"][i]
    i += 1
end_time = time.time()

print(objets)
print()
print(masse_tot, "kg")
print(end_time-start_time, " s")
