

from models import Perfil, Carreira
class RecomendadorCarreira:
    def __init__(self, carreiras):
        # carreiras = lista de objetos Carreira
        self.carreiras = carreiras




    def _calcular_pontuacao(self, perfil, carreira):
        """
        Calcula uma pontuação de compatibilidade entre 0 e 100
        com base nas competências relevantes da carreira.
        """
        soma_pesos = 0
        soma_resultado = 0.0

        for comp, peso in carreira.competencias_relevantes.items():
            soma_pesos += peso
            nota_usuario = perfil.competencias.get(comp, 0)
            # Normaliza a nota do usuário (0 a 5) para 0 a 1
            aproveitamento = nota_usuario / 5.0
            soma_resultado += aproveitamento * peso

        if soma_pesos == 0:
            return 0.0

        return (soma_resultado / soma_pesos) * 100.0





    def recomendar(self, perfil, top_n=3):

        resultados = []

        for carreira in self.carreiras:
            pontuacao = self._calcular_pontuacao(perfil, carreira)
            resultados.append((carreira, pontuacao))

        # Ordena da maior para a menor pontuação
        resultados.sort(key=lambda item: item[1], reverse=True)
        return resultados[:top_n]


    def sugerir_melhorias(self, perfil, carreira):
        sugestoes = []

        for comp, peso in carreira.competencias_relevantes.items():
            nota = perfil.competencias.get(comp, 0)
            if nota < 4:  # abaixo de 4, sugerimos melhoria
                mensagem = (
                    f"Fortaleça a competência '{comp}' "
                    f"(atual: {nota}/5) para se aproximar do perfil ideal."
                )
                sugestoes.append(mensagem)

        if not sugestoes:
            sugestoes.append(
                "Seu perfil já está bem alinhado com essa carreira. Continue se desenvolvendo!"
            )

        return sugestoes