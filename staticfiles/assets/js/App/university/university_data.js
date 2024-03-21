document.getElementById("updateAll").addEventListener("click", async function () {
    await updateUniversity('matn');
    await wait(1500); // 1 sekund kutsish
    await updateGroup('matn');
    await wait(1500); // 1 sekund kutsish
    await updateCurriculum('matn');
    await wait(1500); // 1 sekund kutsish
    await updateSpecialty('matn');
    await wait(1500); // 1 sekund kutsish
    await saveDepartments('matn');
});

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function getCurrentTime() {
    // Hozirgi vaqtni olish
    var now = new Date();
    // Soat va minutlarni olish
    var hours = now.getHours();
    var minutes = now.getMinutes();
    // Soat va minutlarni ikki raqamga olib, 0 dan boshlab boshqa sonlar qo'shilganiga e'tibor qilish
    if (hours < 10) {
        hours = '0' + hours;
    }
    if (minutes < 10) {
        minutes = '0' + minutes;
    }
    // Vaqtni formatlash va qaytarish
    return hours + ':' + minutes;
}


function updateUniversity(text) {
    // "Update" tugmasining matnini "Yangilanmoqda" ga o'zgartirish
    document.getElementById('uButton').innerHTML = `<button class="btn btn-success " type="button" disabled="">
                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                    Update
                                </button>`;
    let DataApi = document.getElementById('errorDataApi')

    // AJAX so'rovi yuborish
    $.ajax({
        url: 'save_university_from_api', // Uni yangilash uchun Django view manzili
        type: 'GET',
        success: function (response) {
            if (text === 'matn') {
                DataApi.innerHTML += (`
                <div class="p-2 bd-example align-items-center col-4 p-1">
                            <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                                <div class="toast-header">
                                    <svg class="rounded bd-placeholder-img me-2" width="20" height="20"
                                         xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
                                         preserveAspectRatio="xMidYMid slice" focusable="false">
                                        <rect width="100%" height="100%" fill="#2E7D69"></rect>
                                    </svg>

                                    <strong class="me-auto">Universitet</strong>
                                    <small class="text-muted">${getCurrentTime()}</small>
                                    <button type="button" class="btn-close" data-bs-dismiss="toast"
                                            aria-label="Close"></button>
                                </div>
                                <div class="toast-body">
                                    Universitetlar ro'yhati muvaffaqiyatli yangilandi
                                </div>
                            </div>

                        </div>
                `)
            }
            // Boshqa xolatda muvaffaqiyatli ish bajarildi
           else {
                Swal.fire({
                position: 'top-end',
                icon: 'success',
                background: `rgba(60,60,60,0.8)`,
                title: 'Universitetlar muvaffaqiyatli yangilandi',
                showConfirmButton: false,
                timer: 2000
            });
            }
        },
        error: function (xhr, errmsg, err) {
            Swal.fire({
                position: 'top-end',
                icon: 'error',
                background: `rgba(60,60,60,0.8)`,
                title: 'HEMIS bilan boglanishda muammo yuzaga keldi',
                showConfirmButton: false,
                timer: 2000

            });
            document.getElementById('uButton').innerHTML = `
                    <button class="btn btn-outline-danger" onClick="updateUniversity()">
                                <span >Update</span>
                            </button>
                    `;
            console.log(xhr.status + ": " + xhr.responseText); // Xatoni konsolga chiqaring
        },
        complete: function () {
            // So'rov tugadi, "Update" tugmasining matnini "Update" ga tiklash
            document.getElementById('uButton').innerHTML = `
                    <button class="btn btn-outline-success" onClick="updateUniversity()">
                                <span >Update</span>
                            </button>
                    `;
            getUniversities();
        }
    });
}

