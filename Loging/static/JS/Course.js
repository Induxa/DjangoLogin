// Получение номера курса из контекста шаблона Django
var course = "{{ course }}";

// Функция для отображения соответствующих курсов студента
function showCourses(course) {
    for (var i = 1; i <= course; i++) {
        var courseDiv = document.querySelector('h3:nth-of-type(' + i + ')').nextElementSibling;
        courseDiv.style.display = 'block';
    }
}

// Вызов функции для отображения курсов студента
showCourses(course);
