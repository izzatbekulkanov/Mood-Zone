$(document).ready(function () {
    $('#save_employee_data_base').click(function () {
        createEmployeeFromApi();
    });
});

function createEmployeeFromApi() {
    var employeeIdNumber = $('#employee_id_raqami').val();
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();  // CSRF tokenini olish
    var save_button_div = $('#save_button_div')

    if (employeeIdNumber) {
        $.ajax({
            url: 'create_employee_from_api',
            type: 'POST',
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': csrfToken,  // CSRF tokenini yuborish
                'employee_id_number': employeeIdNumber
            },
            success: function (response) {
                if (response.success) {
                    // Hodim muvaffaqiyatli saqlandi

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
                        title: response.message
                    });
                    $('#employee_id_num').val('');
                    save_button_div.empty();
                    save_button_div.innerHTML = `<button class="btn btn-primary w-100 mt-3 p-3 " id="save_employee_data_base" onclick=createEmployeeFromApi();
                                            type="button"> Saqlash
                                    </button>`

                    // Ilovani qayta yuklash
                } else {
                    // Xatolik yuz berdi
                    Swal.fire({
                        icon: 'error',
                        title: 'Xatolik',
                        text: response.message
                    });
                    alert(response.message);
                }
            },
            error: function (xhr, status, error) {
                console.error('Xatolik:', error);
                alert('Server bilan bog\'lanishda xatolik yuz berdi.');
            }
        });
    } else {
        Swal.fire({
            position: 'top-end',
            icon: 'error',
            background: `rgba(60,60,60,0.8)`,
            title: 'Hodimning ma\'lumotlari to\'ldirilmagan ',
            showConfirmButton: false,
            timer: 2000
        });
    }
}

$(document).ready(function () {
    $('#employeeInfoForm').submit(function (event) {
        event.preventDefault(); // Boshqa sahifaga o'tkazishni to'xtatish
        var employeeIdNumber = $('#employee_id_num').val();

        fetchEmployeeInfo(employeeIdNumber);
    });
});

function fetchEmployeeInfo(employeeIdNumber) {
    var url_id = '/user/get_employee_info?employee_id_number=';
    var save_button_div = $('#save_button_div'); // save_button_div o'zgaruvchisini e'lon qilingan joyga ko'chiring
    $.ajax({
        url: url_id + employeeIdNumber,
        type: 'GET',
        dataType: 'json',

        success: function (data, status, xhr) {
            if (xhr.status === 200) {
                save_button_div.empty(); // save_button_div ni tozalash
                save_button_div.append(`<button class="btn btn-success w-100 mt-3 p-3 " id="save_employee_data_base" onclick=createEmployeeFromApi();
                                            type="button"> Yangilash
                                    </button>`); // save_button_div ga yangi tugmani qo'shish
            } else {
                save_button_div.empty(); // save_button_div ni tozalash
                save_button_div.append(`<button class="btn btn-primary w-100 mt-3 p-3 " id="save_employee_data_base" onclick=createEmployeeFromApi();
                                            type="button"> Saqlash
                                    </button>`); // save_button_div ga yangi tugmani qo'shish
            }
            displayEmployeeInfo(data);

        },
        error: function (xhr, status, error) {
            console.error('Xatolik:', error);
        }
    });
}


function displayEmployeeInfo(data) {
    // JSON obyektining data qismi uchun tekshirish
    if (data.success && data.data && data.data.items && data.data.items.length > 0) {
        var items = data.data.items; // Ma'lumotlar ro'yxatini olish

        // Birinchi ishchining ma'lumotlarini olish
        var firstEmployee = items[0];

        // Ma'lumotlarni HTML elementlariga joylash
        $('#first_name').val(firstEmployee.first_name);
        $('#second_name').val(firstEmployee.second_name);
        $('#third_name').val(firstEmployee.third_name);
        $('#employee_id_raqami').val(firstEmployee.employee_id_number);
        $('#genderinfo').val(firstEmployee.gender.name);
        $('#employeeStatus').val(firstEmployee.employeeStatus.name);
        $('#employeeType').val(firstEmployee.employeeType.name);
        $('#staffPosition').val(firstEmployee.staffPosition.name);
        $('#department').val(firstEmployee.department.name);
        $('#year_of_enter').val(firstEmployee.year_of_enter);

        // Ma'lumot rasmini joylash
        $('#user_image').attr('src', firstEmployee.image);
        document.getElementById('bigImage').setAttribute('href', firstEmployee.image);
    } else {
        console.error('Ma\'lumotlar ro\'yxati bo\'sh yoki yo\'q.');
    }
}