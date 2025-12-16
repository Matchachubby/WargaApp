document.addEventListener('DOMContentLoaded', function () {

    const API_URL = 'http://127.0.0.1:8000/api/warga/';
    const TOKEN = '470b659b486ec16952d795967b0697a822c0ec4b';

    const container = document.getElementById('warga-list-container');
    const form = document.getElementById('warga-form');

    function loadWarga(url = API_URL) {
        container.innerHTML = '<p>Memuat data...</p>';
        
        fetch(url, {
            headers: {
                'Authorization': 'Token ' + TOKEN
            }
         })
        .then(res => {
            if (!res.ok) throw new Error();
            return res.json();
        })
        .then(data => {
            container.innerHTML = '';
            
            const ul = document.createElement('ul');
            
            data.results.forEach(warga => {
                const li = document.createElement('li');
                li.textContent =
                `${warga.nama_lengkap} - ${warga.nik} - ${warga.alamat}`;
                ul.appendChild(li);
            });
            
            container.appendChild(ul);
            // =====================
            // // PAGINATION BUTTON
            // // ==================
            const nav = document.createElement('div');
            
            if (data.previous) {
                const prevBtn = document.createElement('button');
                prevBtn.textContent = '⬅ Previous';
                prevBtn.onclick = () => loadWarga(data.previous);
                nav.appendChild(prevBtn);
            }
            
            if (data.next) {
                const nextBtn = document.createElement('button');
                nextBtn.textContent = 'Next ➡';
                nextBtn.onclick = () => loadWarga(data.next);
                nav.appendChild(nextBtn);
            }
            
            container.appendChild(nav);
        })
        .catch(() => {
            container.innerHTML = '<p>Gagal memuat data</p>';
        });
    }

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const data = {
            nik: document.getElementById('nik').value,
            nama_lengkap: document.getElementById('nama_lengkap').value,
            alamat: document.getElementById('alamat').value,
            no_telepon: document.getElementById('no_telepon').value || '',
            tanggal_lahir: document.getElementById('tanggal_lahir').value || null,
            jenis_kelamin: document.getElementById('jenis_kelamin').value || null
        };

        fetch(API_URL, {
            method: 'POST',
            headers: {
                'Authorization': 'Token ' + TOKEN,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(res => {
            if (!res.ok) throw new Error();
            return res.json();
        })
        .then(() => {
            alert('Data warga berhasil ditambahkan');
            form.reset();
            loadWarga();
        })
        .catch(() => {
            alert('Gagal menyimpan data (cek token / permission)');
        });
    });

    loadWarga();
});
