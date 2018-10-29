document.querySelector('#cepForm').addEventListener('submit', getCepInfo);

function getCepInfo(e) {
    const cep = document.querySelector('.cep').value;

    fetch(`//viacep.com.br/ws/${cep}/json`)
        .then(Response => {
            return Response.jason();

        })
        .then(data => {

            console.log(data);
        });

    e.preventDefault();

}