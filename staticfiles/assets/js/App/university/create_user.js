$(document).ready(function () {
    $('#save_student_data_base').click(function () {
        createStudentFromApi();
    });
});

function createStudentFromApi() {
    var studentIdNumber = $('#student_id_raqami').val();
    var csrfToken = $('input[name=csrfmiddlewaretoken]').val();  // CSRF tokenini olish
    var save_button_div = $('#save_button_div')

    if (studentIdNumber) {
        $.ajax({
            url: 'create_student_from_api',
            type: 'POST',
            dataType: 'json',
            data: {
                'csrfmiddlewaretoken': csrfToken,  // CSRF tokenini yuborish
                'student_id_number': studentIdNumber
            },
            success: function (response) {
                if (response.success) {
                    // Talaba muvaffaqiyatli saqlandi

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
                    $('#student_id_num').val('');
                    save_button_div.empty();
                    save_button_div.innerHTML = `<button class="btn btn-primary w-100 mt-3 p-3 " id="save_student_data_base" onclick=createStudentFromApi();
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
            title: 'Talaba ma\'lumotlari to\'ldirilmagan ',
            showConfirmButton: false,
            timer: 2000
        });
    }
}

$(document).ready(function () {
    $('#studentInfoForm').submit(function (event) {
        event.preventDefault(); // Boshqa sahifaga o'tkazishni to'xtatish
        var studentIdNumber = $('#student_id_num').val();
        var save_button_div = $('#save_button_div')

        fetchStudentInfo(studentIdNumber);
    });
});
if (studentIdNumber.length > 5) {
    $('#save_button_div').append('<button class="btn btn-success w-100 mt-3 p-3 " id="save_student_data_base" onclick=createStudentFromApi(); type="button">Saqlash</button>');
}

function fetchStudentInfo(studentIdNumber) {
    var url_id = '/university/get_student_info?student_id_number=';
    $.ajax({
        url: url_id + studentIdNumber,
        type: 'GET',
        dataType: 'json',

        success: function (data, status, xhr) {
            if (xhr.status === 200) {
                save_button_div.innerHTML = ''
                save_button_div.innerHTML = `<button class="btn btn-success w-100 mt-3 p-3 " id="save_student_data_base" onclick=createStudentFromApi();
                                            type="button"> Yangilash
                                    </button>`
            } else {
                save_button_div.innerHTML = ''
                save_button_div.innerHTML = `<button class="btn btn-primary w-100 mt-3 p-3 " id="save_student_data_base" onclick=createStudentFromApi();
                                            type="button"> Saqlash
                                    </button>`
            }

            displayStudentInfo(data);

        },
        error: function (xhr, status, error) {
            console.error('Xatolik:', error);
        }
    });
}

function displayStudentInfo(data) {

    var data = data.data; // Ma'lumotlar obyektini olish
    var userImage = $('#user_image');
    var bigImageLink = document.getElementById('bigImage');
    $('#first_name').val(data.first_name);
    $('#second_name').val(data.second_name);
    $('#third_name').val(data.third_name);
    $('#university').val(data.university.name);
    $('#student_id_raqami').val(data.student_id_number);
    $('#genderinfo').val(data.gender.name);
    $('#country').val(data.country.name);
    $('#province').val(data.province.name);
    $('#district').val(data.district.name);
    $('#citizenship').val(data.citizenship.name);
    $('#studentStatus').val(data.studentStatus.name);
    $('#educationForm').val(data.educationForm.name);
    $('#educationTypeInfo').val(data.educationType.name);
    $('#paymentForm').val(data.paymentForm.name);
    $('#accommodation').val(data.accommodation.name);
    $('#department').val(data.department.name);
    $('#group').val(data.group.name);
    $('#level').val(data.level.name);
    $('#semester').val(data.semester.name);
    $('#educationYearInfo').val(data.educationYear.name);
    $('#year_of_enter').val(data.year_of_enter);
    userImage.attr('src', data.image);
    bigImageLink.setAttribute('href', data.image);
}