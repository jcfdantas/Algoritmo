def verifica_listap(p):
    if not p or len(p) == 0:
        return 0

def verifica_petativo(p):
    return p[0]

def calcularpontospvacina(p):
    pontos = 0
    vacinas = p[3]
    if vacinas > 0:
        if vacinas > 10:
            pontos += 25
        elif vacinas > 5:
            pontos += 15
        elif vacinas > 2:
            pontos += 8
    return pontos

def verpetinconfig(p,c):
    especie = p[1]
    if especie not in c[0]:
        return False
    else:
        True
def calcular_status_pets(p, c, r, b=None, d=3):
    """
    Inicia a função com os parametros
    p = lista de pets
    c = configurações teste
    r = regras teste
    b = bonus teste
    d =
    """
    verifica_listap(p)

    total_pontos = 0

    for i in range(len(p)):
        pet = p[i]
        idade = pet[2]
        dono = pet[4]
        atv_extra = pet[5] if len(pet) > 5 else None

        if not verifica_petativo(p):
            continue

        if not verpetinconfig(p,c):
            continue

        if idade < c[1]:
            continue
        pontos = calcularpontospvacina(pet)
        pontos += idade

        
        if atv_extra:
            tipo = atv_extra[0]
            nota = atv_extra[1]
            if tipo == 'adestramento':
                if nota > 80:
                    pontos += 20
                elif nota > 60:
                    pontos += 10
                else:
                    pontos += 5
            elif tipo == 'competicao':
                pontos += nota * 0.2

        if b and i < len(b) and b[i]:
            tipo_bonus = b[i]
            if tipo_bonus == 'premiado':
                pontos *= 1.3
            elif tipo_bonus == 'adocao':
                pontos += 10
            elif tipo_bonus == 'resgate':
                pontos *= 1.1

        if pontos > 100:
            pontos = 100

        if r[0] and idade < c[1]:
            if len(r) > 1 and r[1]:
                idade_bonus = min(idade + 5, c[1])
                pontos = max(pontos, idade_bonus)
            elif len(r) > 2 and r[2] and vacinas > d:
                pontos += 5

        total_pontos += pontos

    media = total_pontos / len(p)

    if media > 90:
        media = min(media * 1.05, 100)
    elif media > 70:
        media *= 1.02

    return media


if __name__ == "__main__":

    pets_teste = [
        [True, 'cachorro', 5, 8, 'Carlos', ['adestramento', 90]],
        [True, 'gato', 3, 12, 'Ana', ['competicao', 70]],
        [False, 'passaro', 1, 2, 'Joao', None],
        [True, 'cachorro', 2, 0, 'Marina', ['adestramento', 65]]
    ]

    config_teste = [['cachorro', 'gato', 'passaro'], 2]

    regras_teste = [True, True, True]

    bonus_teste = ['premiado', 'resgate', None, 'adocao']

    resultado = calcular_status_pets(
        pets_teste, config_teste, regras_teste, bonus_teste)
    print("Média calculada:", resultado)