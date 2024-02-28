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
------- Plugin Init --------
:: Tooltip
:: Popover
:: Progress Bar
:: NoUiSlider
:: CopyToClipboard
:: Vanila Datepicker
:: Minus-plus
:: Flatpickr
:: Range Flatpickr
:: Wrap Flatpickr
:: Time Flatpickr
:: Inline Flatpickr
:: SliderTab
:: Data Tables
:: Active Class for Pricing Table
------ Functions --------
:: Resize Plugins
:: Loader Init
:: Sticky-Nav
:: Resize Plugins
:: Sidebar Toggle
:: Back To Top
:: Form Validation
------- Listners ---------
:: DOMContentLoaded
:: Window Resize
------------------------------------------------
Index Of Script
----------------------------------------------*/
(function(){
  "use strict";
  /*------------LoaderInit----------------*/
  const loaderInit = () => {
    const loader = document.querySelector('.loader')
    if(loader !== null) {
      loader.classList.add('animate__animated', 'animate__fadeOut')
      setTimeout(() => {
        loader.classList.add('d-none')
      }, 200)
    }
  }
   /*----------Sticky-Nav-----------*/
   window.addEventListener('scroll', function () {
    let yOffset = document.documentElement.scrollTop;
    let navbar = document.querySelector(".navs-sticky")
    let contaitInner = document.querySelector(".content-inner")
    if (navbar !== null) {
      if (yOffset >= 0) {
        navbar.classList.add("menu-sticky");
        contaitInner.classList.add('navbar-sticky-space');
      } else {
        navbar.classList.remove("menu-sticky");
      }
    } else {
      contaitInner.classList.remove('navbar-sticky-space');
    }
  });
  /*------------Popover--------------*/
  const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  if (typeof bootstrap !== typeof undefined) {
    popoverTriggerList.map(function (popoverTriggerEl) {
      return new bootstrap.Popover(popoverTriggerEl)
    })
  }
  /*-------------Tooltip--------------------*/
  if (typeof bootstrap !== typeof undefined) {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    const sidebarTooltipTriggerList = [].slice.call(document.querySelectorAll('[data-sidebar-toggle="tooltip"]'))
    sidebarTooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })
  }
  /*-------------Progress Bar------------------*/
  const progressBarInit = (elem) => {
    const currentValue = elem.getAttribute('aria-valuenow')
    elem.style.width = '0%'
    elem.style.transition = 'width 2s'
    if (typeof Waypoint !== typeof undefined) {
      new Waypoint({
        element: elem,
        handler: function () {
          setTimeout(() => {
            elem.style.width = currentValue + '%'
          }, 100);
        },
        offset: 'bottom-in-view',
      })
    }
  }
  const customProgressBar = document.querySelectorAll('[data-toggle="progress-bar"]')
  Array.from(customProgressBar, (elem) => {
    progressBarInit(elem)
  })
  /*---------------noUiSlider-------------------*/
  const rangeSlider = document.querySelectorAll('.range-slider');
  Array.from(rangeSlider, (elem) => {
    if (typeof noUiSlider !== typeof undefined) {
      if (elem.getAttribute('id') !== '' && elem.getAttribute('id') !== null) {
        window[elem.getAttribute('id')] = createSlider(elem)
      } else {
        createSlider(elem)
      }
    }
  })
  function createSlider(elem) {
    return noUiSlider.create(elem, {
      start: [50, 2000],
      connect: true,
      range: {
        'min': 0,
        '10%': [50, 50],
        'max': 2000
      }
    })
  }
  const slider = document.querySelectorAll('.slider');
  Array.from(slider, (elem) => {
    if (typeof noUiSlider !== typeof undefined) {
      noUiSlider.create(elem, {
        start: 50,
        connect: [true, false],
        range: {
          'min': 0,
          'max': 100
        }
      })
    }
  })
  /*------------Copy To Clipboard---------------*/
  const copy = document.querySelectorAll('[data-toggle="copy"]')
  if (typeof copy !== typeof undefined) {
    Array.from(copy, (elem) => {
      elem.addEventListener('click', (e) => {
        const target = elem.getAttribute("data-copy-target");
        let value = elem.getAttribute("data-copy-value");
        const container = document.querySelector(target);
        if (container !== undefined && container !== null) {
          if (container.value !== undefined && container.value !== null) {
            value = container.value;
          } else {
            value = container.innerHTML;
          }
        }
        if (value !== null) {
          const elem = document.createElement("textarea");
          document.querySelector("body").appendChild(elem);
          elem.value = value;
          elem.select();
          document.execCommand("copy");
          elem.remove();
        }
        elem.setAttribute('data-bs-original-title', 'Copied!');
          let btn_tooltip = bootstrap.Tooltip.getInstance(elem);
          btn_tooltip.show();
          // reset the tooltip title
          elem.setAttribute('data-bs-original-title', 'Copy');
          setTimeout(() => {
              btn_tooltip.hide();
          }, 500)
      })
    });
  }
  /*------------Minus-plus--------------*/
  const plusBtns = document.querySelectorAll('.iq-quantity-plus')
  const minusBtns = document.querySelectorAll('.iq-quantity-minus')
  const updateQtyBtn = (elem, value) => {
    const oldValue = elem.closest('[data-qty="btn"]').querySelector('[data-qty="input"]').value
    const newValue = Number(oldValue) + Number(value)
    if (newValue >= 1) {
      elem.closest('[data-qty="btn"]').querySelector('[data-qty="input"]').value = newValue
    }
  }
  Array.from(plusBtns, (elem) => {
    elem.addEventListener('click', (e) => {
      updateQtyBtn(elem, 1)
    })
  })
  Array.from(minusBtns, (elem) => {
    elem.addEventListener('click', (e) => {
      updateQtyBtn(elem, -1)
    })
  })
  /*------------Flatpickr--------------*/
  const date_flatpickr = document.querySelectorAll('.date_flatpicker')
  Array.from(date_flatpickr, (elem) => {
    if (typeof flatpickr !== typeof undefined) {
      flatpickr(elem, {
        minDate: "today",
        dateFormat: "Y-m-d",
      })
    }
  })
  /*----------Range Flatpickr--------------*/
  const range_flatpicker = document.querySelectorAll('.range_flatpicker')
  Array.from(range_flatpicker, (elem) => {
    if (typeof flatpickr !== typeof undefined) {
      flatpickr(elem, {
        mode: "range",
        minDate: "today",
        dateFormat: "Y-m-d",
      })
    }
  })
  /*------------Wrap Flatpickr---------------*/
  const wrap_flatpicker = document.querySelectorAll('.wrap_flatpicker')
  Array.from(wrap_flatpicker, (elem) => {
    if (typeof flatpickr !== typeof undefined) {
      flatpickr(elem, {
        wrap: true,
        minDate: "today",
        dateFormat: "Y-m-d",
      })
    }
  })
  /*-------------Time Flatpickr---------------*/
  const time_flatpickr = document.querySelectorAll('.time_flatpicker')
  Array.from(time_flatpickr, (elem) => {
    if (typeof flatpickr !== typeof undefined) {
      flatpickr(elem, {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
      })
    }
  })
  /*-------------Inline Flatpickr-----------------*/
  const inline_flatpickr = document.querySelectorAll('.inline_flatpickr')
  Array.from(inline_flatpickr, (elem) => {
    if (typeof flatpickr !== typeof undefined) {
      flatpickr(elem, {
        inline: true,
        minDate: "today",
        dateFormat: "Y-m-d",
      })
    }
  })

  /*-------------CounterUp 2--------------*/
  if (window.counterUp !== undefined) {
    const counterUp = window.counterUp["default"];
    const counterUp2 = document.querySelectorAll('.counter')
    Array.from(counterUp2, (el) => {
      if (typeof Waypoint !== typeof undefined) {
        const waypoint = new Waypoint({
          element: el,
          handler: function () {
            counterUp(el, {
              duration: 1000,
              delay: 10,
            });
            this.destroy();
          },
          offset: "bottom-in-view",
        });
      }
    })
  }

  /*----------------SliderTab------------------*/
  Array.from(document.querySelectorAll('[data-toggle="slider-tab"]'), (elem) => {
    if (typeof SliderTab !== typeof undefined) {
      new SliderTab(elem)
    }
  })
  let Scrollbar
  if (typeof Scrollbar !== typeof null) {
    if (document.querySelectorAll(".data-scrollbar").length) {
      Scrollbar = window.Scrollbar
      Scrollbar.init(document.querySelector('.data-scrollbar'), {
        continuousScrolling: false,
      })
    }
  }
  /*-------------Data tables---------------*/
  if ($.fn.DataTable) {
    // Bootstrap DataTable
    if ($('[data-toggle="data-table"]').length) {
      $('[data-toggle="data-table"]').DataTable({
        "autoWidth": false,
        "dom": '<"row align-items-center"<"col-md-6" l><"col-md-6" f>><"table-responsive my-3" rt><"row align-items-center" <"col-md-6" i><"col-md-6" p>><"clear">',
      });
    }
    // Column hidden datatable
    if ($('[data-toggle="data-table-column-hidden"]').length) {
        var hiddentable= $('[data-toggle="data-table-column-hidden"]').DataTable({});
        $('a.toggle-vis').on('click', function (e) {
          e.preventDefault();
          const column = hiddentable.column($(this).attr('data-column'));
          column.visible(!column.visible());
        });
    }
    // Column filter datatable
    if ($('[data-toggle="data-table-column-filter"]').length) {
      $('[data-toggle="data-table-column-filter"] tfoot th').each(function () {
        const title = $(this).attr('title');
        $(this).html(`<td><input type="text" class="form-control form-control-sm" placeholder="${title}" /></td>`);
      });
      $('[data-toggle="data-table-column-filter"]').DataTable({
        initComplete: function () {
          this.api().columns().every(function () {
            var that = this;

            $('input', this.footer()).on('keyup change clear', function () {
              if (that.search() !== this.value) {
                that
                  .search(this.value)
                  .draw();
              }
            });
          });
        }
      });
    };
    // Multilanguage datatable
    if ($('[data-toggle="data-table-multi-language"]').length) {
      function languageSelect() {
        return Array.from(document.querySelector('#langSelector').options).filter(option => option.selected).map(option => option.getAttribute('data-path'))
      }
      function dataTableInit() {
        $('[data-toggle="data-table-multi-language"]').DataTable({
          "language": {
            "url": languageSelect()
          }
        });
      }
      dataTableInit()
      document.querySelector('#langSelector').addEventListener('change', (e) => {
        $('[data-toggle="data-table-multi-language"]').dataTable().fnDestroy();
        dataTableInit()
      })
    };
  };

  /*--------------Active Class for Pricing Table------------------------*/
  const tableTh = document.querySelectorAll('#my-table tr th')
  const tableTd = document.querySelectorAll('#my-table td')
  if (tableTh !== null) {
    Array.from(tableTh, (elem) => {
      elem.addEventListener('click', (e) => {
        Array.from(tableTh, (th) => {
          if (th.children.length) {
            th.children[0].classList.remove('active')
          }
        })
        elem.children[0].classList.add('active')
        Array.from(tableTd, (td) => td.classList.remove('active'))
        const col = Array.prototype.indexOf.call(document.querySelector('#my-table tr').children, elem);
        const tdIcons = document.querySelectorAll("#my-table tr td:nth-child(" + parseInt(col + 1) + ")");
        Array.from(tdIcons, (td) => td.classList.add('active'))
      })
    })
  }
  /*------------Resize Plugins--------------*/
  const resizePlugins = () => {
    // For sidebar-mini & responsive
    const tabs = document.querySelectorAll('.nav')
    if (window.innerWidth < 1025) {
      Array.from(tabs, (elem) => {
        if (!elem.classList.contains('flex-column') && elem.classList.contains('nav-tabs') && elem.classList.contains('nav-pills')) {
          elem.classList.add('flex-column', 'on-resize');
        }
      })
    } else {
      Array.from(tabs, (elem) => {
        if (elem.classList.contains('on-resize')) {
          elem.classList.remove('flex-column', 'on-resize');
        }
      })
    }
  }

  /*----------------Back To Top--------------------*/
  const backToTop = document.getElementById("back-to-top")
  if (backToTop !== null && backToTop !== undefined) {
    document.getElementById("back-to-top").classList.add("animate__animated", "animate__fadeOut")
    window.addEventListener('scroll', (e) => {
      if (document.documentElement.scrollTop > 250) {
        document.getElementById("back-to-top").classList.remove("animate__fadeOut")
        document.getElementById("back-to-top").classList.add("animate__fadeIn")
      } else {
        document.getElementById("back-to-top").classList.remove("animate__fadeIn")
        document.getElementById("back-to-top").classList.add("animate__fadeOut")
      }
    })
    // scroll body to 0px on click
    document.querySelector('#top').addEventListener('click', (e) => {
      e.preventDefault()
      window.scrollTo({ top: 0, behavior: 'smooth' });
    })
  }
  /*------------DOMContentLoaded--------------*/
  document.addEventListener('DOMContentLoaded', (event) => {
    resizePlugins()
    loaderInit()
  });
  /*------------Window Resize------------------*/
  window.addEventListener('resize', function (event) {
    resizePlugins()
  });
  /*--------DropDown--------*/

  function darken_screen(yesno) {
    if (yesno == true) {
      if (document.querySelector('.screen-darken') !== null) {
        document.querySelector('.screen-darken').classList.add('active');
      }
    }
    else if (yesno == false) {
      if (document.querySelector('.screen-darken') !== null) {
        document.querySelector('.screen-darken').classList.remove('active');
      }
    }
  }
  function close_offcanvas() {
    darken_screen(false);
    if (document.querySelector('.mobile-offcanvas.show') !== null) {
      document.querySelector('.mobile-offcanvas.show').classList.remove('show');
      document.body.classList.remove('offcanvas-active');
    }
  }
  function show_offcanvas(offcanvas_id) {
    darken_screen(true);
    if (document.getElementById(offcanvas_id) !== null) {
      document.getElementById(offcanvas_id).classList.add('show');
      document.body.classList.add('offcanvas-active');
    }
  }
  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('[data-trigger]').forEach(function (everyelement) {
      let offcanvas_id = everyelement.getAttribute('data-trigger');
      everyelement.addEventListener('click', function (e) {
        e.preventDefault();
        show_offcanvas(offcanvas_id);
      });
    });
    if (document.querySelectorAll('.btn-close')) {
      document.querySelectorAll('.btn-close').forEach(function (everybutton) {
        everybutton.addEventListener('click', function (e) {
          close_offcanvas();
        });
      });
    }
    if (document.querySelector('.screen-darken')) {
      document.querySelector('.screen-darken').addEventListener('click', function (event) {
        close_offcanvas();
      });
    }
  });
  if (document.querySelector('#navbarSideCollapse')) {
    document.querySelector('#navbarSideCollapse').addEventListener('click', function () {
      document.querySelector('.offcanvas-collapse').classList.toggle('open')
    })
  }
  /*---------------Form Validation--------------------*/
  // Example starter JavaScript for disabling form submissions if there are invalid fields
  window.addEventListener('load', function () {
    var forms = document.getElementsByClassName('needs-validation');
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var validation = Array.prototype.filter.call(forms, function (form) {
      // Loop over them and prevent submission
      form.addEventListener('submit', function (event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
