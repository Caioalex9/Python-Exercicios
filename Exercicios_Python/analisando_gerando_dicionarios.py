def notas(*resp, sit=False):
    """
    --> função para analisar notas do aluno e sua situação.
    resp: uma ou mais notas do aluno.
    sit: valor opcional, indicando se deve ou não adicionar situação do aluno.
    return: dicionario com varias informações sobre a situação da turma.
    """
    aluno = dict()
    aluno['Total'] = len(resp)
    aluno['Maior']  = max(resp)
    aluno['Menor'] = min(resp)
    aluno['Media'] = sum(resp) / len(resp)
    if sit:
        if aluno['Media'] >= 7:
            aluno['Situação'] = 'BOA'
        elif aluno['Media'] >= 5:
            aluno['Situação'] = 'RAZOAVEL'
        else:
            aluno['Situção'] = 'RUIM'
    return aluno


resp = notas(8.5, 5.5,2.5,10 , 9, sit=True)

print(resp)

# help(notas)
