const openModalBtn = document.getElementById('openModal');
const modal = document.getElementById('modal');
const closeModalBtn = document.getElementsByClassName('close')[0];

openModalBtn.addEventListener('click', () => {
    modal.style.display = 'block';
});

closeModalBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

document.addEventListener("DOMContentLoaded", function(){
  var scrollbar = document.body.clientWidth - window.innerWidth + 'px';
  console.log(scrollbar);
  document.querySelector('[href="#ModalReport"]').addEventListener('click',function(){
    document.body.style.overflow = 'hidden';
    document.querySelector('#ModalReport').style.marginLeft = scrollbar;
  });
  document.querySelector('[href="#close"]').addEventListener('click',function(){
    document.body.style.overflow = 'visible';
    document.querySelector('#ModalReport').style.marginLeft = '0px';
  });
});

// Получаем ссылки на модальные окна и их кнопки закрытия
  var reportModal = document.getElementById("reportModal");
  var archiveModal = document.getElementById("archiveModal");
  var reportModalClose = document.getElementById("reportModalClose");
  var archiveModalClose = document.getElementById("archiveModalClose");

  // Функция для открытия модального окна для отчета
  function openReportModal() {
    reportModal.style.display = "block";
  }

  // Функция для закрытия модального окна для отчета
  function closeReportModal() {
    reportModal.style.display = "none";
  }

  // Функция для открытия модального окна для архивов
  function openArchiveModal() {
    archiveModal.style.display = "block";
  }

  // Функция для закрытия модального окна для архивов
  function closeArchiveModal() {
    archiveModal.style.display = "none";
  }

  // Привязываем обработчики событий к кнопкам открытия и закрытия модальных окон
  document.getElementById("ModalReport").onclick = openReportModal;
  document.getElementById("ModalArchive").onclick = openArchiveModal;
  reportModalClose.onclick = closeReportModal;
  archiveModalClose.onclick = closeArchiveModal;

  // Закрыть модальное окно, если пользователь щелкает за его пределами
  window.onclick = function(event) {
    if (event.target == reportModal) {
      closeReportModal();
    }
    if (event.target == archiveModal) {
      closeArchiveModal();
    }
  };