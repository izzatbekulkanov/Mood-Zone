/*
* Version: 1.1.0
* Template: Hope-Ui - Responsive Bootstrap 5 Admin Dashboard Template
* Author: iqonic.design
* Design and Developed by: iqonic.design
* NOTE: This file contains the script for initialize & listener Template.
*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

:: FullScreen
:: Font size change script
:: header toggle
:: Pro Sidebar Left Active Border
:: Reset Settings
:: Copy Json
:: Logo Change Functionality Preview purpose only based on user selected file

------------------------------------------------
Index Of Script
----------------------------------------------*/
"use strict";
/*---------------------------------------------------------------------
            FullScreen
-----------------------------------------------------------------------*/
jQuery( document ).ready(function() {
    jQuery(".search-full").click(function(){
        jQuery(".search-mini").toggleClass("active");

        });
});

jQuery(document).on('click', '.iq-full-screen', function() {
    if (!document.fullscreenElement &&
        !document.mozFullScreenElement && // Mozilla
        !document.webkitFullscreenElement && // Webkit-Browser
        !document.msFullscreenElement) { // MS IE ab version 11

        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen();
        } else if (document.documentElement.mozRequestFullScreen) {
            document.documentElement.mozRequestFullScreen();
        } else if (document.documentElement.webkitRequestFullscreen) {
            document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
        } else if (document.documentElement.msRequestFullscreen) {
            document.documentElement.msRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
        }
        document.querySelector('.iq-full-screen').querySelector('.normal-screen').classList.add('d-none');
        document.querySelector('.iq-full-screen').querySelector('.full-normal-screen').classList.remove('d-none');
    } else {
        if (document.cancelFullScreen) {
            document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        } else if (document.msExitFullscreen) {
            document.msExitFullscreen();
        }
        document.querySelector('.iq-full-screen').querySelector('.full-normal-screen').classList.add('d-none');
        document.querySelector('.iq-full-screen').querySelector('.normal-screen').classList.remove('d-none');
    }
});

/*---------------------------------------------------------------------
            Font size change script
-----------------------------------------------------------------------*/

const sizes = document.querySelectorAll('[data-change="fs"]');
sizes.forEach(size => size.addEventListener('click', () => changeSize(size) ));
function changeSize(params) {
    const size = params.dataset.size;
    sizes.forEach(params => params.classList.remove('btn-primary'));
    if (document.querySelector('html').style.fontSize !== size) {
        document.querySelector('html').style.fontSize = size;
        params.classList.add('btn-primary');
    } else {
        document.querySelector('html').style.removeProperty('font-size');
    }
    window.dispatchEvent(new Event('resize'));
    hideTooltip();
}

function hideTooltip() {
    const tooltipElms = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    tooltipElms.forEach(tooltipElm => {
        const tooltip = bootstrap.Tooltip.getInstance(tooltipElm)
        tooltip.hide();
    });

}

/*---------------------------------------------------------------------
            header toggle
-----------------------------------------------------------------------*/
const toggleelem = document.getElementById('navbarSupportedContent');
const offcanvasheader = document.getElementById('offcanvasBottom')
if(offcanvasheader !== null && offcanvasheader !== undefined) {
    const bsOffcanvas = new bootstrap.Offcanvas(offcanvasheader);
    toggleelem.addEventListener('show.bs.collapse', function () {
        bsOffcanvas.show()
        document.querySelector('.offcanvas-backdrop').addEventListener('click',function(){
            const toggleInstace = bootstrap.Collapse.getInstance(toggleelem)
            toggleInstace.hide()
        })
    })
    toggleelem.addEventListener('hide.bs.collapse', function () {
        bsOffcanvas.hide()
    })
}

const toggleelem1 = document.getElementById('navbarSupportedContent1');
const offcanvas = document.getElementById('offcanvasBottom1')
if(offcanvas !== null && toggleelem1 !== null){
    const offcanvas = new bootstrap.Offcanvas();
    toggleelem1.addEventListener('show.bs.collapse', function () {
        offcanvas.show()
        document.querySelector('.offcanvas-backdrop').addEventListener('click',function(){
            const toggleInstace = bootstrap.Collapse.getInstance(toggleelem1)
            toggleInstace.hide()
        })
    })
    toggleelem1.addEventListener('hide.bs.collapse', function () {
        offcanvas.hide()
    })
}

$('.iq-status').on('change',function(){
    const status = $(this).is(":checked")
    if(status){
        $(".iq-reset-status").text("Online")
    } else{
        $(".iq-reset-status").text("Offline")
    }
})

$(".delete-btn").on("click" ,function() {
    const __this = $(this)
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to delete this item",
        icon: 'error',
        showCancelButton: true,
        backdrop: `rgba(60,60,60,0.8)`,
        confirmButtonText: 'Yes, delete it!',
        confirmButtonColor: "#c03221"
    }).then((result) => {
    if (result.isConfirmed) {
            $(__this).closest('[data-item="list"]').remove();
            Swal.fire(
                'Deleted!',
                'Your item has been deleted.',
                'success'
            )
        }
    })
})

$(".restore-btn").on("click" ,function() {
    const __this = $(this)
    Swal.fire({
        title: 'Are you sure?',
        text: "You want to restore this item",
        icon: 'info',
        showCancelButton: true,
        backdrop: `rgba(60,60,60,0.8)`,
        confirmButtonText: 'Yes',
        confirmButtonColor: "#c03221"
    }).then((result) => {
    if (result.isConfirmed) {
            $(__this).closest('[data-item="list"]').remove();
            Swal.fire(
                'Restore!',
                'Your item has been restore.',
                'success'
            )
        }
    })
})
$(".wishlist-btn").on("click" ,function() {
    Swal.fire(
        'Added!',
        'Your item has been Added to the wishlist.',
        'success'
    )
})

$(".cart-btn").on("click" ,function() {
    Swal.fire(
        'Added!',
        'Your item has been Added to the cart.',
        'success'
    )
})
