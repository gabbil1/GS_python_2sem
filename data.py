from models import Carreira



def carregar_carreiras_padrao():
    carreiras = [
        Carreira(
            nome="Desenvolvedor(a) Back-end",
            area="Tecnologia",
            descricao="Cria e mantém a parte lógica e de dados de sistemas e aplicações.",
            competencias_relevantes={
                "logica": 5,
                "resolucao_problemas": 5,
                "colaboracao": 3,
                "adaptabilidade": 3,
            },
            trilhas_aprendizado=[
                "Lógica de programação e estruturas de dados",
                "Python para back-end (APIs, frameworks web)",
                "Bancos de dados relacionais (SQL)",
                "Git e GitHub para controle de versão",
            ],
        ),
        Carreira(
            nome="Cientista de Dados Júnior",
            area="Tecnologia / Dados",
            descricao="Analisa dados e gera insights para apoiar decisões estratégicas.",
            competencias_relevantes={
                "logica": 5,
                "criatividade": 4,
                "resolucao_problemas": 5,
                "comunicacao": 4,
                "adaptabilidade": 3,
            },
            trilhas_aprendizado=[
                "Fundamentos de estatística",
                "Python para análise de dados (pandas, numpy)",
                "Visualização de dados",
                "Introdução a machine learning",
            ],
        ),
        Carreira(
            nome="UX/UI Designer",
            area="Tecnologia / Design",
            descricao="Projeta experiências e interfaces centradas no usuário.",
            competencias_relevantes={
                "criatividade": 5,
                "colaboracao": 4,
                "comunicacao": 4,
                "adaptabilidade": 3,
            },
            trilhas_aprendizado=[
                "Fundamentos de UX e pesquisa com usuários",
                "Ferramentas de prototipagem (Figma, etc.)",
                "Princípios de design de interfaces",
            ],
        ),
        Carreira(
            nome="Especialista em Transformação Digital",
            area="Negócios / Inovação",
            descricao="Conecta tecnologia, pessoas e processos para modernizar organizações.",
            competencias_relevantes={
                "adaptabilidade": 5,
                "colaboracao": 4,
                "comunicacao": 4,
                "criatividade": 3,
            },
            trilhas_aprendizado=[
                "Gestão de projetos ágeis (Scrum, Kanban)",
                "Fundamentos de transformação digital",
                "Habilidades de liderança e facilitação",
            ],
        ),
    ]

    return carreiras