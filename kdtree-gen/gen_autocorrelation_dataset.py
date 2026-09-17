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


def generate_data(n_points: int, n_dimensions: int, k_autocorrelation: int) -> List[List]:
    if n_dimensions < k_autocorrelation:
        print("n should be higher than k")
        return []

    dataset = []
    counter = 1
    for _ in range(0, n_points):
        x = []
        for _ in range(0, k_autocorrelation):
            x.append(counter)
        for _ in range(n_dimensions - k_autocorrelation):
            x.append(random.random())
        counter += 1

        dataset.append(x)


    return dataset

SEED = 1
np.random.seed(SEED)
random.seed(SEED)

n_points = 100000
d = 5
k_values = [1,2,3,4]

for k in k_values:
    X = generate_data(n_points, d, k)
    y=np.zeros(len(X), dtype=int)
    if X:
        save_arff(X, f"{d}_{k}.arff", "kdtree_worst_case", y=y)

    ### versão aleatória
    # X_shuffled = X.copy()
    # np.random.shuffle(X_shuffled)
    # save_arff(X_shuffled, f"random_{d}_{k}.arff", "kdtree_worst_case", y=y)

    ### versão alterando os blocos
    X_parted = X.copy()
    parted = np.array_split(X, 4)
    X_parted = np.concatenate([
        parted[3],
        parted[1],
        parted[0],
        parted[2]
    ])

    save_arff(X_parted, f"parted_{d}_{k}.arff", "kdtree_worst_case", y=y)
