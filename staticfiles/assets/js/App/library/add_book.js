<!-- Asyn sorov yuborish Code -->
function fetchData() {
    // Axios orqali GET so'rovini yaratish
    axios.get('/library/book_list_json')
        .then(function (response) {
            // Ma'lumotlarni jadvalga qo'yish uchun funksiya chaqirish
            displayLatestBooks(response.data.latest_books);
        })
        .catch(function (error) {
            // Xatolikni konsolga chiqarish
            console.error('Error fetching data:', error);
        });
}


<!-- Asyn sorov yuborish Code -->
function displayLatestBooks(latest_books) {
    const tableBodyRejected = document.getElementById('book-table-body');
    tableBodyRejected.innerHTML = ''; // Eski ma'lumotlarni o'chirish
    // Ma'lumotlar to'plamidagi har bir kitob uchun yangi bir tr elementini jadvalga qo'shish
    latest_books.forEach((book, index) => {
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
                    <td class="text-dark">${book.created_at}</td>                    
                    <td>${statusBadge}</td>`;
        tableBodyRejected.appendChild(row);

    });
}

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

        axios.post('/library/save_book', formData, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'Content-Type': 'multipart/form-data'
            }
        })
        .then(function (response) {
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
                    // Modalni yopadigan funksiya
                    $('#exampleModal').modal('hide');
                    // Ma'lumotlarni qayta yuklash
                    fetchData(); // Ma'lumotlarni qayta yuklash
                },
            });

            // Modalni yopish
            closeModal();
        })
        .catch(function (error) {
            console.error("Xatolik sodir bo'ldi!", error);
        });
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

fetchData();