function updateSpecialty(text) {
    // "Update" tugmasining matnini "Yangilanmoqda" ga o'zgartirish
    document.getElementById('updateSpecialtyButton').innerHTML = `<button class="btn btn-success " type="button" disabled="">
                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                    Update
                                </button>`;
    let DataApi = document.getElementById('errorDataApi')

    // AJAX so'rovi yuborish
    $.ajax({
        url: 'save_specialty_from_api', // Uni yangilash uchun Django view manzili
        type: 'GET',
        success: function (response) {
            if (text === 'matn') {
                DataApi.innerHTML += (`
                <div class="p-2 bd-example align-items-center col-4 p-1">
                            <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                                <div class="toast-header">
                                    <svg class="rounded bd-placeholder-img me-2" width="20" height="20"
                                         xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
                                         preserveAspectRatio="xMidYMid slice" focusable="false">
                                        <rect width="100%" height="100%" fill="#2E7D69"></rect>
                                    </svg>

                                    <strong class="me-auto">Mutaxassislik</strong>
                                    <small class="text-muted">${getCurrentTime()}</small>
                                    <button type="button" class="btn-close" data-bs-dismiss="toast"
                                            aria-label="Close"></button>
                                </div>
                                <div class="toast-body">
                                    Mutaxassisliklar ro'yhati muvaffaqiyatli yangilandi
                                </div>
                            </div>

                        </div>
                `)
            }
            // Boshqa xolatda muvaffaqiyatli ish bajarildi
            else {
                Swal.fire({
                position: 'top-end',
                icon: 'success',
                background: `rgba(60,60,60,0.8)`,
                title: 'Mutaxassisliklar ro\'yhati muvaffaqiyatli yangilandi',
                showConfirmButton: false,
                timer: 2000
            });
            }
        },
        error: function (xhr, errmsg, err) {
            Swal.fire({
                position: 'top-end',
                icon: 'error',
                background: `rgba(60,60,60,0.8)`,
                title: 'HEMIS bilan boglanishda muammo yuzaga keldi',
                showConfirmButton: false,
                timer: 2000
            });
            document.getElementById('uButton').innerHTML = `
                    <button class="btn btn-outline-danger" onClick="updateUniversity()">
                                <span >Update</span>
                            </button>
                    `;
            console.log(xhr.status + ": " + xhr.responseText); // Xatoni konsolga chiqaring
        },
        complete: function () {
            // So'rov tugadi, "Update" tugmasining matnini "Update" ga tiklash
            document.getElementById('updateSpecialtyButton').innerHTML = `
                    <button class="btn btn-outline-success" onClick="updateSpecialty()">
                                <span >Update</span>
                            </button>
                    `;
            getUniversities();
        }
    });

}

function updateCurriculum(text) {
    // "Update" tugmasining matnini "Yangilanmoqda" ga o'zgartirish
    document.getElementById('updateCurriculumButton').innerHTML = `<button class="btn btn-success " type="button" disabled="">
                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                    Update
                                </button>`;
    let DataApi = document.getElementById('errorDataApi')


    // AJAX so'rovi yuborish
    $.ajax({
        url: 'save_curriculum_from_api', // Uni yangilash uchun Django view manzili
        type: 'GET',
        success: function (response) {
            if (text === 'matn') {
                DataApi.innerHTML += (`
                <div class="p-2 bd-example align-items-center col-4 p-1">
                            <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                                <div class="toast-header">
                                    <svg class="rounded bd-placeholder-img me-2" width="20" height="20"
                                         xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
                                         preserveAspectRatio="xMidYMid slice" focusable="false">
                                        <rect width="100%" height="100%" fill="#2E7D69"></rect>
                                    </svg>

                                    <strong class="me-auto">O\'quv reja</strong>
                                    <small class="text-muted">${getCurrentTime()}</small>
                                    <button type="button" class="btn-close" data-bs-dismiss="toast"
                                            aria-label="Close"></button>
                                </div>
                                <div class="toast-body">
                                    O\'quv rejalar ro'yhati muvaffaqiyatli yangilandi
                                </div>
                            </div>

                        </div>
                `)
            }
            // Boshqa xolatda muvaffaqiyatli ish bajarildi
            else {
                Swal.fire({
                position: 'top-end',
                icon: 'success',
                background: `rgba(60,60,60,0.8)`,
                title: 'O\'quv rejalar ro\'yhati muvaffaqiyatli yangilandi',
                showConfirmButton: false,
                timer: 2000
            });
            }
        },
        error: function (xhr, errmsg, err) {
            Swal.fire({
                position: 'top-end',
                icon: 'error',
                background: `rgba(60,60,60,0.8)`,
                title: 'HEMIS bilan boglanishda muammo yuzaga keldi',
                showConfirmButton: false,
                timer: 2000
            });
            document.getElementById('uButton').innerHTML = `
                    <button class="btn btn-outline-danger" onClick="updateUniversity()">
                                <span >Update</span>
                            </button>
                    `;
            console.log(xhr.status + ": " + xhr.responseText); // Xatoni konsolga chiqaring
        },
        complete: function () {
            // So'rov tugadi, "Update" tugmasining matnini "Update" ga tiklash
            document.getElementById('updateCurriculumButton').innerHTML = `
                    <button class="btn btn-outline-success" onClick="updateCurriculum()">
                                <span >Update</span>
                            </button>
                    `;
            getUniversities();

        }
    });
}

