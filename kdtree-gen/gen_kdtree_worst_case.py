import random
from typing import List

import numpy as np

def save_arff(
    X,
    filename,
    relation_name="adversarial_kdtree",
    y=None
):
    """
    Salva uma matriz de dados no formato ARFF.

    Parameters
    ----------
    X : np.ndarray
        Matriz (n_amostras, n_dimensoes).

    filename : str
        Caminho do arquivo .arff.

    relation_name : str
        Nome da relação ARFF.

    y : np.ndarray, optional
        Classe binária dos exemplos.
        Valores esperados: 0 ou 1.
    """

    X = np.asarray(X)

    n_samples, n_features = X.shape

    if y is None:
        y = np.random.randint(
            0,
            2,
            size=n_samples
        )

    y = np.asarray(y)

    if len(y) != n_samples:
        raise ValueError(
            "Quantidade de classes diferente da quantidade de amostras"
        )

    if not np.all(np.isin(y, [0, 1])):
        raise ValueError(
            "A classe deve ser binária (0 ou 1)"
        )


    with open(filename, "w") as f:

        # Cabeçalho
        f.write(
            f"@RELATION {relation_name}\n\n"
        )

        # Atributos
        for i in range(n_features):
            f.write(
                f"@ATTRIBUTE x{i+1} NUMERIC\n"
            )

        f.write(
            "@ATTRIBUTE class {0,1}\n\n"
        )

        # Dados
        f.write("@DATA\n")

        for row, label in zip(X, y):

            values = ",".join(
                f"{v:.8f}"
                for v in row
            )

            f.write(
                f"{values},{label}\n"
            )

def generate_data(n_points: int, n_dimensions: int) -> List[List]:

    dataset = []
    for point in range(0, n_points):
        x = []
        for _ in range(0, n_dimensions):
            x.append(random.random())
        dataset.append(x)
        axis = point % n_dimensions
        x[axis] += 1

    return dataset

n_points = 100000
dimensions = [5, 10, 15, 20]
random.seed(1)

for d in dimensions:
    X = generate_data(n_points, d)
    y=np.zeros(len(X), dtype=int)
    save_arff(X, f"kdtree-{d}.arff", "kdtree_worst_case", y=y)