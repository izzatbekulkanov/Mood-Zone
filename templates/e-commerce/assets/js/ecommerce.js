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

:: 360 Product
:: Product Slider
:: Charts
:: Checkout
:: Horizontal Slider
:: Vertical Slider
:: Column Filter Datatable

------------------------------------------------
Index Of Script
----------------------------------------------*/

(function () {
    "use strict";

    /*---------------------------------------------------------------------
                  360 Product
    -----------------------------------------------------------------------*/

    const event360Modal = document.getElementById('product-viewer360')
    if(event360Modal !== null){
        event360Modal.addEventListener('shown.bs.modal', function () {
            const cloudImg360 = document.querySelector('.cloudimage-360')
            if(!cloudImg360.classList.contains('initialized')){
                window.CI360.init();
            }
        })
    }

    /*---------------------------------------------------------------------
              Product Slider
    -----------------------------------------------------------------------*/

    if ($('#collection-slider').length > 0) {
        const options = {
            centeredSlides: false,
            loop: true,
            slidesPerView: 1,
            autoplay:true,
            spaceBetween: 8,
            breakpoints: {
                320: { slidesPerView: 1 },
                550: { slidesPerView: 1 },
                991: { slidesPerView: 1 },
                1400: { slidesPerView: 1 },
                1500: { slidesPerView: 1 }
            },
        }
        let swiper = new Swiper('#collection-slider',options);
        document.addEventListener('theme_scheme_direction', (e) => {
          swiper.destroy(true, true)
          setTimeout(() => {
              swiper = new Swiper('#collection-slider',options);
          }, 500);
        })
    }
    if ($('#ecommerce-slider').length > 0) {
        const options = {
            centeredSlides: false,
            loop: false,
            slidesPerView: 4,
            autoplay:false,
            spaceBetween: 32,
            breakpoints: {
                320: { slidesPerView: 1 },
                550: { slidesPerView: 2 },
                991: { slidesPerView: 3 },
                1400: { slidesPerView: 3 },
                1500: { slidesPerView: 3 },
                1920: { slidesPerView: 4 },
                2040: { slidesPerView: 4 },
                2440: { slidesPerView: 4 }
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
        let swiper = new Swiper('#ecommerce-slider',options);

        document.addEventListener('theme_scheme_direction', (e) => {
          swiper.destroy(true, true)
          setTimeout(() => {
              swiper = new Swiper('#ecommerce-slider',options);
          }, 500);
        })
    }

/*---------------------------------------------------------------------
              Charts
-----------------------------------------------------------------------*/

    if (document.querySelectorAll('#admin-chart-01').length) {
      const variableColors = IQUtils.getVariableColor();
      const colors = [variableColors.primary];
        const options = {
            series: [{
                name: 'total',
                data: [30, 60, 20,60,25, 80, 40, 94,80,85,70]
            }],
            chart: {
                fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
                height: '100%',
                type: 'area',
                toolbar: {
                    show: false
                },
                sparkline: {
                    enabled: false,
                },
            },
            colors: colors,
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth',
                width: 3,
            },
            yaxis: {
              show: true,
                labels: {
                    show: true,
                    minWidth: 19,
                    maxWidth: 19,
                    style: {
                    colors: "#8A92A6",
                    },
                    offsetX: -5,
                },
                axisBorder: {
                    show: false,
                },
            },
            legend: {
                show: false,
            },
            xaxis: {
                labels: {
                    minHeight:22,
                    maxHeight:22,
                    show: true,
                    style: {
                      colors: "#8A92A6",
                    },
                },
                lines: {
                    show: false  //or just here to disable only x axis grids
                },
                axisTicks: {
                    show: false,

                },
                axisBorder: {
                    show: false,
                },
                categories: ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug","Sep","Oct","Nov","Dec"]
            },
            grid: {
                show: true,
                strokeDashArray: 3,
            },
            responsive: [{
              breakpoint: 1399,
              options: {
                chart: {
                  height:320
                }
              }
            }],
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'dark',
                    type: "vertical",
                    shadeIntensity: 0,
                    gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                    inverseColors: true,
                    opacityFrom: .4,
                    opacityTo: .1,
                    stops: [0, 50, 80],
                    colors: ["#3a57e8"]
                }
            },
            tooltip: {
              enabled: true,
            },
        };

        const chart = new ApexCharts(document.querySelector("#admin-chart-01"), options);
        chart.render();
        document.addEventListener('theme_color', (e) => {
          const variableColors = IQUtils.getVariableColor();
          const colors = [variableColors.primary, variableColors.info];

            const newOpt = {
              colors: colors,
              fill: {
                type: 'gradient',
                gradient: {
                    shade: 'dark',
                    type: "vertical",
                    shadeIntensity: 0,
                    gradientToColors: colors, // optional, if not defined - uses the shades of same color in series
                    inverseColors: true,
                    opacityFrom: .4,
                    opacityTo: .1,
                    stops: [0, 50, 60],
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
    if (document.querySelectorAll('#admin-chart-02').length) {
        const options = {
            series: [{
                name: 'total',
                data: [30, 50, 20,60,25, 80, 40]
            }],
            chart: {
                fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
                height: 155,
                type: 'area',
                toolbar: {
                    show: false
                },
                sparkline: {
                    enabled: true,
                },
                toolbar: {
                  show: false
                },
            },
            colors: ["#ffffff"],
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth',
                width: 4,
            },
            yaxis: {
              show: false,
            },
            legend: {
                show: false,
            },
            xaxis: {
                labels: {
                    minHeight:22,
                    maxHeight:22,
                    show: true,
                    style: {
                      colors: "#ffffff",
                    },
                },
                lines: {
                    show: false
                },
                categories: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
            },
            responsive: [{
              breakpoint: 1399,
              options: {
                chart: {
                  height:140
                }
              }
            }],
            grid: {
                show: false,
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'dark',
                    type: "vertical",
                    shadeIntensity: 0,
                    gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                    inverseColors: true,
                    opacityFrom: .4,
                    opacityTo: .1,
                    stops: [0, 50, 80],
                    colors: ["#3a57e8"]
                }
            },
            tooltip: {
              enabled: false,
            },
        };

        const chart = new ApexCharts(document.querySelector("#admin-chart-02"), options);
        chart.render();

    }
    if (document.querySelectorAll('#admin-chart-03').length) {
    const options = {
        series: [{
            name: 'total',
            data: [30, 50, 20,60,25, 80, 40]
        }],
        chart: {
            fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
            height: 155,
            type: 'area',
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: false,
            },
            sparkline: {
                enabled: true,
            },
        },
        colors: ["#ffffff"],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 3,
        },
        yaxis: {
            show: false,
        },
        legend: {
            show: false,
        },
        responsive: [{
            breakpoint: 1399,
            options: {
            chart: {
                height:140
            }
            }
        }],
        xaxis: {
            labels: {
                minHeight:22,
                maxHeight:22,
                show: true,
                style: {
                    colors: "#ffffff",
                },
            },
            lines: {
                show: false  //or just here to disable only x axis grids
            },
            categories: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        },

        grid: {
            show: false,
        },

        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: "vertical",
                shadeIntensity: 0,
                gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                inverseColors: true,
                opacityFrom: .4,
                opacityTo: .1,
                stops: [0, 50, 80],
                colors: ["#3a57e8"]
            }
        },
        tooltip: {
            enabled: false,
        },
    };

    const chart = new ApexCharts(document.querySelector("#admin-chart-03"), options);
    chart.render();
    }
    if (document.querySelectorAll('#admin-chart-04').length) {
      const variableColors = IQUtils.getVariableColor();
      const colors = [variableColors.primary, variableColors.info];
        const options = {
            series: [44, 55],
            chart: {
                height: 185,
                type: 'radialBar',
            },
        colors: colors,
        plotOptions: {
            radialBar: {
                inverseOrder: false,
                endAngle: 360,
                hollow: {
                    margin: 5,
                    size: '50%',
                    background: 'transparent',
                    imageWidth: 150,
                    imageHeight: 150,
                    imageClipped: true,
                    position: 'front',
                    dropShadow: {
                      enabled: false,
                      blur: 3,
                      opacity: 0.5
                    }
                },
                track: {
                    show: true,
                    background: '#f2f2f2',
                    strokeWidth: '70%',
                    opacity: 1,
                    margin: 6,
                    dropShadow: {
                        enabled: false,
                        blur: 3,
                        opacity: 0.5
                    }
                },
                dataLabels: {
                    show: true,
                    name: {
                        show: true,
                        fontSize: '16px',
                        fontWeight: 600,
                        offsetY: -10
                      },
                      value: {
                        show: true,
                        fontSize: '14px',
                        fontWeight: 400,
                        offsetY: 16,
                        formatter: function (val) {
                          return val + '%'
                        }
                    },
                }
            }
        },
        labels: ['Electronics', 'Accessories'],
        };

        const chart = new ApexCharts(document.querySelector("#admin-chart-04"), options);
        chart.render();
        document.addEventListener('theme_color', (e) => {
          const variableColors = IQUtils.getVariableColor();
          const colors = [variableColors.primary, variableColors.info];

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
    if (document.querySelectorAll('#admin-chart-05').length) {
        const variableColors = IQUtils.getVariableColor();
        const colors = [variableColors.primary, variableColors.info];
        const options = {
            series: [{
                name: 'total',
                data: [95, 80, 90,30,55, 70, 40, 54,44,20]
            }],
            chart: {
                fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
                height: 400,
                type: 'area',
                toolbar: {
                    show: false
                },
                sparkline: {
                    enabled: false,
                },
            },
            colors: colors,
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'smooth',
                width: 3,
            },
            yaxis: {
              show: true,
              labels: {
                show: true,
                minWidth: 19,
                maxWidth: 19,
                style: {
                  colors: "#8A92A6",
                },
                offsetX: -5,
              },
            },
            legend: {
                show: true,
            },
            xaxis: {
                labels: {
                    minHeight:22,
                    maxHeight:22,
                    show: true,
                    style: {
                      colors: "#8A92A6",
                    },
                },
                lines: {
                    show: false  //or just here to disable only x axis grids
                },
                categories: ["Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug","Sep","Oct","Nov","Dec"],

                axisBorder: {
                    show: false,

                },
                axisTicks: {
                    show: false,

                },
            },
            grid: {
                show: true,
                strokeDashArray: 3,
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shade: 'dark',
                    type: "vertical",
                    shadeIntensity: 0,
                    gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                    inverseColors: true,
                    opacityFrom: .4,
                    opacityTo: .1,
                    stops: [0, 50, 80],
                    colors: ["#3a57e8"]
                }
            },
            tooltip: {
              enabled: false,
            },
        };

        const chart = new ApexCharts(document.querySelector("#admin-chart-05"), options);
        chart.render();
        document.addEventListener('theme_color', (e) => {
          const variableColors = IQUtils.getVariableColor();
          const colors = [variableColors.primary];

            const newOpt = {
              colors: colors,
              fill: {
                type: 'gradient',
                gradient: {
                    gradientToColors: colors, // optional, if not defined - uses the shades of same color in series
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
    if (document.querySelectorAll('#admin-chart-06').length) {
    const options = {
        series: [{
            name: 'total',
            data: [30, 60, 20,60,25, 80, 40]
        }],
        chart: {
            fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
            height: 145,
            type: 'area',
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: true,
            },
            toolbar: {
                show: false
            },
        },
        colors: ["#ffffff"],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 3,
        },
        yaxis: {
            show: false,
        },
        legend: {
            show: false,
        },
        xaxis: {
            labels: {
                minHeight:22,
                maxHeight:22,
                show: true,
                style: {
                    colors: "#ffffff",
                },
            },
            lines: {
                show: false
            },
            categories: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        },
        grid: {
            show: false,
        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: "vertical",
                shadeIntensity: 0,
                gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                inverseColors: true,
                opacityFrom: .4,
                opacityTo: .1,
                stops: [0, 50, 80],
                colors: ["#ffffff"]
            }
        },
        tooltip: {
            enabled: false,
        },
    };

    const chart = new ApexCharts(document.querySelector("#admin-chart-06"), options);
    chart.render();
    }
    if (document.querySelectorAll('#admin-chart-07').length) {
    const options = {
        series: [{
            name: 'total',
            data: [30, 60, 20,60,25, 80, 40]
        }],
        chart: {
            fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
            height: 145,
            type: 'area',
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: true,
            },
            toolbar: {
                show: false
            },
        },
        colors: ["#ffffff"],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 3,
        },
        yaxis: {
            show: false,
        },
        legend: {
            show: false,
        },
        xaxis: {
            labels: {
                minHeight:22,
                maxHeight:22,
                show: true,
                style: {
                    colors: "#ffffff",
                },
            },
            lines: {
                show: false
            },
            categories: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        },
        grid: {
            show: false,
        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: "vertical",
                shadeIntensity: 0,
                gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                inverseColors: true,
                opacityFrom: .4,
                opacityTo: .1,
                stops: [0, 50, 80],
                colors: ["#ffffff"]
            }
        },
        tooltip: {
            enabled: false,
        },
    };

    const chart = new ApexCharts(document.querySelector("#admin-chart-07"), options);
    chart.render();
    }
    if (document.querySelectorAll('#admin-chart-08').length) {
    const options = {
        series: [{
            name: 'total',
            data: [30, 60, 20,60,25, 80, 40]
        }],
        chart: {
            fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
            height: 145,
            type: 'area',
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: true,
            },
            toolbar: {
                show: false
            },
        },
        colors: ["#ffffff"],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 3,
        },
        yaxis: {
            show: false,
        },
        legend: {
            show: false,
        },
        xaxis: {
            labels: {
                minHeight:22,
                maxHeight:22,
                show: true,
                style: {
                    colors: "#ffffff",
                },
            },
            lines: {
                show: false
            },
            categories: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        },
        grid: {
            show: false,
        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: "vertical",
                shadeIntensity: 0,
                gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                inverseColors: true,
                opacityFrom: .4,
                opacityTo: .1,
                stops: [0, 50, 80],
                colors: ["#ffffff"]
            }
        },
        tooltip: {
            enabled: false,
        },
    };

    const chart = new ApexCharts(document.querySelector("#admin-chart-08"), options);
    chart.render();
    }
    if (document.querySelectorAll('#admin-chart-09').length) {
    const options = {
        series: [{
            name: 'total',
            data: [30, 60, 20,60,25, 80, 40]
        }],
        chart: {
            fontFamily: '"Inter", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
            height: 145,
            type: 'area',
            toolbar: {
                show: false
            },
            sparkline: {
                enabled: true,
            },
            toolbar: {
                show: false
            },
        },
        colors: ["#ffffff"],
        dataLabels: {
            enabled: false
        },
        stroke: {
            curve: 'smooth',
            width: 3,
        },
        yaxis: {
            show: false,
        },
        legend: {
            show: false,
        },
        xaxis: {
            labels: {
                minHeight:22,
                maxHeight:22,
                show: true,
                style: {
                    colors: "#ffffff",
                },
            },
            lines: {
                show: false
            },
            categories: ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        },
        grid: {
            show: false,
        },
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'dark',
                type: "vertical",
                shadeIntensity: 0,
                gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
                inverseColors: true,
                opacityFrom: .4,
                opacityTo: .1,
                stops: [0, 50, 80],
                colors: ["#ffffff"]
            }
        },
        tooltip: {
            enabled: false,
        },
    };

    const chart = new ApexCharts(document.querySelector("#admin-chart-09"), options);
    chart.render();
    }

