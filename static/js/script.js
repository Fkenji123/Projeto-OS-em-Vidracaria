// Script principal para o MVP de Gestão de Ordens de Serviço - Vidraçaria

document.addEventListener('DOMContentLoaded', function () {
    
    // 1. Auto-fechar alertas flash após 5 segundos
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            let bsAlert = bootstrap.Alert.getInstance(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 5000);
    });

    // 2. Confirmação para status crítico (ex: Cancelar Ordem de Serviço)
    const statusSelects = document.querySelectorAll('select[name="status"]');
    statusSelects.forEach(function (select) {
        let valorOriginal = select.value;

        select.addEventListener('focus', function() {
            valorOriginal = this.value;
        });

        select.addEventListener('change', function (e) {
            if (this.value === 'Cancelada') {
                const confirmar = confirm('Tem certeza de que deseja CANCELAR esta Ordem de Serviço? Esta ação altera o fluxo operacional.');
                if (!confirmar) {
                    this.value = valorOriginal;
                    e.preventDefault();
                }
            }
        });
    });

    // 3. Carregar preferências de acessibilidade salvas ao iniciar a página
    if (localStorage.getItem('contraste') === 'alto') {
        document.body.classList.add('alto-contraste');
    }
    if (localStorage.getItem('tamanhoFonte') === 'grande') {
        document.body.classList.add('fonte-grande');
    }

    console.log('Sistema de Gestão de OS da Vidraçaria carregado e operacional.');
});

// --- Funções de Acessibilidade globais ---

// Função para Alternar Contraste
function alternarContraste() {
    document.body.classList.toggle('alto-contraste');
    const ativo = document.body.classList.contains('alto-contraste');
    localStorage.setItem('contraste', ativo ? 'alto' : 'normal');
}

// Função para Ajustar Tamanho da Fonte
function mudarFonte(acao) {
    if (acao === 'aumentar') {
        document.body.classList.add('fonte-grande');
        localStorage.setItem('tamanhoFonte', 'grande');
    } else {
        document.body.classList.remove('fonte-grande');
        localStorage.setItem('tamanhoFonte', 'normal');
    }
}