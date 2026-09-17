import numpy as np


def generate_uniform(n, d, min_value=0.0, max_value=1.0):
    data = np.random.uniform(min_value, max_value, size=(n, d))

    return data

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


for x in range(1, 6):
    data = generate_uniform(n=100_000, d=5, min_value=0.0, max_value=1.0)
    save_arff(
        data,
        f"uniform_v{x}.arff",
        relation_name="kdtree_worst_case"
    )
