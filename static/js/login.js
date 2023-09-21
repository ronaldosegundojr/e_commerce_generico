// login.js

// Função para mostrar a janela pop-up
function showErrorPopup(message) {
    // Crie uma div para a janela pop-up
    var popup = $("<div></div>");
    popup.html(message);
    popup.addClass("error-popup");

    // Adicione a div à página
    $("body").append(popup);

    // Configure um temporizador para remover a janela pop-up após alguns segundos
    setTimeout(function() {
        popup.fadeOut("slow", function() {
            $(this).remove();
        });
    }, 3000); // A janela pop-up será removida após 3 segundos
}
