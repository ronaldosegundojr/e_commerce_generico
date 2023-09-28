document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.querySelector('form'); // Seleciona o formulário de login
    const errorMessage = document.querySelector('#error-message'); // Seleciona a div de mensagem de erro

    loginForm.addEventListener('submit', async function (e) {
        e.preventDefault(); // Impede o envio padrão do formulário

        const formData = new FormData(loginForm); // Cria um objeto FormData com os dados do formulário

        // Envie uma solicitação POST para a rota de login
        const response = await fetch('/login', {
            method: 'POST',
            body: formData, // Envie os dados do formulário
        });

        if (response.ok) {
            // Login bem-sucedido, redirecione para a página desejada
            window.location.href = '/account'; // Substitua com a página desejada
        } else {
            // Exiba a mensagem de erro
            errorMessage.textContent = 'Usuário, e-mail ou senha inválidos.';
        }
    });
});
