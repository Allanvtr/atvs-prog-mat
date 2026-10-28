from pyscipopt import Model

if __name__ == "__main__":

    c = int(input())

    model = Model("Atividade_3.1")

    # Definindo as variáveis de decisão
    x1 = model.addVar(vtype="C", lb=0, name="x1")
    x2 = model.addVar(vtype="I", lb=0, name="x2")

    # Função objetivo
    model.setObjective(c*x1 + (c + 4)*x2, sense="maximize")

    # Restrições
    model.addCons(10*x1 + 18*x2 <= 52, name="Restricao_1")
    model.addCons(-1*x1 + x2 <= 2, name="Restricao_2")

    # Esconde os logs
    model.hideOutput()

    # Realiza o cálculo
    model.optimize()

    resultado = model.getObjVal()

    print(round(resultado, 2))
    print(round(model.getVal(x1), 2))
    print(round(model.getVal(x2), 2))