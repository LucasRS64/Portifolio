def raiz_quadrada_recursiva(n, estimativa=1.0, precisao=1e-12):
    if abs(estimativa * estimativa - n) <= precisao:
        return estimativa
    else:
        nova_estimativa = (estimativa + n / estimativa) / 2
        return raiz_quadrada_recursiva(n, nova_estimativa, precisao)

def main():
    valores = [16, 25, 30, 50, 100]
    for valor in valores:
        resultado = raiz_quadrada_recursiva(valor)
        print(f"A raiz quadrada de {valor} é aproximadamente {resultado}")

if __name__ == "__main__":
    main()