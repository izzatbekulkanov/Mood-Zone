<!-- Asyn sorov yuborish Code -->
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
    xhr.open('GET', '/library/book_list_json', true);

    // AJAX so'rovini jo'natish
    xhr.send();
}

<!-- Asyn sorov yuborish Code -->
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
                        <button class="btn btn-icon btn-primary rounded-pill btn-sm">
                            <span class="btn-inner">
                             <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="32" height="32" viewBox="0 0 24 24"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>
                            </span>
                        </button>
                    </td> 
                    `;
        tableBody.appendChild(row);
    });
}

fetchData();

function validateForm() {
    var isValid = true;

    // Barcha zarur maydonlarni tekshirish
    $('#bookForm input[required], #bookForm select[required], #bookForm textarea[required]').each(function () {
        if ($.trim($(this).val()) == '') {
            isValid = false;
            $(this).addClass('is-invalid');
        } else {
            $(this).removeClass('is-invalid');
        }
    });


    if (!isValid) {
        Swal.fire({
            position: 'top-end',
            icon: 'error',
            backdrop: `rgba(60,60,60,0.8)`,
            title: 'Kitob ma\'lumotlarini to\'g\'ri kiriting ',
            showConfirmButton: false,
            timer: 3000
        });
    }

    return isValid;
}

<!-- Formani yuborish Code -->
function submitForm() {
    if (validateForm()) {
        var bookForm = document.getElementById("bookForm");
        var formData = new FormData(bookForm);

        // Tasdiqlash belgisini tekshirib, agar belgi belgilangan bo'lsa 'accepted' qilib sozlash
        if (document.getElementById("remebercheck2").checked) {
            formData.set("status", "accepted");
        } else {
            // Agar checkbox tanlanmagan bo'lsa, statusni "rejected" qilib sozlash
            formData.set("status", "rejected");
        }

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/library/save_book", true);
        xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    console.log(xhr.responseText);
                    // Formani tozalash
                    bookForm.reset();
                    // Modal oynani ochish
                    Swal.fire({
                        title: '<strong>Kitob muvaffaqiyatli saqlandi</strong>',
                        icon: 'success',
                        html: 'Yangi kitob kiritasizmi',
                        backdrop: `rgba(60,60,60,0.8)`,
                        showCloseButton: true,
                        showCancelButton: true,
                        confirmButtonText: '<i class="fa fa-thumbs-up"></i>Yangi kitob kitish!',
                        confirmButtonAriaLabel: 'Thumbs up, great!',
                        cancelButtonText: '<i class="fa fa-thumbs-down"></i> Cancel',
                        cancelButtonAriaLabel: 'Thumbs down, cancel!',
                        preConfirm: function () {
                            // Modalni ochadigan funksiya
                            $('#exampleModal').modal('show');
                        },
                        willClose: function () {
                            // Modalni Yopadigan funksiya
                            $('#exampleModal').modal('hide');
                        },
                    });

                    // Modalni yopish
                    closeModal();
                } else {
                    console.error("Xatolik sodir bo'ldi!");
                }
            }
        };

        xhr.send(formData);
    }

    function closeModal() {


        $('#exampleModal').modal('hide');
    }
}

<!-- Yillarni tanlash Script -->
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

<!-- Modalni yopish Script -->
function closeModal() {
    $('#exampleModal').modal('hide');
}