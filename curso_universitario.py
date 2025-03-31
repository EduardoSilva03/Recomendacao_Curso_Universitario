import sys

class Ontologia:
    def __init__(self):
        self.areas = {
            "Exatas": {"habilidades": ["raciocínio lógico", "cálculo", "análise"], "pontos_minimos": 30},
            "Humanas": {"habilidades": ["comunicação", "escrita", "argumentação"], "pontos_minimos": 30},
            "Biológicas": {"habilidades": ["observação", "método científico", "dedicação"], "pontos_minimos": 30},
            "Sociais": {"habilidades": ["negociação", "estratégia", "análise de dados"], "pontos_minimos": 30},
        }

def aplicar_questionario():
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
    
    pontuacao = {"Exatas": 0, "Humanas": 0, "Biológicas": 0, "Sociais": 0}
    
    print("Responda as perguntas de 0 a 10 (sendo 0 = discordo totalmente e 10 = concordo totalmente):\n")
    for pergunta, area in perguntas:
        while True:
            try:
                resposta = int(input(f"{pergunta} (0-10): "))
                if 0 <= resposta <= 10:
                    pontuacao[area] += resposta
                    break
                else:
                    print("Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número entre 0 e 10.")
    
    return pontuacao

class SistemaEspecialista:
    def __init__(self):
        self.ontologia = Ontologia()
    
    def determinar_area(self, pontuacoes):
        melhor_area = max(pontuacoes, key=pontuacoes.get)
        return melhor_area
    
    def exibir_resultado(self, pontuacoes):
        melhor_area = self.determinar_area(pontuacoes)
        print("\n🎯 Resultado Final:")
        print(f"A área mais indicada para você é: {melhor_area}")
        
        print("\n📊 Pontuação por área:")
        for area, pontos in pontuacoes.items():
            pontos_minimos = self.ontologia.areas[area]['pontos_minimos']
            diferenca = max(0, pontos_minimos - pontos)
            print(f"{area}: {pontos} pontos (Mínimo necessário: {pontos_minimos}, Faltam {diferenca} pontos)")
        
        print("\n🎓 Cursos recomendados para essa área:")
        self.recomendar_cursos(melhor_area)
    
    def recomendar_cursos(self, area):
        cursos = {
            "Exatas": ["Engenharia da Computação", "Ciência da Computação", "Matemática", "Engenharia Civil", "Sistemas de Informação"],
            "Humanas": ["Psicologia", "Filosofia", "Direito", "Jornalismo", "História"],
            "Biológicas": ["Medicina", "Biomedicina", "Enfermagem", "Nutrição", "Biologia"],
            "Sociais": ["Administração", "Marketing", "Economia", "Relações Internacionais", "Gestão de RH"]
        }
        
        recomendados = cursos.get(area, [])
        for i, curso in enumerate(recomendados[:5], 1):
            print(f"{i}. {curso}")

def main():
    print("🎓 Bem-vindo ao Sistema Especialista de Escolha de Cursos! 🎓\n")
    pontuacoes = aplicar_questionario()
    sistema = SistemaEspecialista()
    sistema.exibir_resultado(pontuacoes)

if __name__ == "__main__":
    main()