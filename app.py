import pandas as pd
import numpy as np

# url = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
df = pd.read_html(url, encoding="utf-8")[0]
data = df.values
data = np.delete(data, 0, axis=0)
data[:, 0] = data[:, 0].astype(int)
data[:, 2] = data[:, 2].astype(int)
sorted_indices = np.lexsort((data[:, 0], -data[:, 2]))
sorted_array = data[sorted_indices]

i, j = -1, sorted_array[0][2]
for v in sorted_array:
    if j > int(v[2]):
        print()
        i = -1
    print(" " * (int(v[0]) - i - 1), v[1], sep="", end="")
    i, j = int(v[0]), int(v[2])
