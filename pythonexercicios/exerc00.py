class Disciplina:
    def __init__(self,aluno, nota1, nota2):
        self.nome = aluno
        self.nota1 = nota1
        self.nota2 = nota2

    def calcularMedia(self):
            self.media = (self.nota1 + self.nota2) / 2

    def exibirSituacao(self):
            if self.media >= 7:
                print('Aprovado')
            else:
                print('Reprovado')


aluno1 = Disciplina('Stephane', 10, 10)
aluno1.calcularMedia()
aluno1.exibirSituacao()

aluno2 = Disciplina('Alguém', 8, 3)
aluno2.calcularMedia()
aluno2.exibirSituacao()