/*---------------------------------------------------------------------
    Checkout
-----------------------------------------------------------------------*/

    jQuery(document).ready(function(){
        jQuery('#backbutton').click(function(){
            jQuery('#checkout').removeClass('show');
            jQuery('#cart').addClass('show');
            jQuery('#iq-tracker-position-2').removeClass('active');
            jQuery('#iq-tracker-position-1').addClass('active');
        });
        jQuery('#place-order').click(function(){
            jQuery('#cart').removeClass('show');
            jQuery('#checkout').addClass('show');
            jQuery('#iq-tracker-position-1').removeClass('active');
            jQuery('#iq-tracker-position-1').addClass('done');
            jQuery('#iq-tracker-position-2').addClass('active');
        });
        jQuery('#deliver-address').click(function(){
            jQuery('#checkout').removeClass('show');
            jQuery('#payment').addClass('show');
            jQuery('#iq-tracker-position-2').removeClass('active');
            jQuery('#iq-tracker-position-2').addClass('done');
            jQuery('#iq-tracker-position-3').addClass('active');
        });
    });

/*---------------------------------------------------------------------
    Horizontal Slider
-----------------------------------------------------------------------*/

    if(document.querySelectorAll('.gallery-top').length && document.querySelectorAll('.gallery-thumbs').length){
        const galleryTopOptions = {
            spaceBetween: 10,
            loop: true,
            loopedSlides: 3,
            mousewheel: true,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev'
            }
        };
        const galleryThumbsOptions = {
            spaceBetween: 10,
            centeredSlides: true,
            slidesPerView: 'auto',
            touchRatio: 0.2,
            slideToClickedSlide: true,
            loop: true,
            loopedSlides: 3,
        };
        let galleryTop = new Swiper('.gallery-top', galleryTopOptions);
        let galleryThumbs = new Swiper('.gallery-thumbs', galleryThumbsOptions);
        galleryTop.controller.control = galleryThumbs;
        galleryThumbs.controller.control = galleryTop;

        document.addEventListener('theme_scheme_direction', (e) => {
            galleryTop.destroy(true, true)
            setTimeout(() => {
                galleryTop = new Swiper('.gallery-top', galleryTopOptions);
                galleryThumbs = new Swiper('.gallery-thumbs', galleryThumbsOptions);
                galleryTop.controller.control = galleryThumbs;
                galleryThumbs.controller.control = galleryTop;
            }, 500);
        })

    }

