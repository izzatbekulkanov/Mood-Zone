document.addEventListener('DOMContentLoaded', function () {
    // API dan ma'lumotlarni olish
    fetch('https://api.example.com/users') // API_URL orqasiga API manzilingizni qo'shing
        .then(response => response.json())
        .then(data => {
            // Chiqarish funksiyasini chaqirish
            renderUsers(data.users);
        })
        .catch(error => console.error('Ma\'lumotlarni olishda xato:', error));
});

// Ma'lumotlarni chiqarish funksiyasi
function renderUsers(users) {
    const userTableBody = document.getElementById('userTableBody');
    const userTemplate = document.getElementById('userTemplate').innerHTML;

    // Har bir foydalanuvchini shablon bilan HTML-ga qo'shish
    users.forEach(user => {
        const userHtml = userTemplate.replace(/{{\s*user\.(\w+)\s*}}/g, (match, p1) => user[p1]);
        userTableBody.innerHTML += userHtml;
    });
}
