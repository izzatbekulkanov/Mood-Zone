// Kitob turlarini olib kelish uchun fetch funksiyasi
async function fetchBookTypes() {
    try {
        const response = await fetch('get_book_types/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        displayBookTypes(data);

    } catch (error) {
        console.error('Error fetching book types:', error);
    }
}
function displayBookTypes(bookTypes) {
    let book_type_list = document.getElementById('book-type-list');
    // Listni tozalash
    book_type_list.innerHTML = '';

    // Kitob turlarini chiqarish
    bookTypes.forEach((bookType, index) => {
        const row = document.createElement('li');
        row.classList.add('d-flex', 'align-items-center', 'gap-3', 'justify-content-between', 'border-bottom', 'mb-3', 'pb-3', 'flex-column', 'flex-md-row');

        // Rasm manzili bo'sh bo'lmasa, rasmni chiqarish
        let imageHTML = '';
        if (bookType.image_url) {
            imageHTML = `<img src="${bookType.image_url}" width="50" style="width: 80px; height: 80px;" alt="${bookType.name}" class="rounded-circle avatar-48" loading="lazy" />`;
        }

        row.innerHTML = `
            <div class="user-img img-fluid flex-shrink-0">
                <div class="border-profile-card-header ">
                    <div class="sidebar-border-profile-card m-0 p-1">
                        <div class="sidebar-border-profile-body w-75" >
                            ${imageHTML ? imageHTML : `
                            <div class="sidebar-btn m-0" onclick="openImageUploader(${bookType.id})">
                                <span class="sidebar-btn-icon">
                                    <svg class="icon-40" width="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path opacity="0.4" d="M16.6667 2H7.33333C3.92889 2 2 3.92889 2 7.33333V16.6667C2 20.0622 3.92 22 7.33333 22H16.6667C20.0711 22 22 20.0622 22 16.6667V7.33333C22 3.92889 20.0711 2 16.6667 2Z" fill="currentColor"></path>
                                        <path d="M15.3205 12.7083H12.7495V15.257C12.7495 15.6673 12.4139 16 12 16C11.5861 16 11.2505 15.6673 11.2505 15.257V12.7083H8.67955C8.29342 12.6687 8 12.3461 8 11.9613C8 11.5765 8.29342 11.2539 8.67955 11.2143H11.2424V8.67365C11.2824 8.29088 11.6078 8 11.996 8C12.3842 8 12.7095 8.29088 12.7495 8.67365V11.2143H15.3205C15.7066 11.2539 16 11.5765 16 11.9613C16 12.3461 15.7066 12.6687 15.3205 12.7083Z" fill="currentColor"></path>
                                    </svg>
                                </span>
                            </div>
                            `}
                        </div>
                    </div>
                </div>
            </div>
            <div class="d-flex align-items-center justify-content-between w-100 flex-column flex-md-row">
                <div>
                    <h6>${bookType.name}</h6>
                    <p class="mb-0"><b><code>${bookType.book_count}</code></b> ta kitob biriktirilgan</p>
                </div>
                <div class="d-flex align-items-center mt-2 mt-md-0">
                    <div class="d-flex gap-3">
                        <a href="" class="btn btn-primary rounded confirm-btn">Ko'rish</a>                                   
                    </div>
                </div>
            </div>`;
        book_type_list.appendChild(row);
    });
    book_type_list.insertAdjacentHTML('beforeend', `
        <li class="d-block text-center mb-0 pb-0">
            <a href="#" class="btn">View More Request</a>
        </li>
    `);
}


// Dokument yuklandiqda fetchAndDisplayBookTypes() funksiyasini chaqirish

document.getElementById('imageInput').addEventListener('change', function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const imgSrc = e.target.result;

        };
        reader.readAsDataURL(file);
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const bookTypeForm = document.getElementById('bookTypeForm');
    // Forma jo'natilganda hodisa
    bookTypeForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Boshqa sahifaga o'tkazishni to'xtatish
        // Form ma'lumotlarini olish
        const formData = new FormData(this);
        // AJAX orqali ma'lumotlarni serverga yuborish
        fetch('/library/create_book_type', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Ma'lumotni konsolga chiqaring
            console.log(data);

            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer);
                    toast.addEventListener('mouseleave', Swal.resumeTimer);
                }
            });

            if (data.error) {
                // Xatolik bo'lgan holatda
                Toast.fire({
                    icon: 'error',
                    title: data.error
                });
            } else {
                // Kitob turi muvaffaqiyatli saqlanib, forma tozalanadi va ma'lumotni ko'rsatib beradi
                bookTypeForm.reset();
                fetchBookTypes();
                // Xatolik yo'qligida
                Toast.fire({
                    icon: 'success',
                    title: data.message
                });
            }
        })
        .catch(error => {
            // Xatolikni foydalanuvchiga xabardor qilish
            const Toast = Swal.mixin({
                toast: true,
                position: 'top-end',
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.addEventListener('mouseenter', Swal.stopTimer);
                    toast.addEventListener('mouseleave', Swal.resumeTimer);
                }
            });

            Toast.fire({
                icon: 'error',
                title: 'Xatolik yuz berdi. Iltimos, qaytadan urinib ko\'ring.'
            });
        });
    });
});

function get_csrf_token() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.substring('csrftoken='.length, cookie.length);
        }
    }
    return null;
}

function openImageUploader(bookTypeId) {
    const formData = new FormData();
    const csrfToken = get_csrf_token(); // CSRF tokenni olish

    formData.append('csrfmiddlewaretoken', csrfToken); // CSRF tokenni yuborish

    const imageInput = document.createElement('input');
    imageInput.type = 'file';
    imageInput.accept = 'image/*';
    imageInput.addEventListener('change', function() {
        formData.append('image', imageInput.files[0]);
        formData.append('book_type_id', bookTypeId);

        // AJAX so'rovini yuborish
        fetch('/library/save_book_type_image', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Response:', data);
            console.log(data.image_url)
            fetchBookTypes();

            // Rasmni ko'rsatish yoki muvaffaqiyatli saqlandi deb xabarni chiqaring
            Swal.fire({
                title: data.name,
                text: data.message,
                imageUrl: data.image_url, // Tasvirning server tomonidan qaytarilgan manzili
                imageAlt: 'Uploaded image',
                imageWidth: 400,
                imageHeight: 200,
                backdrop: `rgba(60, 60, 60, 0.8)`
            });
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
    });

    // Rasmni tanlash uchun eslatma ochiladi
    imageInput.click();

}

document.addEventListener('DOMContentLoaded', function () {
    fetchBookTypes();
});
