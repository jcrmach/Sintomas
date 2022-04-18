const sintomas = document.getElementsByName('sintomas');

const searchbox = document.getElementById('search');
const btnDiagnosticar = document.getElementById('diagnosticar');

const p = document.getElementById('not-found');

searchbox.addEventListener('input', function() {
    p.classList.add("visually-hidden");

    if (!this.value) {
        btnDiagnosticar.disabled = false;
        btnDiagnosticar.classList.remove("visually-hidden");

        sintomas.forEach(sintoma => {
            sintoma.closest("div").classList.remove("visually-hidden");
        })
    } else {
        btnDiagnosticar.disabled = true;
        btnDiagnosticar.classList.add("visually-hidden");

        var counter = 0;
        sintomas.forEach(sintoma => {
            if (!sintoma.value.toLowerCase().includes(this.value.toLowerCase())) {
                sintoma.closest("div").classList.add("visually-hidden");
                
                counter += 1;
                
                if (counter == sintomas.length) {
                    p.classList.remove("visually-hidden");
                }
            } else {
                sintoma.closest("div").classList.remove("visually-hidden");
            }
        });
    }
});
