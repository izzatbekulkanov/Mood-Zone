// const sidebar_left_social = new StickySidebar('#sidebar-left-social', {
//     innerWrapperSelector: '.sidebar__inner',
//     topSpacing: 60,
//     bottomSpacing: 60
// });


//social event-detail
const post = document.querySelectorAll('.save');
post.forEach(element => {
    element.addEventListener('click', () => {
        element.classList.add('active');
    })
})