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

------- Plugin Init --------

:: Product Slider
:: Charts
:: DataTable
:: Masonry

------------------------------------------------
Index Of Script
----------------------------------------------*/
"use strict";

/*---------------------------------------------------------------------
              Product Slider
-----------------------------------------------------------------------*/

if (document.querySelectorAll('.blog-data-slider').length > 0) {
    const options = {
        centeredSlides: false,
        loop: false,
        slidesPerView: 4,
        autoplay:false,
        spaceBetween: 32,
        breakpoints: {
            320: { slidesPerView: 1 },
            550: { slidesPerView: 1 },
            991: { slidesPerView: 1 },
            1400: { slidesPerView: 1 },
            1500: { slidesPerView: 1 },
            1920: { slidesPerView: 1 },
            2040: { slidesPerView: 1 },
            2440: { slidesPerView: 1 }
        },
        pagination: {
            el: '.swiper-pagination'
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        },

        // And if we need scrollbar
        scrollbar: {
            el: '.swiper-scrollbar'
        }
    }

    let swiper = new Swiper('.blog-data-slider',options);

    document.addEventListener('theme_scheme_direction', (e) => {
      swiper.destroy(true, true)
      setTimeout(() => {
          swiper = new Swiper('.blog-data-slider',options);
      }, 500);
    })
}

if (document.querySelectorAll('.upcoming-blog-slider').length > 0) {
    const options = {
        centeredSlides: false,
        loop: false,
        slidesPerView: 3,
        autoplay:false,
        spaceBetween: 32,
        breakpoints: {
            320: { slidesPerView: 1 },
            550: { slidesPerView: 1 },
            991: { slidesPerView: 2 },
            1400: { slidesPerView: 2 },
            1500: { slidesPerView: 2 },
            1920: { slidesPerView: 3 },
            2040: { slidesPerView: 3 },
            2440: { slidesPerView: 3 }
        },
        pagination: {
            el: '.swiper-pagination'
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        },

        // And if we need scrollbar
        scrollbar: {
            el: '.swiper-scrollbar'
        }
    }
    let swiper = new Swiper('.upcoming-blog-slider',options);

    document.addEventListener('theme_scheme_direction', (e) => {
      swiper.destroy(true, true)
      setTimeout(() => {
          swiper = new Swiper('.upcoming-blog-slider',options);
      }, 500);
    })
}

if (document.querySelectorAll('.blog-analysis-slider').length > 0) {
    const options = {
        centeredSlides: false,
        loop: false,
        slidesPerView: 2,
        autoplay:false,
        spaceBetween: 32,
        breakpoints: {
            320: { slidesPerView: 1 },
            550: { slidesPerView: 2 },
            991: { slidesPerView: 2 },
            1400: { slidesPerView: 2 },
            1500: { slidesPerView: 2 },
            1920: { slidesPerView: 2 },
            2040: { slidesPerView: 2 },
            2440: { slidesPerView: 2 }
        },
        pagination: {
            el: '.swiper-pagination'
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        },

        // And if we need scrollbar
        scrollbar: {
            el: '.swiper-scrollbar'
        }
    }
    let swiper = new Swiper('.blog-analysis-slider',options);

    document.addEventListener('theme_scheme_direction', (e) => {
      swiper.destroy(true, true)
      setTimeout(() => {
          swiper = new Swiper('.blog-analysis-slider',options);
      }, 500);
    })
}

/*---------------------------------------------------------------------
              Charts
-----------------------------------------------------------------------*/

