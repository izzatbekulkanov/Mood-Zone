function submitForm() {
    // Formdan ma'lumotlarni olish
    var formData = new FormData();
    formData.append('name', document.getElementById('libraryName').value);
    formData.append('address', document.getElementById('libraryAdress').value);
    formData.append('number', document.getElementById('libraryNumber').value);
    formData.append('status', document.getElementById('remebercheck2').checked ? true : false);

    // CSRF tokenini olish
    var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    formData.append('csrfmiddlewaretoken', csrfToken);

    // Kutubhonani yaratish uchun POST so'rovini yuborish
    axios.post('/library/create_library_json/', formData)
        .then(function (response) {
            // Muvaffaqiyatli javob
            console.log(response);
            clearForm();
            closeModal(); // Modalni yopish
            fetchData();
            // Success toast chiqarish
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
                icon: 'success',
                title: response.data.message
            });
        })
        .catch(function (error) {
            // Xatolik
            console.error(error);
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
                title: response.data.message
            });
        });

    function clearForm() {
        // Formdagi barcha inputlarni tozalash
        document.getElementById('libraryName').value = '';
        document.getElementById('libraryAdress').value = '';
        document.getElementById('libraryNumber').value = '';
        document.getElementById('remebercheck2').checked = false;
    }
}

function closeModal() {
    // Modalni yopish uchun JavaScript kodlari
    $('#addLibraryModal').modal('hide');
}

function fetchData() {
    axios.get('libraries_list/')
        .then(function (response) {
            // Ma'lumotlarni olish muvaffaqiyatli bo'lganda amallar
            var libraries = response.data;
            renderTable(libraries);
        })
        .catch(function (error) {
            // Xatolik bo'lganda qilinishi kerak bo'lgan amallar
            console.log(error);
        });
}

function renderTable(data) {
    var tableBody = document.querySelector('#datatable tbody');
    tableBody.innerHTML = '';

    data.forEach(function (library) {
        var row = document.createElement('tr');

        var nameCell = document.createElement('td');
        nameCell.textContent = library.name;
        row.appendChild(nameCell);

        var addressCell = document.createElement('td');
        addressCell.textContent = library.address;
        row.appendChild(addressCell);

        var userCell = document.createElement('td');
        userCell.innerHTML = library.admin ? `<button type="button" class="btn btn-success btn-sm">${library.admin.full_name}</button>` : '<button type="button" class="btn btn-danger btn-sm">Admin yoq</button>';
        row.appendChild(userCell);

        var editCell = document.createElement('td');
        editCell.innerHTML = '<button class="btn btn-icon btn-warning">\n' +
            '        <span class="btn-inner">' +
            '             <svg fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-32" width="15" height="15" viewBox="0 0 20 20"><path fill-rule="evenodd" clip-rule="evenodd" d="M9.3764 20.0279L18.1628 8.66544C18.6403 8.0527 18.8101 7.3443 18.6509 6.62299C18.513 5.96726 18.1097 5.34377 17.5049 4.87078L16.0299 3.69906C14.7459 2.67784 13.1541 2.78534 12.2415 3.95706L11.2546 5.23735C11.1273 5.39752 11.1591 5.63401 11.3183 5.76301C11.3183 5.76301 13.812 7.76246 13.8651 7.80546C14.0349 7.96671 14.1622 8.1817 14.1941 8.43969C14.2471 8.94493 13.8969 9.41792 13.377 9.48242C13.1329 9.51467 12.8994 9.43942 12.7297 9.29967L10.1086 7.21422C9.98126 7.11855 9.79025 7.13898 9.68413 7.26797L3.45514 15.3303C3.0519 15.8355 2.91395 16.4912 3.0519 17.1255L3.84777 20.5761C3.89021 20.7589 4.04939 20.8879 4.24039 20.8879L7.74222 20.8449C8.37891 20.8341 8.97316 20.5439 9.3764 20.0279ZM14.2797 18.9533H19.9898C20.5469 18.9533 21 19.4123 21 19.9766C21 20.5421 20.5469 21 19.9898 21H14.2797C13.7226 21 13.2695 20.5421 13.2695 19.9766C13.2695 19.4123 13.7226 18.9533 14.2797 18.9533Z" fill="currentColor"></path></svg>' +
            '        </span>' +
            '    </button>';
        row.appendChild(editCell);

        tableBody.appendChild(row);
    });
}

fetchData()