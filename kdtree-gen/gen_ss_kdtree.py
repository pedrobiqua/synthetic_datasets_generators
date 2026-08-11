from typing import Optional

import numpy as np

class Node:
    def __init__(
        self,
        depth,
        split_dim=None,
        split_value=None,
        left: Optional["Node"]=None,
        right: Optional["Node"]=None,
        left_ratio=0.5,
    ):
        """
        Parameters
        ----------
        depth : int
            Profundidade do nó.

        split_dim : int
            Dimensão usada no split.

        split_value : float
            Valor do corte.

        left_ratio : float
            Percentual de pontos que devem ir para o filho esquerdo.

        left/right : Node
            Filhos.
        """

        self.depth = depth
        self.split_dim = split_dim
        self.split_value = split_value

        self.left = left
        self.right = right

        self.left_ratio = left_ratio

    @property
    def is_leaf(self):
        return self.left is None and self.right is None

def create_leaf(depth: int) -> Node:
    return Node(depth=depth)

def create_tree(
    n_dimensions: int,
    split_value=0.5,
    left_ratio=0.1
) -> Node | None:

    root: Optional["Node"] = None
    current: Optional["Node"] = None

    for depth in range(n_dimensions):

        node = Node(
            depth=depth,
            split_dim=depth % n_dimensions,
            split_value=split_value,
            left_ratio=left_ratio
        )

        # primeiro nó criado
        if root is None:
            root = node
        else:
            assert current is not None
            current.right = node

        # ramo esquerdo termina aqui
        node.left = create_leaf(depth + 1)

        # continuamos pelo ramo direito
        current = node


    # depois do último split,
    # o ramo direito também precisa terminar
    assert current is not None
    current.right = create_leaf(n_dimensions + 1)

    return root



def generate_points(
    node,
    n_points,
    n_dimensions,
    bounds=None,
    seed=None
):
    """
    Gera pontos a partir de uma árvore de cortes.

    Parameters
    ----------
    node : Node
        Raiz da árvore.

    n_points : int
        Quantidade total de pontos.

    n_dimensions : int
        Número de dimensões.

    bounds : list
        Intervalos atuais de cada dimensão.

    Returns
    -------
    np.ndarray
        Pontos gerados.
    """

    rng = np.random.default_rng(seed)

    if bounds is None:
        bounds = [
            (0.0, 1.0)
            for _ in range(n_dimensions)
        ]


    # Caso folha: gera os pontos dentro da região
    if node.is_leaf:

        points = np.zeros(
            (n_points, n_dimensions)
        )

        for dim, (low, high) in enumerate(bounds):
            points[:, dim] = rng.uniform(
                low,
                high,
                size=n_points
            )

        return points


    # Divide quantidade de pontos
    n_left = int(
        n_points * node.left_ratio
    )

    n_right = n_points - n_left


    # Copia limites
    left_bounds = bounds.copy()
    right_bounds = bounds.copy()


    dim = node.split_dim
    split = node.split_value


    # Esquerda: x_dim < split
    low, high = left_bounds[dim]
    left_bounds[dim] = (
        low,
        split
    )


    # Direita: x_dim >= split
    low, high = right_bounds[dim]
    right_bounds[dim] = (
        split,
        high
    )


    left_points = generate_points(
        node.left,
        n_left,
        n_dimensions,
        left_bounds,
        seed=int(rng.integers(0, 10**9))
    )


    right_points = generate_points(
        node.right,
        n_right,
        n_dimensions,
        right_bounds,
        seed=int(rng.integers(0, 10**9))
    )


    return np.vstack(
        [
            left_points,
            right_points
        ]
    )

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

### Criação da estrutura de teste
n_points = 100000
n_dimensions = 20

root = create_tree(n_dimensions)

### Geração dos dados com base na estrutura
X = generate_points(
    root,
    n_points=n_points,
    n_dimensions=n_dimensions,
    seed=42
)


# exemplo de classe
y = np.zeros(len(X), dtype=int)


save_arff(
    X,
    "adversarial_stream.arff",
    relation_name="kdtree_worst_case",
    y=y
)