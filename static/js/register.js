document.addEventListener('DOMContentLoaded', function () {
    const emailField = document.querySelector('#email');
    const emailValidationMessage = document.querySelector('#email-validation-message');
    const passwordField = document.querySelector('#password');
    const registerForm = document.querySelector('#register-form');
    const passwordStrength = document.querySelector('#password-strength');
    const errorMessage = document.querySelector('#error-message'); // Elemento para mensagens de erro
    
    let formSubmitted = false; // Variável para rastrear se o formulário foi submetido

    emailField.addEventListener('input', function () {
        const email = emailField.value;
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

        if (emailRegex.test(email)) {
            emailValidationMessage.textContent = '';
        } else {
            emailValidationMessage.textContent = 'O e-mail inserido não é um e-mail válido';
        }
        checkFormValidity();
    });

    passwordField.addEventListener('input', function () {
        const password = passwordField.value;
        const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$/;
        
        if (passwordRegex.test(password)) {
            passwordStrength.textContent = 'Senha forte';
            passwordStrength.style.color = 'green';
        } else if (password.length >= 8) {
            passwordStrength.textContent = 'Senha média';
            passwordStrength.style.color = 'yellow';
        } else {
            passwordStrength.textContent = 'Senha fraca';
            passwordStrength.style.color = 'red';
        }
        checkFormValidity();
    });

    function checkFormValidity() {
        const email = emailField.value;
        const password = passwordField.value;
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$/;

        const isEmailValid = emailRegex.test(email);
        const isPasswordValid = passwordRegex.test(password);
        const isNotEmpty = email !== '' && password !== '';

        if (isEmailValid && isPasswordValid && isNotEmpty) {
            // Não redirecione automaticamente aqui
            errorMessage.textContent = ''; // Limpe qualquer mensagem de erro anterior
        } else {
            // Verifique se o formulário foi submetido antes de mostrar a mensagem de erro
            if (formSubmitted) {
                errorMessage.textContent = 'Preencha todos os campos corretamente.';
            }
        }
    }

    const registerButton = document.querySelector('#register-button');
    registerButton.addEventListener('click', function () {
        // Marque o formulário como submetido
        formSubmitted = true;

        // Verifique novamente a validade do formulário antes de redirecionar
        const email = emailField.value;
        const password = passwordField.value;
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        const passwordRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$/;

        const isEmailValid = emailRegex.test(email);
        const isPasswordValid = passwordRegex.test(password);
        const isNotEmpty = email !== '' && password !== '';

        if (isEmailValid && isPasswordValid && isNotEmpty) {
            registerForm.submit(); // Submeta o formulário se todos os campos forem válidos
        } else {
            errorMessage.textContent = 'Preencha todos os campos corretamente.';
        }
    });
});