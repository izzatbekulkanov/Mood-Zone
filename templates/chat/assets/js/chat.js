"use strict";

const chatTabs = document.querySelectorAll('#sidebar-menu [data-bs-toggle="tab"]')
_.forEach(chatTabs, function(elem) {
    const instance = bootstrap.Tab.getInstance(elem)
    elem.addEventListener('shown.bs.tab', function(e) {
        chatTabs.forEach(function(elem) {
            elem.closest('li').classList.remove('active')
        })
        e.target.closest('li').classList.add('active')
    })
})

function openUrl(e, elem) {
    e.preventDefault()
    console.log(elem.dataset.href)
    window.open(elem.dataset.href, '_blank')
}