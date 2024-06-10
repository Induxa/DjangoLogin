document.querySelectorAll('input[name="data_type"]').forEach(function(radio) {
    radio.addEventListener('change', function() {
        if (this.checked) {
            document.querySelectorAll('input[name="data_type"]').forEach(function(otherRadio) {
                if (otherRadio !== radio) {
                    otherRadio.checked = false;
                }
            });
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const groupDateButton = document.getElementById('groups_id');
    const groupSelectDiv = document.querySelector('.group_select');

    groupDateButton.addEventListener('click', function() {
        if (groupSelectDiv.style.display === 'none') {
            groupSelectDiv.style.display = 'block';
        } else {
            groupSelectDiv.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const AllDateButton = document.getElementById('all_date_id');
    const AllButtonDiv = document.querySelector('.all_date_student');

    AllDateButton.addEventListener('click', function() {
        if (AllButtonDiv.style.display === 'none') {
            AllButtonDiv.style.display = 'block';
        } else {
            AllButtonDiv.style.display = 'none';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const AllDateButton = document.getElementById('student_id');
    const AllButtonDiv = document.querySelector('.student_input');

    AllDateButton.addEventListener('click', function() {
        if (AllButtonDiv.style.display === 'none') {
            AllButtonDiv.style.display = 'block';
        } else {
            AllButtonDiv.style.display = 'none';
        }
    });
});