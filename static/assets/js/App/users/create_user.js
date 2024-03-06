document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        fetchData();
    });
});

function fetchData() {
    const apiUrl = 'https://student.namdu.uz/rest/v1/data/student-list';
    const token = 'cbdfefbb283db3a219a7e7dcefd620b4';
    const studentId = document.getElementById('student_id').value;

    const searchQuery = `?search=${studentId}`;

    axios.get(apiUrl + searchQuery, {
        headers: {
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json'
        }
    })
        .then(function (response) {
            console.log('Ma\'lumotlar yuklandi:', response.data);
            displayData(response.data); // Ma'lumotlarni konsolda ko'rsatish
        })
        .catch(function (error) {
            console.error('Yuklashda xatolik yuz berdi:', error);
        });
}


function displayData(data) {
    // Ma'lumotlar obyektining "items" bo'limini olamiz
    const items = data.data.items;

    // Agar "items" bo'limi mavjud bo'lsa
    if (items && Array.isArray(items) && items.length > 0) {
        // Ma'lumotlarni ko'rsatish uchun HTML elementlarini tanlash
        const userInfoDiv = document.getElementById('student_info_api');

        // Ma'lumotlarni HTML elementiga chiqarish
        items.forEach(item => {
            const itemDiv = document.createElement('div');
            for (const key in item) {
                const keySpan = document.createElement('span');
                keySpan.textContent = `${key}: `;
                const valueSpan = document.createElement('span');
                valueSpan.textContent = (key === 'birth_date') ? formatDate(item[key]) : getValue(item[key]);

                // Qator yaratish
                const row = document.createElement('div');
                row.classList.add('row');

                // Key uchun form-group
                const keyFormGroup = document.createElement('div');
                keyFormGroup.classList.add('form-group', 'col-md-6');
                keyFormGroup.appendChild(keySpan);

                // Value uchun form-group
                const valueFormGroup = document.createElement('div');
                valueFormGroup.classList.add('form-group', 'col-md-6');
                valueFormGroup.appendChild(valueSpan);

                // Key va value ni qatorga qo'shish
                row.appendChild(keyFormGroup);
                row.appendChild(valueFormGroup);

                // Ma'lumot diviga qatorni qo'shish
                itemDiv.appendChild(row);
                itemDiv.appendChild(document.createElement('br')); // Qatordan keyin qator qo'shish
            }
            // HTML-ni sahifaga qo'shish
            userInfoDiv.appendChild(itemDiv);
            userInfoDiv.appendChild(document.createElement('hr')); // Har bir ma'lumotdan keyin chiziq qo'yish
        });
    } else {
        console.error('Data items not found or empty!');
    }
}

// Ma'lumot turi bo'yicha qiymat olish
function getValue(value) {
    if (typeof value === 'object' && value !== null) {
        return value.name || value.code || 'Object';
    }
    return value;
}

// Unix timestampni sana ko'rinishiga o'girish
function formatDate(timestamp) {
    const date = new Date(timestamp * 1000);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-$
    {month}-${day}`;
}

// Forma elementini tanlash
const form = document.querySelector('form');

// Forma yuborilganda
form.addEventListener('submit', async (e) => {
    // Boshqa bir joyga yuborilishni to'xtatamiz
    e.preventDefault();

    // Formadagi barcha input elementlarini tanlash
    const inputs = form.querySelectorAll('input');

    // Ma'lumotlarni saqlash uchun bo'sh obyekt
    const studentData = {};

    // Har bir inputni o'qish va studentData obyektiga joylash
    inputs.forEach(input => {
        studentData[input.id] = input.value;
    });

    try {
        // Student obyektini yaratish uchun serverga so'rov jo'natish
        const response = await fetch('/api/create_student/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(studentData), // Student ma'lumotlarini JSON ko'rinishida yuborish
        });

        if (!response.ok) {
            throw new Error('Server bilan muammo');
        }

        // Agar javob muvaffaqiyatli bo'lsa, ma'lumotlarni qayta tozalash
        inputs.forEach(input => {
            input.value = '';
        });

        // Foydalanuvchi uchun ma'lumot yuborildi xabarni chiqarish
        alert('Yangi student muvaffaqiyatli yaratildi!');
    } catch (error) {
        // Xatolik bo'lsa uni chiqarish
        console.error('Xatolik yuz berdi:', error.message);
        alert('Xatolik yuz berdi, iltimos qaytadan urinib ko\'ring');
    }
});

