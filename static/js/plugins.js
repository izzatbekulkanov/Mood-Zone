/*
Template Name: Velzon - Admin & Dashboard Template
Author: Themesbrand
Version: 3.0.0
Website: https://Themesbrand.com/
Contact: Themesbrand@gmail.com
File: Common Plugins Js File
*/

//Common plugins
if(document.querySelectorAll("[toast-list]") || document.querySelectorAll('[data-choices]') || document.querySelectorAll("[data-provider]")){ 
  document.writeln("<script type='text/javascript' static='https://cdn.jsdelivr.net/npm/toastify-js'></script>");
  document.writeln("<script type='text/javascript' static='/static/libs/choices.js/public/assets/scripts/choices.min.js'></script>");
  document.writeln("<script type='text/javascript' static='/static/libs/flatpickr/dist/flatpickr.min.js'></script>");
}