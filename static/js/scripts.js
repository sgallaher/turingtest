// static/js/scripts.js

// Auto-resize textarea
document.addEventListener('DOMContentLoaded', () => {
  const textarea = document.getElementById('answers');  // assuming id="answers"
  if (!textarea) return;

  function autoResize() {
    textarea.style.height = 'auto';
    textarea.style.height = textarea.scrollHeight + 'px';
  }
  textarea.addEventListener('input', autoResize);
  autoResize();

  // Bootstrap form validation
  const form = document.getElementById('turingForm');
  form.addEventListener('submit', event => {
    if (!form.checkValidity() || textarea.value.trim() === '') {
      event.preventDefault();
      event.stopPropagation();
      textarea.classList.add('is-invalid');
    } else {
      textarea.classList.remove('is-invalid');
    }
    form.classList.add('was-validated');
  }, false);
});
