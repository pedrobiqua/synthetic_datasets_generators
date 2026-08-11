import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

n = 100_000

x = np.arange(n)
y = x
z = x


df = pd.DataFrame({
    0: x,
    1: y,
    2: z,
    "class": 1
})

df = pd.DataFrame({
    "x": x,
    "y": y,
    "z": z,
    "class": 1
})

# Salvar em ARFF
with open(f"diagonal/diagonal_{n}_3d.arff", "w") as f:
    f.write("@RELATION diagonal\n\n")
    f.write("@ATTRIBUTE x NUMERIC\n")
    f.write("@ATTRIBUTE y NUMERIC\n")
    f.write("@ATTRIBUTE z NUMERIC\n")
    f.write("@ATTRIBUTE class NUMERIC\n\n")
    f.write("@DATA\n")

    df.to_csv(
        f,
        sep=",",
        index=False,
        header=False
    )

# Plot 3D
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection="3d")

# ax.scatter(
#     df["x"],
#     df["y"],
#     df["z"],
#     s=1
# )

# ax.set_xlabel("Dimension 1")
# ax.set_ylabel("Dimension 2")
# ax.set_zlabel("Dimension 3")

# plt.show()