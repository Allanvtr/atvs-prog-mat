from pyscipopt import Model

if __name__ == "__main__":

    c = float(input())

    model = Model("Atividade_3.2")

    # Definindo as variáveis de decisão
    x1 = model.addVar(vtype="C", lb=0, name="x1")
    x2 = model.addVar(vtype="I", lb=0, name="x2")

    # Função objetivo
    model.setObjective(c*c*x1 + c*x2, sense="minimize")

    # Restrições
    model.addCons(5*x1 + x2 >= 100, name="Restricao_1")
    model.addCons(x1 - x2 <= 15, name="Restricao_2")

    # Esconde os logs
    model.hideOutput()

    # Realiza o cálculo
    model.optimize()

    if model.getStatus() == "unbounded":
        print("ILIMITADO")
    else:
        resultado = model.getObjVal()

        print(round(resultado, 2))
        print(round(model.getVal(x1), 2))
        print(round(model.getVal(x2), 2))