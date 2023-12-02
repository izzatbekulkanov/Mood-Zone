/*
* Version: 1.0.0
* Template: Hope-Ui Pro - Responsive Bootstrap 5 Admin Dashboard Template
* Author: iqonic.design
* Design and Developed by: iqonic.design
* NOTE: This file contains the script for initialize & listener Template.
*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

------- Plugin Init --------

:: Chart

------------------------------------------------
Index Of Script
----------------------------------------------*/

(function (jQuery) {
  "use strict";
  if (document.querySelectorAll('#appointment-line-chart').length) {
    const variableColors = IQUtils.getVariableColor();
    const colors = [variableColors.primary, variableColors.info];
    const options = {
      series: [
        {
          name: 'Booked',
          data: [7, 4, 9, 4, 7, 3, 8]
        },
        {
          name: 'Cancelled',
          data: [3, 5, 3, 7, 4, 6, 9]
        }],
      colors: colors,
      chart: {
        height: 350,
        type: 'line',
        zoom: {
          enabled: false
        },
        toolbar: {
          show: false
        },
      },
      dataLabels: {
        enabled: false
      },
      legend: {
        show:false,
      },
      stroke: {
        show: true,
        curve: 'smooth',
        lineCap: 'butt',
        width: 3,
        dashArray: 0,
      },
      grid: {
        show: true,
        strokeDashArray: 3,
    },
      xaxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July'],
        axisBorder: {
          show: false,

      },
      axisTicks: {
          show: false,

      },
      },
    };

    const chart = new ApexCharts(document.querySelector("#appointment-line-chart"), options);
    chart.render();

    document.addEventListener('theme_color', (e) => {
      const variableColors = IQUtils.getVariableColor();
      const colors = [variableColors.primary, variableColors.info];

      const newOpt = {
        colors: colors
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

  //radial chart
  if(document.querySelectorAll("#appointment-booking").length){
    const variableColors = IQUtils.getVariableColor();
    const colors = [variableColors.primary, variableColors.info];
    const options = {
        series: [40,15],
        chart: {
        height:180,
        type: 'donut',
      },
      labels: ["Dentist", "Surgeon"],
      colors: colors,
      plotOptions: {
        pie: {
          startAngle: -90,
          endAngle: 270,
          donut:{
            size: '70%',
            labels:{
              show:true,
              total:{
                show:true,
                color: '#BCC1C8',
                fontSize: '18px',
                fontFamily: 'Inter',
                fontWeight: 600,
              },
              value: {
                show: true,
                fontSize: '25px',
                fontFamily: 'Inter',
                fontWeight: 700,
                color: '#8F9FBC',
              },
            }
          }
        }
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        lineCap: 'round'
      },
      grid:{
        padding: {
          bottom: 0,
        }
      },
      legend: {
        position: 'bottom',
        offsetY: 8,
        show:false,
      },
      responsive: [{
        breakpoint: 480,
        options: {
          chart: {
            height:268
          }
        }
      }]
    };

    const chart = new ApexCharts(document.querySelector("#appointment-booking"), options);
    chart.render();

    document.addEventListener('theme_color', (e) => {
      let prefix = getComputedStyle(document.body).getPropertyValue('--prefix') || 'bs-';
      if (prefix) {
        prefix = prefix.trim()
      }
      const color1 = getComputedStyle(document.body).getPropertyValue(`--${prefix}primary`);
      const color2 = getComputedStyle(document.body).getPropertyValue(`--${prefix}info`);
      const colors = [color1.trim(), color2.trim()];

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

  if (document.querySelectorAll('[data-toggle="doctor_visit"]').length) {
    $('[data-toggle="doctor_visit"] tfoot th').each(function () {
      const title = $(this).attr('title');
      if(title !== undefined) {
        $(this).html(`<td><input type="text" class="form-control form-control-sm" placeholder="${title}" /></td>`);
      }
    });
    $('[data-toggle="doctor_visit"]').DataTable({
        pageLength: 5,
        lengthMenu: [5, 10, 20, 50, 100],
        columnDefs: [{
          'searchable'    : true,
          'targets'       : [0,1, 2, 3],
        }],
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

})(jQuery)