function updateGroup(text) {
    // "Update" tugmasining matnini "Yangilanmoqda" ga o'zgartirish
    document.getElementById('updateGroupButton').innerHTML = `<button class="btn btn-success " type="button" disabled="">
                                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                                    Update
                                </button>`;
    let DataApi = document.getElementById('errorDataApi')


    // AJAX so'rovi yuborish
    $.ajax({
        url: 'save_group_from_api', // Uni yangilash uchun Django view manzili
        type: 'GET',
        success: function (response) {
            if (text === 'matn') {
                DataApi.innerHTML += (`
                <div class="p-2 bd-example align-items-center col-4 p-1">
                            <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                                <div class="toast-header">
                                    <svg class="rounded bd-placeholder-img me-2" width="20" height="20"
                                         xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
                                         preserveAspectRatio="xMidYMid slice" focusable="false">
                                        <rect width="100%" height="100%" fill="#2E7D69"></rect>
                                    </svg>

                                    <strong class="me-auto">Akademik guruh</strong>
                                    <small class="text-muted">${getCurrentTime()}</small>
                                    <button type="button" class="btn-close" data-bs-dismiss="toast"
                                            aria-label="Close"></button>
                                </div>
                                <div class="toast-body">
                                    Akademik guruhlar ro'yhati muvaffaqiyatli yangilandi
                                </div>
                            </div>

                        </div>
                `)
            }
            // Boshqa xolatda muvaffaqiyatli ish bajarildi
            else {
                Swal.fire({
                position: 'top-end',
                icon: 'success',
                background: `rgba(60,60,60,0.8)`,
                title: 'Akademik guruhlar ro\'yhati muvaffaqiyatli yangilandi',
                showConfirmButton: false,
                timer: 2000
            });
            }
        },
        error: function (xhr, errmsg, err) {
            Swal.fire({
                position: 'top-end',
                icon: 'error',
                background: `rgba(60,60,60,0.8)`,
                title: 'HEMIS bilan boglanishda muammo yuzaga keldi',
                showConfirmButton: false,
                timer: 2000
            });
            document.getElementById('uButton').innerHTML = `
                    <button class="btn btn-outline-danger" onClick="updateUniversity()">
                                <span >Update</span>
                            </button>
                    `;
            console.log(xhr.status + ": " + xhr.responseText); // Xatoni konsolga chiqaring
        },
        complete: function () {
            // So'rov tugadi, "Update" tugmasining matnini "Update" ga tiklash
            document.getElementById('updateGroupButton').innerHTML = `
                    <button class="btn btn-outline-success" onClick="updateCurriculum()">
                                <span >Update</span>
                            </button>
                    `;
            getUniversities();
        }
    });

}

