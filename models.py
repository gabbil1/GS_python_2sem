class Perfil:
    def __init__(self, nome, idade, objetivos, competencias):
        # competencias = dicionário, ex: {"logica": 5, "criatividade": 3}
        self.nome = nome
        self.idade = idade
        self.objetivos = objetivos
        self.competencias = competencias




    def resumo(self):
        linhas = [
            f"Nome: {self.nome}",
            f"Idade: {self.idade}",
            f"Objetivos: {self.objetivos}",
            "Competências:",
        ]
        for chave, valor in sorted(self.competencias.items(),
                                   key=lambda item: item[1],
                                   reverse=True):
            linhas.append(f"  - {chave}: {valor}/5")
        return "\n".join(linhas)


class Carreira:
    def __init__(self, nome, area, descricao, competencias_relevantes, trilhas_aprendizado=None):
        self.nome = nome
        self.area = area
        self.descricao = descricao
        self.competencias_relevantes = competencias_relevantes
        self.trilhas_aprendizado = trilhas_aprendizado or []

    def resumo(self):
        linhas = [
            f"Carreira: {self.nome}",
            f"Área: {self.area}",
            f"Descrição: {self.descricao}",
            "Competências mais importantes:",
        ]
        for chave, peso in sorted(self.competencias_relevantes.items(),
                                  key=lambda item: item[1],
                                  reverse=True):
            linhas.append(f"  - {chave} (peso {peso})")

        if self.trilhas_aprendizado:
            linhas.append("Trilhas de aprendizado sugeridas:")
            for trilha in self.trilhas_aprendizado:
                linhas.append(f"  - {trilha}")

        return "\n".join(linhas)