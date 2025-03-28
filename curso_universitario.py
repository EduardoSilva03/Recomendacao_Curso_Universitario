# ===== ONTOLOGIA =====
class Ontologia:
    def __init__(self):
        self.areas = {
            "Exatas": {
                "subareas": ["Engenharia", "Matemática", "Computação", "Física"],
                "relacionadas": ["Tecnologia", "Ciências Naturais"],
                "habilidades": ["raciocínio lógico", "cálculo", "análise"]
            },
            "Humanas": {
                "subareas": ["Direito", "História", "Filosofia", "Psicologia"],
                "relacionadas": ["Sociais", "Educação"],
                "habilidades": ["comunicação", "escrita", "argumentação"]
            },
            "Biológicas": {
                "subareas": ["Medicina", "Biomedicina", "Farmácia", "Biologia"],
                "relacionadas": ["Saúde", "Ciências Naturais"],
                "habilidades": ["observação", "método científico", "dedicação"]
            },
            "Sociais": {
                "subareas": ["Administração", "Economia", "Marketing", "Relações Internacionais"],
                "relacionadas": ["Humanas", "Tecnologia"],
                "habilidades": ["negociação", "estratégia", "análise de dados"]
            }
        }

# ===== FRAMES =====
class CursoFrame:
    def __init__(self, nome, area, duracao, modalidade, habilidades, mercado):
        self.nome = nome
        self.area = area
        self.duracao = duracao  # Em anos
        self.modalidade = modalidade  # Presencial, EAD ou Híbrido
        self.habilidades = habilidades  # Habilidades essenciais para o curso
        self.mercado = mercado  # Nível de empregabilidade esperado (0-10)

# ===== LÓGICA FUZZY =====
class LogicaFuzzy:
    @staticmethod
    def calcular_similaridade_area(areas_usuario, area_curso, ontologia):
        """Calcula a compatibilidade entre as áreas de interesse do aluno e a área do curso"""
        if area_curso in areas_usuario:
            return 1.0
        for area in areas_usuario:
            if area in ontologia.areas and area_curso in ontologia.areas[area].get("relacionadas", []):
                return 0.7
        return 0.3  # Baixa compatibilidade se não estiver relacionado

    @staticmethod
    def calcular_afinidade_habilidades(habilidades_usuario, habilidades_curso):
        """Calcula a afinidade do aluno com as habilidades exigidas pelo curso"""
        if not habilidades_usuario or not habilidades_curso:
            return 0.5  # Valor neutro

        correspondencias = sum(1 for h in habilidades_usuario if h in habilidades_curso)
        return correspondencias / len(habilidades_curso)

    @staticmethod
    def calcular_relevancia_mercado(mercado_minimo, mercado_curso):
        """Avalia a empregabilidade do curso conforme a exigência do aluno"""
        if mercado_curso < mercado_minimo:
            return 0.0  # Descartar cursos abaixo do mínimo de mercado
        return 1.0

    @staticmethod
    def calcular_pontuacao_final(similaridade_area, afinidade_habilidades, relevancia_mercado):
        """Combina os critérios para determinar a recomendação do curso"""
        return (0.5 * similaridade_area) + (0.3 * afinidade_habilidades) + (0.2 * relevancia_mercado)