function getUniversities() {
    $.ajax({
        url: 'get_universities_data', // get_universities funksiyasini chaqirish uchun Django view manzili
        type: 'GET',
        success: function (response) {
            displayUniversities('university-table', response.universities);
            displayCount('univercount', response.count);
            displayUniversities('specialty-table', response.specialty);
            displayCount('specialtycount', response.specialty_count);
            displayCurriculum('curriculum-table', response.curriculums);
            displayCount('curriculumcount', response.curriculums_count);
            displayGroups('group-table', response.groups);
            displayCount('groupcount', response.groups_count);
        },
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // Xatolikni konsolga chiqarish
        }
    });
}

function saveDepartments(text) {
    let DataApi = document.getElementById('errorDataApi')

    $.ajax({
        url: 'save_department',
        type: 'GET',
        success: function (response) {
            if (text === 'matn') {
                DataApi.innerHTML += (`
                <div class="p-2 bd-example align-items-center col-4 p-1">
                            <div class="toast fade show" role="alert" aria-live="assertive" aria-atomic="true">
                                <div class="toast-header">
                                    <svg class="rounded bd-placeholder-img me-2" width="20" height="20"
                                         xmlns="http://www.w3.org/2000/svg" aria-hidden="true"
                                         preserveAspectRatio="xMidYMid slice" focusable="false">
                                        <rect width="100%" height="100%" fill="#2E7D69"></rect>
                                    </svg>

                                    <strong class="me-auto">Fakultet</strong>
                                    <small class="text-muted">${getCurrentTime()}</small>
                                    <button type="button" class="btn-close" data-bs-dismiss="toast"
                                            aria-label="Close"></button>
                                </div>
                                <div class="toast-body">
                                    Fakultetlar ro'yhati muvaffaqiyatli yangilandi
                                </div>
                            </div>

                        </div>
                `)
            }
            // Boshqa xolatda muvaffaqiyatli ish bajarildi
            else {
                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    background: `rgba(60,60,60,0.8)`,
                    title: 'Fakultetlar ro\'yhati muvaffaqiyatli yangilandi',
                    showConfirmButton: false,
                    timer: 2000
                });
            }
        },
        error: function (xhr, status, error) {
            Swal.fire({
                position: 'top-end',
                icon: 'error',
                background: `rgba(60,60,60,0.8)`,
                title: 'HEMIS bilan bog\'lanib bo\'madi',
                showConfirmButton: false,
                timer: 2000
            });
        }
    });
}

function displayUniversities(id, universities) {
    var tableBody = $(`#${id}`);
    tableBody.empty(); // Eski malumotlarni tozalash

    universities.forEach(function (university) {
        var truncatedName = truncateText(university.name, 50);
        var truncatedCode = truncateText(university.code, 50);
        var row = '<tr>' +
            '<td>' + truncatedName + '</td>' +
            '<td>' + truncatedCode + '</td>' +
            '</tr>';
        tableBody.append(row);
    });
}

function displayGroups(id, universities) {
    var tableBody = $(`#${id}`);
    tableBody.empty(); // Eski malumotlarni tozalash

    universities.forEach(function (university) {
        var truncatedName = truncateText(university.name, 50);
        var truncatedCode = truncateText(university.codeID, 50);
        var row = '<tr>' +
            '<td>' + truncatedName + '</td>' +
            '<td>' + truncatedCode + '</td>' +
            '</tr>';
        tableBody.append(row);
    });
}

function displayCurriculum(id, universities) {
    var tableBody = $(`#${id}`);
    tableBody.empty(); // Eski malumotlarni tozalash

    universities.forEach(function (university) {
        var truncatedName = truncateText(university.name, 50);
        var truncatedCode = truncateText(university.codeID, 50);
        var row = '<tr>' +
            '<td>' + truncatedName + '</td>' +
            '<td>' + truncatedCode + '</td>' +
            '</tr>';
        tableBody.append(row);
    });
}

function displayCount(id, count) {
    $(`#${id}`).text(count);
}
function truncateText(text, maxLength) {
    if (text.length > maxLength) {
        return text.substring(0, maxLength) + '...';
    }
    return text;
}

$(document).ready(function () {
    getUniversities();
});
