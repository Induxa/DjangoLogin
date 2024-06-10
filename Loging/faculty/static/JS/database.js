// Получаем кнопку "Изменить"
var editButton = document.getElementById('editButton');
// Добавляем обработчик события на нажатие кнопки "Изменить"
editButton.addEventListener('click', function() {
    // Получаем все скрытые ячейки с кнопками radio
    var hiddenRadioCells = document.querySelectorAll('.position_right[style="display: none;"]');
    // Переключаем их видимость на "блок"
    hiddenRadioCells.forEach(function(cell) {
        cell.style.display = 'table-cell';
    });
    // Отображаем кнопку "Сохранить"
    document.getElementById('saveButton').style.display = 'inline-block';
});

window.onload = function() {
    // Получаем все элементы radio
    var radioButtons = document.querySelectorAll('input[type="radio"]');

    // Проходимся по каждому элементу radio
    radioButtons.forEach(function(radioButton) {
        // Добавляем обработчик события change
        radioButton.addEventListener('change', function() {
            // Если элемент выбран
            if (this.checked) {
                // Получаем id студента
                var studentId = this.id;
                // Получаем все input студента
                var studentInputs = document.querySelectorAll('.student-' + studentId);
                // Проходимся по каждому input и убираем атрибут disabled
                studentInputs.forEach(function(input) {
                    input.removeAttribute('disabled');
                });

                // Отключаем все остальные input
                var allRadioButtons = document.querySelectorAll('input[type="radio"]');
                allRadioButtons.forEach(function(button) {
                    if (button.id !== studentId) {
                        var otherStudentInputs = document.querySelectorAll('.student-' + button.id);
                        otherStudentInputs.forEach(function(input) {
                            input.setAttribute('disabled', 'disabled');
                        });
                    }
                });
            }
        });
    });
};