# ===== BASE DE CONHECIMENTO =====
def criar_base_cursos():
    return [
    CursoFrame("Engenharia da Computação", "Exatas", 5, "Presencial", ["raciocínio lógico", "cálculo", "programação"], 9),
    CursoFrame("Psicologia", "Humanas", 5, "Presencial", ["comunicação", "empatia", "análise comportamental"], 8),
    CursoFrame("Biomedicina", "Biológicas", 4, "Presencial", ["método científico", "observação", "laboratório"], 7),
    CursoFrame("Administração", "Sociais", 4, "Híbrido", ["negociação", "estratégia", "liderança"], 8),
    CursoFrame("Matemática", "Exatas", 4, "EAD", ["cálculo", "raciocínio lógico", "abstração"], 6),
    CursoFrame("Direito", "Humanas", 5, "Presencial", ["argumentação", "escrita", "comunicação"], 7),
    CursoFrame("Ciência da Computação", "Exatas", 4, "Presencial", ["programação", "cálculo", "pensamento lógico"], 9),
    CursoFrame("Arquitetura", "Exatas", 5, "Presencial", ["desenho técnico", "criatividade", "construção"], 8),
    CursoFrame("Enfermagem", "Biológicas", 4, "Presencial", ["atenção ao paciente", "procedimentos clínicos", "trabalho em equipe"], 7),
    CursoFrame("Marketing", "Sociais", 4, "Híbrido", ["estratégia", "criatividade", "comunicação"], 8),
    CursoFrame("Filosofia", "Humanas", 3, "EAD", ["pensamento crítico", "argumentação", "ética"], 7),
    CursoFrame("Design Gráfico", "Exatas", 4, "Presencial", ["criatividade", "programação", "design visual"], 8),
    CursoFrame("Economia", "Sociais", 5, "Presencial", ["análise de dados", "raciocínio lógico", "estratégia"], 9),
    CursoFrame("Medicina", "Biológicas", 6, "Presencial", ["conhecimento técnico", "humanidade", "dedicação"], 10),
    CursoFrame("Jornalismo", "Humanas", 4, "Híbrido", ["escrita", "comunicação", "investigação"], 7),
    CursoFrame("Gestão de Recursos Humanos", "Sociais", 4, "Híbrido", ["negociação", "liderança", "gestão de pessoas"], 8),
    CursoFrame("Engenharia Civil", "Exatas", 5, "Presencial", ["física", "construção", "planejamento"], 8),
    CursoFrame("Antropologia", "Humanas", 4, "EAD", ["cultura", "sociedade", "pesquisa"], 7),
    CursoFrame("Zootecnia", "Biológicas", 4, "Presencial", ["animais", "produção", "gestão rural"], 7),
    CursoFrame("Nutrição", "Biológicas", 4, "Presencial", ["alimentação", "saúde", "ciências"], 8),
    CursoFrame("Engenharia Mecânica", "Exatas", 5, "Presencial", ["física", "projetos", "inovação"], 8),
    CursoFrame("Teologia", "Humanas", 4, "EAD", ["religião", "filosofia", "ética"], 6),
    CursoFrame("Administração Pública", "Sociais", 4, "Presencial", ["gestão pública", "legislação", "planejamento"], 7),
    CursoFrame("Ciências Sociais", "Humanas", 4, "EAD", ["sociedade", "história", "política"], 7),
    CursoFrame("Gestão Ambiental", "Exatas", 5, "Presencial", ["ecologia", "sustentabilidade", "planejamento ambiental"], 8),
    CursoFrame("Sistemas de Informação", "Exatas", 4, "EAD", ["programação", "banco de dados", "gestão de TI"], 8),
    CursoFrame("Educação Física", "Humanas", 4, "Presencial", ["atividade física", "saúde", "educação"], 7),
    CursoFrame("Artes Visuais", "Humanas", 4, "Híbrido", ["criação artística", "design", "história da arte"], 7),
    CursoFrame("Letras", "Humanas", 4, "Presencial", ["literatura", "linguística", "ensino"], 8),
    CursoFrame("Biologia", "Biológicas", 5, "Presencial", ["pesquisa científica", "ecologia", "genética"], 9),
    CursoFrame("Ciência de Dados", "Exatas", 4, "EAD", ["programação", "estatística", "análise de dados"], 8),
    CursoFrame("Veterinária", "Biológicas", 6, "Presencial", ["animais", "cuidados", "diagnóstico"], 9)
]



# ===== SISTEMA ESPECIALISTA =====
class SistemaEspecialista:
    def __init__(self):
        self.ontologia = Ontologia()
        self.logica_fuzzy = LogicaFuzzy()
        self.cursos = criar_base_cursos()

    def recomendar(self, preferencias_usuario):
        """Recomenda cursos com base nas preferências do aluno"""
        areas_interesse = preferencias_usuario.get("areas", [])
        habilidades_usuario = preferencias_usuario.get("habilidades", [])
        mercado_minimo = preferencias_usuario.get("mercado_minimo", 6)

        recomendacoes = []

        for curso in self.cursos:
            similaridade_area = self.logica_fuzzy.calcular_similaridade_area(areas_interesse, curso.area, self.ontologia)
            afinidade_habilidades = self.logica_fuzzy.calcular_afinidade_habilidades(habilidades_usuario, curso.habilidades)
            relevancia_mercado = self.logica_fuzzy.calcular_relevancia_mercado(mercado_minimo, curso.mercado)

            pontuacao = self.logica_fuzzy.calcular_pontuacao_final(similaridade_area, afinidade_habilidades, relevancia_mercado)

            if pontuacao > 0.5:
                recomendacoes.append({
                    "curso": curso.nome,
                    "área": curso.area,
                    "duração": f"{curso.duracao} anos",
                    "modalidade": curso.modalidade,
                    "empregabilidade": curso.mercado,
                    "pontuação": pontuacao
                })

        recomendacoes.sort(key=lambda x: x["pontuação"], reverse=True)
        return recomendacoes[:5]

# ===== INTERFACE COM O USUÁRIO =====
def interface_usuario():
    print("🎓 Bem-vindo ao Sistema Especialista de Escolha de Cursos! 🎓\n")

    print("Quais áreas te interessam? (Separe por vírgula)")
    print("Opções: Exatas, Humanas, Biológicas, Sociais")
    areas_input = input("> ")
    areas_interesse = [a.strip() for a in areas_input.split(",")]

    print("\nQuais habilidades você possui? (Separe por vírgula)")
    habilidades_input = input("> ")
    habilidades_usuario = [h.strip() for h in habilidades_input.split(",")]

    print("\nQual nível mínimo de empregabilidade (0-10) você deseja?")
    try:
        mercado_minimo = float(input("> "))
        mercado_minimo = max(0, min(10, mercado_minimo))
    except ValueError:
        mercado_minimo = 6

    preferencias_usuario = {
        "areas": areas_interesse,
        "habilidades": habilidades_usuario,
        "mercado_minimo": mercado_minimo
    }

    sistema = SistemaEspecialista()
    recomendacoes = sistema.recomendar(preferencias_usuario)

    if recomendacoes:
        print("\n🎉 Cursos recomendados para você:\n")
        for rec in recomendacoes:
            print(f"📚 {rec['curso']} ({rec['área']}) - {rec['duração']}, {rec['modalidade']}, Empregabilidade: {rec['empregabilidade']}")
    else:
        print("\n😔 Nenhum curso encontrado com suas preferências.")

if __name__ == "__main__":
    interface_usuario()
