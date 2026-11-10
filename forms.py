from datetime import datetime

def validar_cliente(nome, telefone):
    erros = []
    if not nome or len(nome.strip()) < 3:
        erros.append("O nome do cliente é obrigatório e deve ter no mínimo 3 caracteres.")
    if not telefone or len(telefone.strip()) < 8:
        erros.append("O telefone do cliente é obrigatório.")
    return erros

def validar_os(descricao, prazo_str, prioridade):
    erros = []
    if not descricao or len(descricao.strip()) < 5:
        erros.append("A descrição do serviço deve ser detalhada.")
    if not prazo_str:
        erros.append("O prazo de entrega é obrigatório.")
    else:
        try:
            datetime.strptime(prazo_str, '%Y-%m-%d')
        except ValueError:
            erros.append("Data de prazo inválida.")
    if prioridade not in ['Baixa', 'Média', 'Alta', 'Urgente']:
        erros.append("Prioridade selecionada é inválida.")
    return erros