document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');
  const loginError = document.getElementById('login-error');

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // ¿Es este el nombre de la cookie CSRF?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie('csrftoken');

  loginForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const formData = new FormData(loginForm);

    fetch(loginForm.action, {
      method: 'POST',
      headers: {
        'X-CSRFToken': csrftoken,
      },
      body: formData,
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Credenciales inválidas');
        }
        return response.json();
      })
      .then(data => {
        if (data.success) {
          window.location.href = "/"; // o "/inicio/" según tu estructura
        } else {
          loginError.textContent = data.message;
        }
      })
      .catch(error => {
        loginError.textContent = error.message;
      });
  });
});
