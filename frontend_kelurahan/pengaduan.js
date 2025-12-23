const API_URL = 'http://127.0.0.1:8000/api/pengaduan/';
const TOKEN = '470b659b486ec16952d795967b0697a822c0ec4b';

if (!TOKEN) {
    alert('Silakan login terlebih dahulu');
    window.location.href = 'login.html';
}

const listContainer = document.getElementById('pengaduan-list');
const form = document.getElementById('pengaduan-form');

// =======================
// LOAD DATA PENGADUAN
// =======================
function loadPengaduan() {
    fetch(API_URL, {
        headers: {
            'Authorization': 'Token ' + TOKEN
        }
    })
    .then(res => res.json())
    .then(data => {
        listContainer.innerHTML = '';
        const ul = document.createElement('ul');

        data.results.forEach(p => {
            const li = document.createElement('li');
            li.textContent = `${p.judul} - ${p.status}`;
            ul.appendChild(li);
        });

        listContainer.appendChild(ul);
    })
    .catch(() => {
        listContainer.innerHTML = '<p>Gagal memuat pengaduan</p>';
    });
}

// =======================
// TAMBAH PENGADUAN
// =======================
form.addEventListener('submit', function (e) {
    e.preventDefault();

    const judul = document.getElementById('judul').value;
    const deskripsi = document.getElementById('deskripsi').value;

    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Authorization': 'Token ' + TOKEN,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            judul: judul,
            deskripsi: deskripsi
        })
    })
    .then(res => {
        if (!res.ok) throw new Error();
        return res.json();
    })
    .then(() => {
        alert('Pengaduan berhasil dikirim');
        form.reset();
        loadPengaduan();
    })
    .catch(() => {
        alert('Gagal mengirim pengaduan');
    });
});

// =======================
// LOGOUT
// =======================
function logout() {
    localStorage.removeItem('token');
    window.location.href = 'login.html';
}

loadPengaduan();
