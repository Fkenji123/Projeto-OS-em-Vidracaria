// Script principal para o MVP de Gestão de Ordens de Serviço - Vidraçaria

document.addEventListener('DOMContentLoaded', function () {
    
    // Auto-fechar alertas flash após 5 segundos
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            let bsAlert = bootstrap.Alert.getInstance(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 5000);
    });

    // Confirmação para status crítico (ex: Cancelar Ordem de Serviço)
    const statusSelects = document.querySelectorAll('select[name="status"]');
    statusSelects.forEach(function (select) {
        // Armazenar o valor original caso o usuário desista da confirmação
        let valorOriginal = select.value;

        select.addEventListener('focus', function() {
            valorOriginal = this.value;
        });

        select.addEventListener('change', function (e) {
            if (this.value === 'Cancelada') {
                const confirmar = confirm('Tem certeza de que deseja CANCELAR esta Ordem de Serviço? Esta ação altera o fluxo operacional.');
                if (!confirmar) {
                    this.value = valorOriginal; // Reverte para o status anterior
                    e.preventDefault();
                }
            }
        });
    });

    console.log('Sistema de Gestão de OS da Vidraçaria carregado e operacional.');
});