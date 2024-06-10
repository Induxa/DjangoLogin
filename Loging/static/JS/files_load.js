$(document).ready(function() {
    var group = "{{ student.GroupStudents }}";
    var lst = ['11', '21', '31', '41', '15', '25'];

    // Проверяем, какой курс исследует студент
    if (lst.some(item => group.includes(item))) {
        // Показываем div для первого курса
        $("#first-course").show();
    } else if (group === "ИТ-21") {
        // Показываем div для второго курса
        $("#second-course").show();
    } else if (group === "ИТ-31") {
        // Показываем div для третьего курса
        $("#third-course").show();
    } else if (group === "ИТ-41") {
        // Показываем div для четвертого курса
        $("#fourth-course").show();
    }
});
