(function () {
    "use strict";
    $(document).on('click', '[data-load-file="file"]' ,function(){
        let target = $(this).attr('data-load-target')
        let url = $(this).attr('data-url')
        let title = $(this).attr('data-title')
        let previewUrl = $(this).attr('data-preview-url')
        $('.modal-title').html(title)
        $('.modal-preview-link').attr('href', previewUrl)
        loadDocToHtml(target, url)
    })

    function loadDocToHtml(target, url){
        $(target).html('')
        $(target).officeToHtml({
            url: url,
            pdfSetting: {
                setLang: "",
                setLangFilesPath: "" /*"include/pdf/lang/locale" - relative to app path*/
            }
        });
    }
})()