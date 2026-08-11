import sys

oldpath = sys.argv[1]
newpath = sys.argv[2]

with open(oldpath, "r") as f:
    lines = f.readlines()

header = lines[0].split()
n = int(header[0])
d = int(header[1])

with open(newpath, "w") as f:
    # ARFF header
    f.write("@RELATION varden\n\n")

    for i in range(d):
        f.write(f"@ATTRIBUTE x{i + 1} NUMERIC\n")

    f.write("@ATTRIBUTE class NUMERIC\n\n")
    f.write("@DATA\n")

    # Dados
    for line in lines[1:]:
        values = line.split()

        # Remove o ID da primeira coluna
        values = values[1:]

        # Adiciona a classe 1
        values.append("1")

        f.write(",".join(values))
        f.write("\n")