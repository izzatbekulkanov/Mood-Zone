(function(){
  "use strict";
      /*--------------single----------------*/
  $(".select2-basic-single").select2();

      /*--------------tags----------------*/
  $(".select2-basic-single-tag").select2({
      tags: true
  });

      /*--------------multiple----------------*/
  $(".select2-basic-multiple").select2();

      /*--------------disble----------------*/
  var $disabledResults = $(".select2-disabled ");
  $disabledResults.select2();

      /*--------------placeholder----------------*/
  $('.select2-placeholder').select2({
    placeholder: "Select a State",
    allowClear: true
  });
  /*--------------maximum num----------------*/
  $(".select2-multiple-limit").select2({
    maximumSelectionLength: 3
  });

  /*--------------theme----------------*/
  $(".select2-theme-single").select2({
    theme: "classic"
  });
    /*--------------select 2----------------*/
  $(".select2-option-creation").select2({
    tags: true
  });
    /*--------------select 2 automatic----------------*/
  $(".select2-automatic-tokenizer").select2({
    tags: true,
    tokenSeparators: [',', ' ']
  })
})();
