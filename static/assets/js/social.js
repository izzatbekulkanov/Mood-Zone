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

    //dashboard chart
    if (jQuery('#overall-chart').length) {
      const variableColors = IQUtils.getVariableColor();
      const colors = [variableColors.primary];
        const options = {
          series: [{
          name: 'Profiles',
          data: [40, 55, 25, 60, 30, 85, 60, 75, 57]
          }],
          colors: colors,
            chart: {
            height: 300,
            type: 'line',
            toolbar: {
              show: false
            },
          },
          forecastDataPoints: {
            count: 2,
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
            strokeColors: [variableColors.primary],
            strokeWidth: 2,
            strokeOpacity: 0.9,
            strokeDashArray: 0,
            fillOpacity: 0,
            shape: "circle",
            radius: 2,
            offsetX: 0,
            offsetY: 0,
          },
          xaxis: {
            categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
            tooltip: {
              enabled: false,
            }
          },
          yaxis: {
            tickAmount: 5,
            min: 0,
            max: 100,
          },
          responsive: [{
            breakpoint: 1399,
            options: {
              chart: {
                height:230
              },
              xaxis: {
                minHeight: 20,
                maxHeight: 20,
              }
            }
          }],
        };

        const chart = new ApexCharts(document.querySelector("#overall-chart"), options);
        chart.render();

        document.addEventListener('theme_color', (e) => {
          const variableColors = IQUtils.getVariableColor();
          const colors = [variableColors.primary, variableColors.info];

          const newOpt = {
            colors: colors,
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
    /*--------------Social Chart 3----------------*/
    if(document.querySelectorAll('#social-1').length){
      const variableColors = IQUtils.getVariableColor();
      const colors = [variableColors.info];
      const options = {
        chart: {
            height: 150,
            type: 'area',
            sparkline: {
                enabled: true
            },
            group: 'sparklines',

        },

        dataLabels: {
            enabled: false
        },
        stroke: {
            width: 3,
            curve: 'smooth'
        },
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.5,
                opacityTo: 0.3,
            }
        },

        series: [{
            name: 'series1',
            data: [10, 35, 20, 50, 70]
        }, ],
        colors: colors,

        xaxis: {
            type: 'datetime',
            categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
        },
        tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
            enabled:false,
        }

        };
        const chart = new ApexCharts(
            document.querySelector("#social-1"),
            options
        );
        chart.render();

        document.addEventListener('theme_color', (e) => {
          const variableColors = IQUtils.getVariableColor();
          const colors = [variableColors.info];

            const newOpt = {
              colors: colors,
              fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.5,
                    opacityTo: 0.3,
                }
            },
           }
            chart.updateOptions(newOpt)
        })

    }
    /*--------------Social Chart 3----------------*/
    if(document.querySelectorAll('#social-2').length){
      const variableColors = IQUtils.getVariableColor();
      const colors = [variableColors.primary];
        const options = {
        chart: {
            height: 150,
            type: 'area',
            sparkline: {
                enabled: true
            },
            group: 'sparklines',

        },
        dataLabels: {
            enabled: false
        },
        stroke: {
            width: 3,
            curve: 'smooth'
        },
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.5,
                opacityTo: 0.5,
            }
        },
        series: [{
            name: 'series1',
            data: [70, 50, 20, 35, 10]
        }, ],
        colors: colors,

        xaxis: {
            type: 'datetime',
            categories: ["2018-08-19T00:00:00", "2018-09-19T01:30:00", "2018-10-19T02:30:00", "2018-11-19T01:30:00", "2018-12-19T01:30:00"],
        },
        tooltip: {
            x: {
                format: 'dd/MM/yy HH:mm'
            },
            enabled: false,
        }
        };
        const chart = new ApexCharts(
            document.querySelector("#social-2"),
            options
        );

        chart.render();

        document.addEventListener('theme_color', (e) => {
          const variableColors = IQUtils.getVariableColor();
          const colors = [variableColors.primary];

            const newOpt = {
              colors: colors,
              fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    opacityFrom: 0.5,
                    opacityTo: 0.3,
                }
            },
           }
            chart.updateOptions(newOpt)
        })

    }

})(jQuery)
