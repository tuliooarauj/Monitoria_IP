def calculo_da_efetividade(tipo, tipo_adversario, efetividade):
    # pokemon fogooo
    if tipo == "fogo" and tipo_adversario == "agua":
        efetividade[0] = 0.5
    elif tipo == "fogo" and tipo_adversario == "grama":
        efetividade[0] = 2
    elif tipo == "fogo" and (tipo_adversario == "fogo" or tipo_adversario == "normal"):
        efetividade[0] = 1

    # aguaaaaa
    elif tipo == "agua" and tipo_adversario == "grama":
        efetividade[0] = 0.5
    elif tipo == "agua" and tipo_adversario == "fogo":
        efetividade[0] = 2
    elif tipo == "agua" and (tipo_adversario == "agua" or tipo_adversario == "normal"):
        efetividade[0] = 1
    
    # gramaaaa
    elif tipo == "grama" and tipo_adversario == "fogo":
        efetividade[0] = 0.5
    elif tipo == "grama" and tipo_adversario == "agua":
        efetividade[0] = 2
    elif tipo == "grama" and (tipo_adversario == "grama" or tipo_adversario == "normal"):
        efetividade[0] = 1

    # normal.
    elif tipo == "normal":
        efetividade[0] = 1


def calculo_de_dano(nivel, poder, defesa_adversario, poder_do_ataque, efetividade):
    dano = ((((2* nivel) + 10) / 250) * (poder/defesa_adversario * poder_do_ataque) + 2) * (efetividade)
    return int(dano)


def entrada_tratada(entrada):
    partes = entrada.split(", ")
    nome, tipo, nivel, vida, poder, defesa, velocidade, nome_do_ataque, poder_do_ataque = partes
    return nome, tipo, int(nivel), int(vida), int(poder), int(defesa), int(velocidade), nome_do_ataque, int(poder_do_ataque)


# vamos vê o seu poke poke
entrada_informacoes_pokemon = input()
pokemon = entrada_tratada(entrada_informacoes_pokemon)
nome, tipo, nivel, vida, poder, defesa, velocidade, nome_do_ataque, poder_do_ataque = pokemon
vida_total = vida
print(f"escolho você {nome}")


combate_em_andamento = False

while not combate_em_andamento:
    comando = input()
    if comando == "um pokemon selvagem aparece!" or comando == "Equipe Rocket!":
        print("vamo botar pra quebrar!" if comando == "um pokemon selvagem aparece!" else f"{nome}, bora acabar com a raça desses bandidos e salvar o professor!")
        entrada_pokemon_adversario = input()
        pokemon_adversario = entrada_tratada(entrada_pokemon_adversario)
        nome_adversario, tipo_adversario, nivel_adversario, vida_adversario, poder_adversario, defesa_adversario, velocidade_adversario, nome_ataque_adversario, poder_ataque_adversario = pokemon_adversario
        vida_adversario_total = vida_adversario
        combate_em_andamento = True

    elif comando == "atacar" and combate_em_andamento:
        if velocidade >= velocidade_adversario:
            atacante, defensor = pokemon, pokemon_adversario
        else:
            atacante, defensor = pokemon_adversario, pokemon

        efetividade = calculo_da_efetividade(atacante[1], defensor[1])
        dano = calculo_de_dano(atacante[2], atacante[4], defensor[5], atacante[8], efetividade)
        defensor[3] -= dano

        if defensor[3] < 0:
            defensor[3] = 0

        print()
        print(f"{atacante[0]} usou {atacante[7]}")
        if efetividade == 2:
            print("foi super efetivo!")
        elif efetividade == 0.5:
            print("não foi muito efetivo")
        print(f"HP: {atacante[3]}/{vida_total}")
        print(f"HP inimigo: {defensor[3]}/{vida_adversario_total}")

        if defensor[3] == 0:
            print(f"{defensor[0]} derrotado!")
        if defensor[0] == nome:
            print("Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.")
        else:
            print(f"Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {nome}?")
            combate_em_andamento = False

        pokemon, pokemon_adversario = pokemon_adversario, pokemon

    elif comando == "correr" and combate_em_andamento:
        if nome_adversario == "Equipe Rocket!":
            print("lascou, eles não largam do meu pé!")
        else:
            print("ufa, consegui meter o pé!")
            combate_em_andamento = False