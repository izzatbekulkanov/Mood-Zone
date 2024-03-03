// Ma'lumotlarni olish uchun AJAX so'rovi
function fetchData() {
    // AJAX so'rovi yaratish
    var xhr = new XMLHttpRequest();

    // Ma'lumotlar qabul qilinishida o'zgarishlar uchun funksiya
    xhr.onreadystatechange = function () {
        // So'rov muvaffaqiyatli amalga oshirilgan va javob qaytarilganligini tekshirish
        if (xhr.readyState === XMLHttpRequest.DONE) {
            // HTTP status kodi 200 bo'lsa (muvaffaqiyatli javob olingan bo'lsa)
            if (xhr.status === 200) {
                // JSON javobni obyektga o'zgartirish
                var response = JSON.parse(xhr.responseText);
                // Ma'lumotlarni jadvalga qo'yish uchun funksiya chaqirish
                displayData(response);
                displayRejectedBooks(response.rejected_books); // rejected_booksni jadvalga qo'shish
            } else {
                // Xatolik bo'lsa
                console.error('Error fetching data:', xhr.statusText);
            }
        }
    };

    // AJAX so'rovini tayyorlash
    xhr.open('GET', 'book_list_json', true);

    // AJAX so'rovini jo'natish
    xhr.send();
}

// accepted_books jadvalga qo'shish

function displayData(data) {
    const tableBody = document.getElementById('book-table-body');
    tableBody.innerHTML = ''; // Eski ma'lumotlarni o'chirish

    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    data.approved_books.forEach((book, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (book.status === 'accepted') {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success">Complete</span>`;
        } else if (book.status === 'rejected') {
            statusBadge = `<span class="badge bg-soft-warning p-2 text-warning">Tasdiqlanmagan</span>`;
        } else {
            statusBadge = ''; // Boshqacha holat uchun
        }
        row.innerHTML = `
                    <td class="sorting_1">
                        <div class="d-flex align-items-center">
                            <div class="media-support-info">
                                <h5 class="iq-sub-label">${book.title}</h5>
                                <p class="mb-0">${book.author}</p>
                            </div>
                        </div>
                    </td>
                    <td class="text-dark">${book.library_name}</td>
                    <td class="text-dark">${book.added_by}</td>
                    <td class="text-dark">${book.book_id}</td>
                    <td class="text-dark">${book.quantity}</td>
                    <td class="text-dark">${book.publication_year}</td>
                    <td>${statusBadge}</td>
                    <td>
                        <button class="btn btn-icon btn-primary rounded-pill btn-sm" onclick="openModal()">
                            <span class="btn-inner">
                             <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                            </span>
                        </button>
                    </td> 
                    `;
        tableBody.appendChild(row);
    });
}

// rejected_booksni jadvalga qo'shish
function displayRejectedBooks(rejected_books) {
    const tableBodyRejected = document.getElementById('book-table-body-rejected');
    tableBodyRejected.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    confirmModal.innerHTML = '';
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    rejected_books.forEach((book, index) => {
        const row = document.createElement('tr');
        // Odd va even klasslarni qo'shish
        row.className = index % 2 === 0 ? 'even' : 'odd';
        let statusBadge;
        if (book.status === 'accepted') {
            statusBadge = `<span class="badge bg-soft-success p-2 text-success cursor-pointer">Complete</span>`;
        } else if (book.status === 'rejected') {
            statusBadge = `
                     <button type="button" class="btn btn-warning" data-bs-toggle="modal"  data-bs-target="#staticBackdrop" onclick="fillModal(${book.book_id}, '${book.title}')" >Tasdiqlash</button>

                     `;
        } else {
            statusBadge = ''; // Boshqacha holat uchun
        }
        row.innerHTML = `
                    <td class="sorting_1">
                        <div class="d-flex align-items-center">
                            <div class="media-support-info">
                                <h5 class="iq-sub-label">${book.title}</h5>
                                <p class="mb-0">${book.author}</p>
                            </div>
                        </div>
                    </td>
                    <td class="text-dark">${book.library_name}</td>
                    <td class="text-dark">${book.added_by}</td>
                    <td class="text-dark">${book.book_id}</td>
                    <td class="text-dark">${book.quantity}</td>
                    <td class="text-dark">${book.publication_year}</td>
                    <td>${statusBadge}</td>
                    `;
        tableBodyRejected.appendChild(row);

    });
}

// Kitob holatini o'zgartirish
function fillModal(bookId, bookTitle) {
    // Modal oynani o'chirish
    const confirmModal = document.getElementById('confirmModal');
    confirmModal.innerHTML = '';

    // Modalning HTML kodini yaratish
    const modalContent = `
        <div class="modal-header">
            <h5 class="modal-title" id="staticBackdropLabel">Kitobni tasdiqlash</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
            <p>${bookTitle} ni tasdiqlamoqchimisiz?</p>
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-outline-success" onclick="changeBookStatus(${bookId}, 'accepted')" data-bs-dismiss="modal">Tasdiqlash</button>
        </div>
    `;

    // Modalga HTML kodini joylash
    confirmModal.innerHTML = modalContent;
}

function changeBookStatus(bookId, newStatus) {
    // CSRF tokenini olish
    var csrftoken = getCookie('csrftoken'); // Xo'sh tabadallangan CSRF tokenini olish uchun funksiya

    // Hozirgi statusni "rejected" bo'lsa, yangi statusni "accepted" ga o'zgartiramiz
    var newStatus = newStatus === 'rejected' ? 'accepted' : newStatus;

    // Axios orqali POST so'rovi yuborish
    axios.post(`/library/change_book_status/${bookId}/`, {
        new_status: newStatus
    }, {
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        }
    })
        .then(function (response) {
            // Agar o'zgartirish muvaffaqiyatli bo'lsa, ma'lumotlarni qayta yuklaymiz
            fetchData();
        })
        .catch(function (error) {
            console.error('Xatolik:', error);
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

// Modalni ochish funksiyasi
var selectElement = document.getElementById("publication_year");

var currentYear = new Date().getFullYear(); // Hozirgi yil
var startYear = 2015; // Boshlang'ich yil
var endYear = currentYear; // Oxirgi yil
for (var year = startYear; year <= endYear; year++) {
    var option = document.createElement("option");
    option.value = year;
    option.text = year;
    selectElement.appendChild(option);
}


// Modalni yopish funksiyasi
function closeModal() {
    $('#exampleModal').modal('hide');
}
function openModal() {
    $('#exampleModal').modal('show');
}

// Ma'lumotlarni olishni boshlash
fetchData();