const canvas = document.querySelector("#visitsignature");
if(canvas != undefined && canvas !== null) {
    const signaturePad = new SignaturePad(canvas, {
        backgroundColor: 'rgb(233, 236, 239)'
    });
    const resetBtn = IQUtils.getElem('#clear-sign')
    if(resetBtn != undefined && resetBtn !== null){
        resetBtn.addEventListener('click', function (e) {
            signaturePad.clear();
        })
    }
}

