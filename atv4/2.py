from pyscipopt import Model

if __name__ == "__main__":

    b1, b2, b3, b4 = map(float, input().split())

    if b1 < 0 or b2 < 0 or b3 < 0 or b4 < 0:
        print("INFACTÍVEL")
    
    else:
        model = Model("Atividade_3.2")

        # Definindo as variáveis de decisão
        x1 = model.addVar(vtype="C", lb=0, name="x1")
        x2 = model.addVar(vtype="I", lb=0, name="x2")

        # Função objetivo
        model.setObjective(x1 + 2*x2, sense="maximize")

        # Restrições
        model.addCons(x1 + x2 <= 15, name="Restricao_1")
        model.addCons(x1 <= 10, name="Restricao_2")
        model.addCons(x2 <= b, name="Restricao_3")

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