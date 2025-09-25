def cliente_ativo(cliente):
    return cliente[0]


def cliente_eh_premium(cliente):
    return cliente[1] == 'premium'


def produto_relevante(produto, categorias_validas):
    return produto[0] in categorias_validas


def valor_acima_minimo(valor, minimo):
    return valor > minimo


def calcular_desconto(cliente):
    compras = cliente[2]
    tempo = cliente[3]

    if compras > 5:
        return 0.2
    elif compras > 3:
        return 0.15
    elif compras > 1:
        return 0.1
    elif tempo > 10:
        return 0.05
    return 0


def aplicar_desconto(valor, desconto):
    return valor * (1 - desconto)


def deve_aplicar_desconto(opcoes):
    return opcoes[0]


def processar_produto(cliente, produto, configuracoes, opcoes):
    categorias_validas = configuracoes[0]
    valor_minimo = configuracoes[1]
    resultados = []

    if produto_relevante(produto, categorias_validas):
        if valor_acima_minimo(produto[1], valor_minimo):
            if deve_aplicar_desconto(opcoes):
                desconto = calcular_desconto(cliente)
                produto[2] = aplicar_desconto(produto[1], desconto)
            resultados.append(produto)
    return resultados


def processar_dados_clientes(clientes, configuracoes, opcoes):
    resultados = []
    for i, cliente in enumerate(clientes):
        if cliente_ativo(cliente) and cliente_eh_premium(cliente):
            for produto in cliente[4]:
                resultado = processar_produto(cliente, produto, configuracoes, opcoes)
                resultados.extend(resultado)

                # Caso especial: incluir produtos mesmo que irrelevantes, dependendo das opções
                if not produto_relevante(produto, configuracoes[0]) and opcoes[1] and i % 2 == 0:
                    resultados.append(produto)
    return resultados

if __name__ == "__main__":
    clientes_teste = [
        [
            True,
            'premium',
            6,
            15,
            [
                ['eletronicos', 1000, None],
                ['livros', 50, None]
            ]
        ]
    ]

    configuracoes_teste = [
        ['eletronicos', 'casa'],
        500
    ]

    opcoes_teste = [
        True,
        False
    ]

    resultado = processar_dados_clientes(
        clientes_teste, configuracoes_teste, opcoes_teste)
    print("Resultado do teste:")
    print(resultado)