if (document.querySelectorAll('#activity-chart').length) {
  const variableColors = IQUtils.getVariableColor();
  const colors = [variableColors.primary, variableColors.info];
  const options = {
    series: [{
    // name: 'PRODUCT A',
    data: [20, 70, 35, 24, 60, 50, 20]
    },
    {
    // name: 'PRODUCT B',
    data: [60, 20, 70, 80, 20, 43, 30]
  }],
    chart: {
    type: 'bar',
    height: 350,
    stacked: true,
    toolbar: {
      show: false
    },
    zoom: {
      enabled: true
    }
  },
  yaxis: {
    show: true,
    tickAmount: 6,
    min: 0,
    max: 120
  },
  xaxis:{
    categories: ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
  },
  legend: {
    show: false,
  },
  grid: {
    show: true,
    strokeDashArray: 7,
  },
  colors: colors,
  plotOptions: {
    bar: {
      horizontal: false,
      borderRadius: 4,
      columnWidth: '18%'
    },
  },
  dataLabels: {
    enabled: false,
  }

  };

  const chart = new ApexCharts(document.querySelector("#activity-chart"), options);
  chart.render();

  //color customizer
  document.addEventListener('theme_color', (e) => {
    const variableColors = IQUtils.getVariableColor();
    const colors = [variableColors.primary, variableColors.info];

    const newOpt = {
      colors: colors,
      markers: {
        strokeColors: colors,
      },
      fill: {
        type: 'gradient',
        gradient: {
            shade: 'dark',
            type: "vertical",
            gradientToColors: colors, // optional, if not defined - uses the shades of same color in series
            opacityFrom: 1,
            opacityTo: 1,
            colors: colors,
        }
      },
   }
    chart.updateOptions(newOpt)
  })
  document.addEventListener('body_font_family',(e) =>{
    let prefix = getComputedStyle(document.body).getPropertyValue('--prefix') || 'bs-';
    if (prefix) {
        prefix = prefix.trim()
    }
    const font_1 = getComputedStyle(document.body).getPropertyValue(`--${prefix}body-font-family`);
    const fonts = [font_1.trim()];
    const newOpt = {
        chart: {
            fontFamily: fonts,
        }
}
chart.updateOptions(newOpt)
})
}

if (document.querySelectorAll('#blog-visitor').length) {
  const variableColors = IQUtils.getVariableColor();
  const colors = [variableColors.primary];
  const options = {
    chart: {
      height: 185,
      type: "radialBar"
    },
    series: [72.5],
    colors: colors,
    plotOptions: {
      radialBar: {
        hollow: {
          margin: 15,
          size: "60%"
        },
        dataLabels: {
          showOn: "always",
          name: {
            show: false,
          },
          value: {
            fontSize: "24px",
            show: true,
            formatter: function (val) {
              return '+'+val + '%'
            }
          }
        }
      }
    },

    stroke: {
      lineCap: "smooth",
    },
  };

  const chart = new ApexCharts(document.querySelector("#blog-visitor"), options);
  chart.render();

  document.addEventListener('theme_color', (e) => {
    const variableColors = IQUtils.getVariableColor();
  const colors = [variableColors.primary];

    const newOpt = {
      colors: colors
   }
    chart.updateOptions(newOpt)
  })
}

if (document.querySelectorAll('#blog-view-chart').length) {
  const variableColors = IQUtils.getVariableColor();
  const colors = [variableColors.primary, variableColors.warning, variableColors.info];
  const options = {
    series: [65, 70, 78],
    chart: {
    height: 185,
    type: 'radialBar',
  },
  colors: colors,
  plotOptions: {
    radialBar: {
      dataLabels: {
        name: {
          fontSize: '13px',
          show: true
        },
        value: {
          fontSize: '16px',
          show: true
        },
      },
      hollow: {
        size: '25%',
      },
      track: {
        margin: 8,
        strokeWidth: '70%',
      }
    }
  },
  labels: ['Info Blogs', 'Food Blogs','Lifestyle Blogs'],
  };

  const chart = new ApexCharts(document.querySelector("#blog-view-chart"), options);
  chart.render();

  document.addEventListener('theme_color', (e) => {
    const variableColors = IQUtils.getVariableColor();
  const colors = [variableColors.primary, variableColors.warning, variableColors.info];

    const newOpt = {
      colors: colors,
      fill: {
        type: 'gradient',
        gradient: {
            shade: 'dark',
            type: "vertical",
            gradientToColors: colors, // optional, if not defined - uses the shades of same color in series
            opacityFrom: 1,
            opacityTo: 1,
            colors: colors,
        }
      },
   }
    chart.updateOptions(newOpt)
  })

  document.addEventListener('body_font_family',(e) =>{
    let prefix = getComputedStyle(document.body).getPropertyValue('--prefix') || 'bs-';
    if (prefix) {
        prefix = prefix.trim()
    }
    const font_1 = getComputedStyle(document.body).getPropertyValue(`--${prefix}body-font-family`);
    const fonts = [font_1.trim()];
    const newOpt = {
        chart: {
            fontFamily: fonts,
        }
}
chart.updateOptions(newOpt)
})
}

