# Synthetic Dataset Generators

This repository provides a collection of **synthetic dataset generators** designed to support research in data structures, machine learning, data streams, and related areas.

The initial version of this repository includes three generators:

* **Diagonal Dataset**[^1]
* **k-d Tree Generator Dataset**
* **Varden Dataset** — Seed Spreader: Varying-density Dataset[^2]

These generators are currently being used in my research to investigate the behavior and performance of data structures under different data distributions and structural characteristics.

However, this repository is intended to be **more than a collection of datasets used in a single research project**. The goal is to provide an open and collaborative space where researchers can share synthetic dataset generators, document their properties, and contribute new generators for reproducible scientific experiments.

> **The goal is to make synthetic data generation more transparent, reproducible, and accessible to researchers.**

## Research

The datasets in this repository are used in the following research projects:

* *[Add research papers, articles, or projects here]*

If you use one of these generators in your research, please cite the corresponding work and, whenever possible, report the parameters used to generate the data.

## How to Use the Generators

### Diagonal Dataset

Run:

```bash
python3 gen_ss_diagonal.py
```

### k-d Tree Generator Dataset

Run:

```bash
python3 gen_ss_kdtree.py
```

### Varden Dataset

Run:

```bash
./gen_ss_varden.sh -w 1 -g 1 -n 500000 -d 10 -v 1
```

The parameters can be adjusted according to the requirements of the experiment.

The Varden generator used in this repository is based on the implementation available in the **PKd-tree** repository.[^3] The original implementation and description of the Varden dataset are available through the ApproxDBSCAN project.[^4]

## Contributing

Contributions are welcome!

Researchers and developers are encouraged to contribute new **synthetic dataset generators**, improvements, documentation, and examples.

A useful contribution should, whenever possible, include:

* The dataset generator source code;
* A description of the data distribution;
* The characteristics or properties that the generator is intended to control;
* Instructions for generating the dataset;
* Examples of generated data;
* The parameters available in the generator;
* References to previous work, when applicable;
* Information required to reproduce the generated datasets.

The objective is not only to provide datasets, but also to make it possible for other researchers to understand **how the data was generated and why it has particular characteristics**.

### Adding a New Generator

When contributing a new generator, please create a directory containing the generator source code and a `README.md` describing its purpose, parameters, and generation process.

For example:

```text
generators/
├── diagonal/
│   ├── gen_diagonal.py
│   └── README.md
├── kdtree-gen/
│   ├── gen_kdtree.py
│   └── README.md
└── varden/
    ├── gen_varden.sh
    └── README.md
```

Contributors are encouraged to provide references to the original work whenever a generator is based on an existing dataset, algorithm, or implementation.

## References

[^1]: J. Gan and Y. Tao, ‘On the Hardness and Approximation of Euclidean DBSCAN’, ACM Trans. Database Syst., vol. 42, no. 3, pp. 1–45, Sep. 2017, doi: 10.1145/3083897.

[^2]: O. Procopiuc, P. K. Agarwal, L. Arge, and J. S. Vitter, ‘Bkd-Tree: A Dynamic Scalable kd-Tree’, in Advances in Spatial and Temporal Databases, vol. 2750, T. Hadzilacos, Y. Manolopoulos, J. Roddick, and Y. Theodoridis, Eds, in Lecture Notes in Computer Science, vol. 2750. , Berlin, Heidelberg: Springer Berlin Heidelberg, 2003, pp. 46–65. doi: 10.1007/978-3-540-45072-6_4.

[^3]: Z. Men, Z. Shen, Y. Gu, and Y. Sun, ‘Parallel kd-tree with Batch Updates’, Proc. ACM Manag. Data, vol. 3, no. 1, p. 62:1-62:26, Feb. 2025, doi: 10.1145/3709712.

[^4]: https://sites.google.com/view/approxdbscan