$(document).ready(function() {
    $('input[name="status"]').on('change', function() {
        var status = $(this).val();
        $.ajax({
            url: '{% url 'faculty:faculty_students' faculty_id %}',
            method: 'GET',
            data: {
                'status': status
            },
            success: function(data) {
                $('#student-list').html(data);
            }
        });
    });
    $('input[name="status"]:checked').trigger('change');
});
//jQuery(($) => {
//    $('.select').on('click', '.select__head', function () {
//        if ($(this).hasClass('open')) {
//            $(this).removeClass('open');
//            $(this).next().fadeOut();
//        } else {
//            $('.select__head').removeClass('open');
//            $('.select__list').fadeOut();
//            $(this).addClass('open');
//            $(this).next().fadeIn();
//        }
//    });
//
//    $('.select').on('click', '.select__item', function () {
//        $('.select__head').removeClass('open');
//        $(this).parent().fadeOut();
//        $(this).parent().prev().text($(this).text());
//        $(this).parent().prev().prev().val($(this).text());
//    });
//
//    $(document).click(function (e) {
//        if (!$(e.target).closest('.select').length) {
//            $('.select__head').removeClass('open');
//            $('.select__list').fadeOut();
//        }
//    });
//});

//<script>
//    document.getElementById("transferButton").onclick = function() {
//        var group = document.querySelector('input[name="Group"]');
//        document.getElementById("transferButton").value = group;
//    };
//</script>

//<!--{% block script %}-->
//<!--<script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4="-->
//<!--        crossorigin="anonymous"></script>-->
//<!--<script>-->
//<!--    $(document).ready(function() {-->
//<!--    $('input[name="status"]').on('change', function() {-->
//<!--        var status = $(this).val();-->
//<!--        $.ajax({-->
//<!--            url: '{% url 'faculty:faculty_students' faculty_id %}',-->
//<!--            method: 'GET',-->
//<!--            data: {-->
//<!--                'status': status-->
//<!--            },-->
//<!--            success: function(data) {-->
//<!--                $('#student-list').html(data);-->
//<!--            }-->
//<!--        });-->
//<!--    });-->
//<!--    $('input[name="status"]:checked').trigger('change');-->
//<!--});-->
//<!--</script>-->
//<!--{% endblock %}-->