/*---------------------------------------------------------------------
    Vertical Slider
-----------------------------------------------------------------------*/

    if(document.querySelectorAll('.slider__thumbs .swiper-container').length) {
        const sliderThumbsOptions = {
            direction: 'vertical',
            slidesPerView: 3,
            spaceBetween: 24,
            slideToClickedSlide: true,
            loop: true,
            loopedSlides: 5,
            navigation: {
                nextEl: '.slider__next',
                prevEl: '.slider__prev'
            },
            breakpoints: {
                0: {
                    direction: 'horizontal',
                    slidesPerView: 3,
                },
                768: {
                    direction: 'vertical',
                }
            }
        }
        const sliderImagesOptions = {
            direction: 'vertical',
            slidesPerView: 1,
            spaceBetween: 32,
            loop: true,
            loopedSlides: 5,
            mousewheel: true,
            navigation: {
                nextEl: '.slider__next',
                prevEl: '.slider__prev'
            },
            grabCursor: true,
            breakpoints: {
                0: {
                    direction: 'horizontal',

                },
                768: {
                    direction: 'vertical',
                }
            }
        }
        let sliderThumbs = new Swiper('.slider__thumbs .swiper-container', sliderThumbsOptions);
        let sliderImages = new Swiper('.slider__images .swiper-container', sliderImagesOptions);
        sliderThumbs.controller.control = sliderImages;
        sliderImages.controller.control = sliderThumbs;
        document.addEventListener('theme_scheme_direction', (e) => {
          sliderImages.destroy(true, true)
            setTimeout(() => {
              sliderThumbs = new Swiper('.slider__thumbs .swiper-container', sliderThumbsOptions);
              sliderImages = new Swiper('.slider__images .swiper-container', sliderImagesOptions);
              sliderThumbs.controller.control = sliderImages;
              sliderImages.controller.control = sliderThumbs;
            }, 500);
        })
    }

    const valuesNode = [
        document.getElementById('lower-value'), // 0
        document.getElementById('upper-value')  // 1
    ];
    window.addEventListener('load', function() {
        if(window['product-price-range']) {
            window['product-price-range'].on('update', function (values, handle, unencoded, isTap, positions) {
                valuesNode[handle].innerHTML = '$' + Number(values[handle]).toFixed(0);
            });
        }
        const pageType = IQUtils.getQueryString('type')
        switch (pageType) {
            case 'product-grid':
                $('.breadcrumb-title small').text('Product Grid View');
                $('.sidebar .product-grid').addClass('active').parent().addClass('active')
                $('.sidebar .product-grid').closest('.collapse').addClass('show').prev().attr('aria-expanded', true).parent().addClass('active')
                $('#grid-view-tab').tab('show')
                break;
            case 'product-list':
                $('.breadcrumb-title small').text('Product List View');
                $('.sidebar .product-list').addClass('active').parent().addClass('active')
                $('.sidebar .product-list').closest('.collapse').addClass('show').prev().attr('aria-expanded', true).parent().addClass('active')
                $('#list-view-tab').tab('show')
                break;
            default:
            break;
        }
    })

/*---------------------------------------------------------------------
    Column filter datatable
-----------------------------------------------------------------------*/
    if ($('[data-table="eCommerce-admin"]').length) {
        $('[data-table="eCommerce-admin"] tfoot th').each(function () {
        const title = $(this).attr('title');
        $(this).html(`<td><input type="text" class="form-control form-control-sm" placeholder="${title}" /></td>`);
        });
        $('[data-table="eCommerce-admin"]').DataTable({
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


})();
