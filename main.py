from models import Perfil
from data import carregar_carreiras_padrao
from recomender import RecomendadorCarreira

#Aqui comecei a exibir as areas disponiveis puxando as variaveis formada
COMPETENCIAS_DISPONIVEIS = [
    ("logica", "Lógica de programação"),
    ("criatividade", "Criatividade"),
    ("colaboracao", "Colaboração"),
    ("adaptabilidade", "Adaptabilidade"),
    ("comunicacao", "Comunicação"),
    ("resolucao_problemas", "Resolução de problemas"),
]


def ler_inteiro(mensagem, minimo=None, maximo=None):




    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"Valor mínimo permitido é {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"Valor máximo permitido é {maximo}.")
                continue
            return valor
        except ValueError:
            print("Não foi possivel registrar.Por favor apenas Digite um número inteiro.")


def coletar_competencias():


    print("\nAvalie suas competências de 0 a 5:")
    print("0 = ainda não desenvolvida | 5 = muito desenvolvida\n")

    competencias_usuario = {}

    for chave, descricao in COMPETENCIAS_DISPONIVEIS:
        nota = ler_inteiro(f"{descricao}: ", minimo=0, maximo=5)
        competencias_usuario[chave] = nota

    return competencias_usuario


def cadastrar_perfil():
    print("\n=== Cadastro de Perfil ===")
    nome = input("Nome: ")
    idade = ler_inteiro("Idade: ", minimo=14, maximo=120)
    objetivos = input("Quais são seus objetivos profissionais para o futuro? ")

    competencias = coletar_competencias()

    perfil = Perfil(nome=nome, idade=idade, objetivos=objetivos, competencias=competencias)
    print("\nPerfil cadastrado com sucesso!\n")
    return perfil


def exibir_menu():
    print("=== Future Skills Lab - Orientação de Carreira ===")
    print("1. Cadastrar/atualizar meu perfil")
    print("2. Visualizar meu perfil")
    print("3. Gerar recomendações de carreira")
    print("4. Sair")
    return ler_inteiro("Escolha uma opção: ", minimo=1, maximo=4)





def main():
    carreiras = carregar_carreiras_padrao()
    recomendador = RecomendadorCarreira(carreiras)
    perfil = None



    while True:
        opcao = exibir_menu()

        if opcao == 1:
            perfil = cadastrar_perfil()
        elif opcao == 2:
            if perfil is None:
                print("\nNenhum perfil cadastrado. Cadastre um perfil primeiro.\n")
            else:
                print("\n=== Meu Perfil ===")
                print(perfil.resumo())
                print()
        elif opcao == 3:
            if perfil is None:
                print("\nNenhum perfil cadastrado. Cadastre um perfil primeiro.\n")
            else:
                print("\n=== Recomendações de Carreira ===")
                resultados = recomendador.recomendar(perfil)
                for carreira, pontuacao in resultados:
                    print(f"\nCarreira sugerida: {carreira.nome}")
                    print(f"Área: {carreira.area}")
                    print(f"Compatibilidade estimada: {pontuacao:.1f}%")
                    print("Resumo da carreira:")
                    print(f"  {carreira.descricao}")
                    print("\nPrincipais orientações de desenvolvimento:")
                    for sugestao in recomendador.sugerir_melhorias(perfil, carreira):
                        print(f"  - {sugestao}")
                print()
        elif opcao == 4:
            print("\nObrigado por utilizar o Future Skills Lab. Até a próxima!\n")
            break



if __name__ == "__main__":
    main()