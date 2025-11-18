# Future Skills Lab – Sistema de Orientação de Carreira (GS 2025.2)

Projeto desenvolvido para a Global Solution 2025.2 (PCP) do 2º semestre do curso de Ciência da Computação.

O objetivo deste sistema é *organizar e analisar perfis profissionais do futuro, simulando uma ferramenta simples de orientação de carreiras, utilizando **Python orientado a objetos*, estruturas de dados (listas e dicionários) e uma lógica de recomendação baseada em competências.

---

## 1. Visão geral do sistema

O sistema é uma aplicação *CLI (linha de comando)* que:

- Cadastra um *perfil profissional* (nome, idade, objetivos);
- Coleta uma *autoavaliação de competências* (de 0 a 5) em:
  - Lógica de programação  
  - Criatividade  
  - Colaboração  
  - Adaptabilidade  
  - Comunicação  
  - Resolução de problemas
- Compara esse perfil com um conjunto de *carreiras do futuro* pré-cadastradas;
- Gera:
  - *Recomendações de carreiras* mais compatíveis;
  - *Trilhas de aprendizado* sugeridas;
  - *Áreas de aprimoramento* (competências que precisam ser fortalecidas).

> ⚠ *Ponto importante:*  
> As recomendações *não são feitas com base apenas no que o usuário escreve no campo de “objetivos”*.  
> Elas são calculadas *matematicamente, usando as **notas de competências* informadas pelo usuário.  
> Ou seja: o sistema pode sugerir uma carreira diferente do “sonho” inicial, com base nas habilidades que a pessoa demonstra hoje.

---

## 2. Conexão com o desafio proposto no PDF

De acordo com a descrição do desafio da GS:

- É necessário *desenvolver um sistema em Python orientado a objetos*;
- O sistema deve *organizar e analisar perfis profissionais do futuro*;
- Deve utilizar *listas, tuplas e/ou dicionários* para representar competências técnicas e comportamentais;
- A aplicação deve *gerar recomendações personalizadas* de:
  - carreiras,
  - trilhas de aprendizado,
  - áreas de aprimoramento;
- A proposta deve *conectar lógica de programação e automação* ao *desenvolvimento humano e profissional*.

Este projeto atende a esses pontos da seguinte forma:

1. Usa *POO* com as classes Perfil, Carreira e RecomendadorCarreira;
2. Representa competências e pesos usando *dicionários* e *listas*;
3. Implementa uma *lógica de pontuação* para comparar perfil x carreira;
4. Gera recomendações de carreira, trilhas e sugestões de desenvolvimento;
5. Mostra como *lógica de programação + estruturas de dados + condicional* podem ser usadas para orientar o desenvolvimento profissional para o futuro do trabalho.

---

## 3. Como a análise do perfil funciona (passo a passo)

A análise do perfil segue uma lógica *totalmente baseada em dados numéricos*, não apenas no texto digitado pelo usuário. O processo é:

1. *Cadastro do perfil*
   - O usuário informa:
     - nome
     - idade
     - objetivos (texto livre, ex.: “quero trabalhar com machine learning”)
   - O campo “objetivos” serve para *contextualização*, mas não entra diretamente na fórmula matemática.

2. *Autoavaliação das competências*
   - O sistema pergunta ao usuário notas de *0 a 5* para cada competência:
     - 0 = ainda não desenvolvida  
     - 5 = muito desenvolvida
   - Essas notas são armazenadas em um *dicionário*, por exemplo:

     python
     {
         "logica": 3,
         "criatividade": 4,
         "colaboracao": 5,
         "adaptabilidade": 4,
         "comunicacao": 5,
         "resolucao_problemas": 5,
     }
     

3. *Carreiras do futuro pré-cadastradas*
   - Cada carreira possui:
     - nome
     - area
     - descricao
     - competencias_relevantes (dicionário com pesos)
     - trilhas_aprendizado (lista de tópicos para estudar)
   - Exemplo simplificado de uma carreira:

     python
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
             "Python para análise de dados",
             "Visualização de dados",
             "Introdução a machine learning",
         ],
     )
     

4. *Cálculo de compatibilidade (matemática da recomendação)*

   A classe RecomendadorCarreira faz o seguinte:

   - Para cada carreira:
     - Lê as competências relevantes e seus *pesos* (importância);
     - Para cada competência:
       - Pega a nota do usuário (0 a 5);
       - Normaliza essa nota para um valor entre 0 e 1;
       - Multiplica pela importância (peso) naquela carreira;
     - Soma os resultados e divide pela soma dos pesos → gera uma *pontuação de 0 a 100*.

   Em termos simples:

   > *Quanto mais o perfil do usuário se aproxima das competências ideais de uma carreira, maior será a porcentagem de compatibilidade.*

   Isso significa que:

   - Se o usuário disser que quer “trabalhar com IA / machine learning”,  
     *mas tiver lógica relativamente baixa* e competências humanas muito fortes (comunicação, colaboração, criatividade),  
     o sistema pode:
       - listar *Cientista de Dados Júnior* entre as opções,
       - mas dar pontuação melhor, por exemplo, para *UX/UI Designer* ou *Especialista em Transformação Digital*,  
         dependendo das notas inseridas.

   Isso é um comportamento *esperado e coerente com o projeto*, pois:

   - O sistema está avaliando o *perfil de competências de hoje*,  
   - e não apenas o que o usuário deseja ser no futuro.

5. *Geração das recomendações*

   - As carreiras são ordenadas da *maior compatibilidade para a menor*;
   - São exibidas as *3 principais* com:
     - nome da carreira;
     - área;
     - compatibilidade estimada (%);
     - resumo (descrição);
     - trilhas implícitas (dentro de cada carreira);
     - mensagens de *sugestão de desenvolvimento*.

6. *Análise das áreas de aprimoramento*

   - Para cada carreira recomendada, o sistema verifica quais competências relevantes estão *abaixo de 4/5*;
   - Para essas competências, gera mensagens como:

     > "Fortaleça a competência 'logica' (atual: 3/5) para se aproximar do perfil ideal."

   Isso cria uma *ponte* entre:

   - a situação atual;
   - e o que o usuário precisa fortalecer para chegar na carreira desejada.

---

## 4. Tecnologias, conceitos e requisitos atendidos

- *Linguagem:*  
  - Python 3

- *Paradigma:*  
  - Programação Orientada a Objetos (POO)

- *Estruturas de dados utilizadas:*
  - *Listas*
  - *Dicionários*
  - (Opcionalmente, tuplas na definição das competências disponíveis)

- *Requisitos técnicos do desafio atendidos:*
  - Código em Python, organizado em *módulos e classes*;
  - Uso de *listas e dicionários* para estruturação e análise dos dados;
  - Classes, atributos e métodos para representar o modelo de dados:
    - Perfil
    - Carreira
    - RecomendadorCarreira
  - Funções e condicionais para:
    - ler entradas do usuário;
    - validar dados;
    - calcular pontuações;
    - gerar recomendações e orientações;
  - *Interface textual simples (CLI)*:
    - menu principal;
    - cadastro de perfil;
    - visualização de perfil;
    - geração de recomendações;
  - Projeto pronto para ser versionado em repositório público no GitHub.

---

## 5. Estrutura do projeto

```text
GS_python_2sem/
├─ main.py          # Ponto de entrada da aplicação (menu e fluxo principal)
├─ models.py        # Classes Perfil e Carreira (modelo de dados)
├─ data.py          # "Banco de dados" em memória com carreiras do futuro
├─ recommender.py   # Lógica de recomendação (RecomendadorCarreira)
└─ README.md        # Documentação do projeto