if (document.querySelectorAll("#growthChart").length) {
  const variableColors = IQUtils.getVariableColor();
  const colors = [variableColors.primary, variableColors.info];
  const options = {
    series: [{
      name: "Desktops",
      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
      },
      {
        name: "Mobile",
        data: [10, 82, 75, 68, 47, 60, 49, 91, 108]
    }],
    chart: {
      height: 350,
      type: 'line',
      zoom: {
        enabled: false
      },
      animations: {
        enabled: true,
        easing: 'easeinout',
        speed: 800,
        dynamicAnimation: {
          enabled: true,
          speed: 400
        }
      },
      toolbar: {
        show: false
      },
    },
    colors: colors,
    dataLabels: {
      enabled: false
    },
    stroke: {
      width: 3,
    },
    grid: {
      show:true,
      strokeDashArray: 7,
    },
    markers: {
      size: 6,
      colors:  '#FFFFFF',
      strokeColors: colors,
      strokeWidth: 2,
      strokeOpacity: 0.9,
      strokeDashArray: 0,
      fillOpacity: 0,
      shape: "circle",
      radius: 2,
      offsetX: 0,
      offsetY: 0,
    },
    grid: {
      show:true,
      strokeDashArray: 3,
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    legend: {
      show: false,
    }
  };

  const chart = new ApexCharts(document.querySelector("#growthChart"), options);
  chart.render();

  //chart update onclick
  $('[data-chart="update"]').on('click', function() {
    const type = $(this).attr('data-type')
    let searies = []
    switch (type) {
        case 'blog-chart-fall':
          searies= [{
            name: "Desktops",
            data: [20, 51, 65, 21, 39, 42, 62, 51, 18]
            },
            {
              name: "Mobile",
              data: [80, 62, 55, 58, 87, 50, 49, 41, 16]
          }]
        break;
        default:
          searies = [{
            name: "Desktops",
            data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
            },
            {
              name: "Mobile",
              data: [10, 82, 75, 68, 47, 60, 49, 91, 108]
          }]
        break;
    }
    chart.updateSeries(searies)
  })

  //color customizer
  document.addEventListener('theme_color', (e) => {
    const variableColors = IQUtils.getVariableColor();
    const colors = [variableColors.primary, variableColors.info];

    const newOpt = {
      colors: colors,
      markers: {
        strokeColors: colors,
      }
  }
    chart.updateOptions(newOpt)
  })
}

/*---------------------------------------------------------------------
              DataTable
-----------------------------------------------------------------------*/

if (document.querySelectorAll('[data-table="blog-comment"]').length) {
  $('[data-table="blog-comment"]').DataTable();
};

if (document.querySelectorAll('[data-toggle="blog_admin"]').length) {
  $('[data-toggle="blog_admin"] tfoot th').each(function () {
    const title = $(this).attr('title');
    $(this).html(`<td><input type="text" class="form-control form-control-sm" placeholder="${title}" /></td>`);
  });
  $('[data-toggle="blog_admin"]').DataTable({
      pageLength: 5,
      lengthMenu: [5, 10, 20, 50, 100],
      initComplete: function () {
          this.api().columns().every(function () {
              const that = this;
              $('input', this.footer()).on('keyup change clear', function () {
                  if (that.search() !== this.value) {
                      that.search(this.value).draw();
                  }
              });
          });
      }
  });
};

/*---------------------------------------------------------------------
              Masonry
-----------------------------------------------------------------------*/

if(document.querySelector('[data-toggle="masonry"]')){
  setTimeout(() => {
    const elem = document.querySelector('[data-toggle="masonry"]');
    new Masonry( elem, {
        itemSelector: '.col-lg-4',
    });
  }, 100)
}
