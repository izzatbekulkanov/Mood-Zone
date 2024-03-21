// Ma'lumotlarni olish uchun AJAX so'rovi
function fetchData() {
    $.ajax({
        url: 'get_departments',
        type: 'GET',
        success: function (response) {
            // Agar so'rov muvaffaqiyatli bo'lsa
            fakultetData(response.fakultet);
            bolimData(response.bolim);
            kafedraData(response.kafedra);
            boshqarmaData(response.boshqarma);
            markazData(response.markaz);
            rektoratData(response.rektorat);
            // Swal.fire({
            //     position: 'top-end',
            //     icon: 'success',
            //     backdrop: `rgba(60,60,60,0.8)`,
            //     title: 'Ma\'lumotlarni muvaffaqiyatli yuklandi',
            //     showConfirmButton: false,
            //     timer: 55000
            // });
        },
        error: function (xhr, status, error) {
            Swal.fire({
                position: 'top-end',
                icon: 'error',
                backdrop: `rgba(60,60,60,0.8)`,
                title: 'Ma\'lumotlarni olishda xatolik yuz berdi',
                showConfirmButton: false,
                timer: 55000
            });
        }
    });
}


function fakultetData(fakultetData) {
    const tableBody = document.getElementById('book-table-fakultet');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish

    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    fakultetData.forEach((department, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (department.is_active === true) {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        }
        row.innerHTML = `
                <td class="text-dark">${department.name}</td>
                <td class="text-dark">${department.code}</td>
                <td class="text-dark">${department.structure_type}</td>
                <td class="text-dark">${department.parent}</td>
                <td class="text-dark">${statusBadge}</td>
                <td><button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal(); fillBookData(${department.code},'${department.name}', '${department.structure_type}', '${department.parent}', ${department.is_active})">
                        <span class="btn-inner">
                            <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                        </span>
                    </button>
                </td> 
                    `;
        tableBody.appendChild(row);
    });
}

function bolimData(bolimData) {
    const tableBody = document.getElementById('book-table-bolim');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    bolimData.forEach((department, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (department.is_active === true) {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        }
        row.innerHTML = `
                <td class="text-dark">${department.name}</td>
                <td class="text-dark">${department.code}</td>
                <td class="text-dark">${department.structure_type}</td>
                <td class="text-dark">${department.parent}</td>
                <td class="text-dark">${statusBadge}</td>
                <td class="text-dark"><button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal(); fillBookData(${department.code},'${department.name}', '${department.structure_type}', '${department.parent}', ${department.is_active})">
                        <span class="btn-inner">
                            <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                        </span>
                    </button>
                </td> 
                    `;
        tableBody.appendChild(row);
    });
}

function kafedraData(kafedraData) {
    const tableBody = document.getElementById('book-table-kafedra');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    kafedraData.forEach((department, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (department.is_active === true) {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        }
        row.innerHTML = `
                <td class="text-dark">${department.name}</td>
                <td class="text-dark">${department.code}</td>
                <td class="text-dark">${department.structure_type}</td>
                <td class="text-dark">${department.parent}</td>
                <td class="text-dark">${statusBadge}</td>
                <td class="text-dark"><button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal(); fillBookData(${department.code},'${department.name}', '${department.structure_type}', '${department.parent}', ${department.is_active})">
                        <span class="btn-inner">
                            <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                        </span>
                    </button>
                </td> 
                    `;
        tableBody.appendChild(row);
    });
}

function boshqarmaData(boshqarmaData) {
    const tableBody = document.getElementById('headbolim');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    boshqarmaData.forEach((department, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (department.is_active === true) {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        }
        row.innerHTML = `
                <td class="text-dark">${department.name}</td>
                <td class="text-dark">${department.code}</td>
                <td class="text-dark">${department.structure_type}</td>
                <td class="text-dark">${department.parent}</td>
                <td class="text-dark">${statusBadge}</td>
                <td ><button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal(); fillBookData(${department.code},'${department.name}', '${department.structure_type}', '${department.parent}', ${department.is_active})">
                        <span class="btn-inner">
                            <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                        </span>
                    </button>
                </td> 
                    `;
        tableBody.appendChild(row);
    });
}

function markazData(markazData) {
    const tableBody = document.getElementById('book-table-markaz');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    markazData.forEach((department, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (department.is_active === true) {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        }
        row.innerHTML = `
                <td class="text-dark">${department.name}</td>
                <td class="text-dark">${department.code}</td>
                <td class="text-dark">${department.structure_type}</td>
                <td class="text-dark">${department.parent}</td>
                <td class="text-dark">${statusBadge}</td>
                <td><button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal(); fillBookData(${department.code},'${department.name}', '${department.structure_type}', '${department.parent}', ${department.is_active})">
                        <span class="btn-inner">
                            <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                        </span>
                    </button>
                </td> 
                    `;
        tableBody.appendChild(row);
    });
}

function rektoratData(rektoratData) {
    const tableBody = document.getElementById('book-table-rektorat');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    rektoratData.forEach((department, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (department.is_active === true) {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        }
        row.innerHTML = `
                <td class="text-dark">${department.name}</td>
                <td class="text-dark">${department.code}</td>
                <td class="text-dark">${department.structure_type}</td>
                <td class="text-dark">${department.parent}</td>
                <td class="text-dark">${statusBadge}</td>
                <td><button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal(); fillBookData(${department.code},'${department.name}', '${department.structure_type}', '${department.parent}', ${department.is_active})">
                        <span class="btn-inner">
                            <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                        </span>
                    </button>
                </td> 
                    `;
        tableBody.appendChild(row);
    });
}


// CSRF tokenini olish uchun funksiya
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Xavfsizlik uchun "csrftoken" nomli cookie ni tekshirish
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function saveDepartments() {
    var loadedData = document.getElementById("loaded-data");
    loadedData.textContent = "Yuklanmoqda";
    $.ajax({
        url: 'save_department',
        type: 'GET',
        success: function (response) {
            fetchData();
            loadedData.textContent = "Yangilash";
            Swal.fire({
                position: 'top-end',
                icon: 'success',
                backdrop: `rgba(60,60,60,0.8)`,
                title: 'Fakultetlar ro\'yhati muvaffaqiyatli yangilandi',
                showConfirmButton: false,
                timer: 2000
            });
        },
        error: function (xhr, status, error) {
            loadedData.textContent = "Yangilash";

            Swal.fire({
                position: 'top-end',
                icon: 'error',
                backdrop: `rgba(60,60,60,0.8)`,
                title: 'HEMIS bilan bog\'lanib bo\'madi',
                showConfirmButton: false,
                timer: 2000
            });
        }
    });
}

fetchData();