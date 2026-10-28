from pyscipopt import Model

if __name__ == "__main__":

    b1, b2, b3, b4 = map(float, input().split())

    model = Model("Atividade_3.2")

    # Definindo as variáveis de decisão
    x1 = model.addVar(vtype="C", lb=0, name="x1")
    x2 = model.addVar(vtype="I", lb=0, name="x2")

    # Função objetivo
    model.setObjective(x1 + 2*x2, sense="minimize")

    # Restrições
    model.addCons(-x1 + x2 >= b1, name="Restricao_1")
    model.addCons(x1 + x2 <= b2, name="Restricao_2")
    model.addCons(x1 >= b3, name="Restricao_3")
    model.addCons(x2 >= b4, name="Restricao_4")

    # Esconde os logs
    model.hideOutput()

    # Realiza o cálculo
    model.optimize()

    status = model.getStatus()

    if status == "infeasible":
        print("INFACTÍVEL")
    elif status == "unbounded":
        print("ILIMITADO")
    else:
        resultado = model.getObjVal()

        print(round(resultado, 2))
        print(round(model.getVal(x1), 2))
        print(round(model.getVal(x2), 2))