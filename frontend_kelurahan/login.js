document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const message = document.getElementById('message');

    fetch('http://127.0.0.1:8000/api/auth/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(res => {
        if (!res.ok) {
            throw new Error('Login gagal');
        }
        return res.json();
    })
    .then(data => {
        // SIMPAN TOKEN
        localStorage.setItem('token', data.token);

        message.textContent = 'Login berhasil!';
        message.style.color = 'green';

        // PINDAH HALAMAN
        window.location.href = 'index.html';
    })
    .catch(() => {
        message.textContent = 'Username atau password salah';
        message.style.color = 'red';
    });
});
