/*
* Version: 1.1.0
* Template: Hope-Ui Pro - Responsive Bootstrap 5 Admin Dashboard Template
* Author: iqonic.design
* Design and Developed by: iqonic.design
* NOTE: This file contains the script for initialize & listener Template.
*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

:: Mailbox

------------------------------------------------
Index Of Script
----------------------------------------------*/
"use strict";

/*---------------------------------------------------------------------
            Mailbox
-----------------------------------------------------------------------*/
jQuery(document).on('click', 'ul.iq-email-sender-list li', function(e) {
    if (e.target.closest('.email-app-details') === null) {
        jQuery(this).find('.email-app-details').addClass('show');
    }
});

jQuery(document).on('click', '.email-remove', function(e) {
    jQuery(this).closest('.email-app-details').removeClass('show');
});