import sys  # Importação do módulo sys (não está sendo utilizado no código)

# Classe que define a base de conhecimento do sistema especialista
class Ontologia:
    def __init__(self):
        # Dicionário contendo as áreas do conhecimento, suas habilidades associadas e a pontuação mínima necessária
        self.areas = {
            "Exatas": {"habilidades": ["raciocínio lógico", "cálculo", "análise"], "pontos_minimos": 30},
            "Humanas": {"habilidades": ["comunicação", "escrita", "argumentação"], "pontos_minimos": 30},
            "Biológicas": {"habilidades": ["observação", "método científico", "dedicação"], "pontos_minimos": 30},
            "Sociais": {"habilidades": ["negociação", "estratégia", "análise de dados"], "pontos_minimos": 30},
        }

# Função que aplica o questionário ao usuário
def aplicar_questionario():
    # Lista de perguntas associadas a cada área do conhecimento
    perguntas = [
        ("Você gosta de resolver problemas matemáticos?", "Exatas"),
        ("Prefere ler e interpretar textos?", "Humanas"),
        ("Se interessa por biologia e ciências naturais?", "Biológicas"),
        ("Gosta de entender como funcionam os negócios e o mercado?", "Sociais"),
        ("Prefere trabalhar com números e cálculos complexos?", "Exatas"),
        ("Se sente confortável debatendo ideias e conceitos?", "Humanas"),
        ("Tem interesse em trabalhar com pesquisas laboratoriais?", "Biológicas"),
        ("Acha interessante o funcionamento da economia?", "Sociais"),
        ("Gosta de programar e criar soluções tecnológicas?", "Exatas"),
        ("Prefere escrever textos argumentativos e ensaios?", "Humanas"),
        ("Gosta de estudar o corpo humano e suas funções?", "Biológicas"),
        ("Tem interesse em trabalhar com marketing e publicidade?", "Sociais"),
        ("Acha interessante a física e suas aplicações?", "Exatas"),
        ("Gosta de ensinar e transmitir conhecimento?", "Humanas"),
        ("Prefere estudar química e suas interações?", "Biológicas"),
    ]
    
    # Dicionário que armazena a pontuação do usuário para cada área do conhecimento
    pontuacao = {"Exatas": 0, "Humanas": 0, "Biológicas": 0, "Sociais": 0}
    
    print("Responda as perguntas de 0 a 10 (sendo 0 = discordo totalmente e 10 = concordo totalmente):\n")
    
    # Loop que percorre todas as perguntas e coleta as respostas do usuário
    for pergunta, area in perguntas:
        while True:
            try:
                # Solicita ao usuário uma nota de 0 a 10 para cada pergunta
                resposta = int(input(f"{pergunta} (0-10): "))
                
                # Verifica se a resposta está dentro do intervalo permitido
                if 0 <= resposta <= 10:
                    pontuacao[area] += resposta  # Soma a pontuação à área correspondente
                    break  # Sai do loop de validação
                else:
                    print("Digite um valor entre 0 e 10.")  # Mensagem de erro caso o valor esteja fora do intervalo
            except ValueError:
                print("Entrada inválida! Digite um número entre 0 e 10.")  # Mensagem de erro caso a entrada não seja um número
    
    return pontuacao  # Retorna o dicionário de pontuações

# Classe principal do sistema especialista
class SistemaEspecialista:
    def __init__(self):
        self.ontologia = Ontologia()  # Criação da base de conhecimento
    
    # Determina qual área obteve a maior pontuação
    def determinar_area(self, pontuacoes):
        melhor_area = max(pontuacoes, key=pontuacoes.get)  # Retorna a área com a pontuação mais alta
        return melhor_area
    
    # Exibe os resultados da análise para o usuário
    def exibir_resultado(self, pontuacoes):
        melhor_area = self.determinar_area(pontuacoes)  # Obtém a área mais indicada
        
        print("\n🎯 Resultado Final:")
        print(f"A área mais indicada para você é: {melhor_area}")
        
        print("\n📊 Pontuação por área:")
        # Exibe a pontuação do usuário para cada área, indicando se atingiu o mínimo necessário
        for area, pontos in pontuacoes.items():
            pontos_minimos = self.ontologia.areas[area]['pontos_minimos']
            diferenca = max(0, pontos_minimos - pontos)  # Calcula quantos pontos faltam para o mínimo necessário
            print(f"{area}: {pontos} pontos (Mínimo necessário: {pontos_minimos}, Faltam {diferenca} pontos)")
        
        print("\n🎓 Cursos recomendados para essa área:")
        self.recomendar_cursos(melhor_area)  # Chama a função de recomendação de cursos
    
    # Recomenda cursos de acordo com a área determinada
    def recomendar_cursos(self, area):
        cursos = {
            "Exatas": [
                "Engenharia da Computação", "Ciência da Computação", "Matemática", "Engenharia Civil",
                "Sistemas de Informação", "Engenharia Elétrica", "Física", "Estatística", "Engenharia Mecânica",
                "Engenharia de Software", "Análise e Desenvolvimento de Sistemas", "Ciência de Dados"
            ],
            "Humanas": [
                "Psicologia", "Filosofia", "Direito", "Jornalismo", "História",
                "Letras", "Serviço Social", "Pedagogia", "Sociologia", "Teologia",
                "Ciências Políticas", "Antropologia", "Artes Cênicas", "Comunicação Social"
            ],
            "Biológicas": [
                "Medicina", "Biomedicina", "Enfermagem", "Nutrição", "Biologia",
                "Farmácia", "Fisioterapia", "Odontologia", "Educação Física", "Zootecnia",
                "Veterinária", "Biotecnologia", "Ecologia", "Ciências Ambientais"
            ],
            "Sociais": [
                "Administração", "Marketing", "Economia", "Relações Internacionais", "Gestão de RH",
                "Ciências Contábeis", "Publicidade e Propaganda", "Gestão Pública", "Logística", "Comércio Exterior",
                "Empreendedorismo", "Finanças", "Turismo", "Ciências Atuariais"
            ]
        }
        
        recomendados = cursos.get(area, [])  # Obtém a lista de cursos da área determinada
        for i, curso in enumerate(recomendados[:5], 1):  # Exibe até 5 cursos recomendados
            print(f"{i}. {curso}")

# Função principal do programa
def main():
    print("🎓 Bem-vindo ao Sistema Especialista de Escolha de Cursos! 🎓\n")
    
    pontuacoes = aplicar_questionario()  # Aplica o questionário ao usuário
    sistema = SistemaEspecialista()  # Cria uma instância do sistema especialista
    sistema.exibir_resultado(pontuacoes)  # Exibe o resultado baseado nas respostas do usuário

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal
