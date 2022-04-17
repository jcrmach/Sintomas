var sintomas = document.getElementsByName('sintomas');

var searchbox = document.getElementById('search')
var btnDiagnosticar = document.getElementById('diagnosticar')

searchbox.addEventListener('input', function(event) {
    console.log(this.value);
    if (!this.value) {
        btnDiagnosticar.classList.remove("visually-hidden");

        sintomas.forEach(sintoma => {
            sintoma.closest("div").classList.remove("visually-hidden");
        })
    } else {
        btnDiagnosticar.classList.add("visually-hidden");

        sintomas.forEach(sintoma => {
            if (!sintoma.value.toLowerCase().includes(this.value.toLowerCase())) {
                sintoma.closest("div").classList.add("visually-hidden");
            } else {
                sintoma.closest("div").classList.remove("visually-hidden");
            }
        });
    }
});
