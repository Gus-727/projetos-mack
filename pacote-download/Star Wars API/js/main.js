const base_url = 'https://swapi.dev/api'

window.onload = function () {
    for (var i = 0; i < 2; i++) {
        this.getAndShow(getRandom());
    }
}

function getRandom() {
    return Math.floor(Math.random() * 30) + 1;
}

function getAndShow(id) {
     
        var url = base_url + "/people" + "/" + id;

        callAPI(url, function (status, data) {
            let name = data.name;
            let height = data.height;
            let mass = data.mass;
            let hair_color = data.hair_color;
            let skin_color = data.skin_color;
            let eye_color = data.eye_color;
            let birth_year = data.birth_year;
            let gender = data.gender;

            document.getElementById("content").innerHTML += "<article>" +
                "<h1>" + name + "</h1>" +
                "<p>Height: " + height + "</p>" +
                "<p>Mass: " + mass + "</p>" +
                "<p>Hair color: " + hair_color + "</p>" +
                "<p>Skin color: " + skin_color + "</p>" +
                "<p>Eye color: " + eye_color + "</p>" +
                "<p>Birth year: " + birth_year + "</p>" +
                "<p>Gender: " + gender + "</p>" +
                "</article>";

        })

    }

function callAPI(url, callback) {
    var xhr = new XMLHttpRequest(); //Requisição no protocolo HTTP
    xhr.responseType = 'json'; //Tipo de resposta
    xhr.open('GET', url, true); //Abrir a mensagem do protocolo
    xhr.onload = function () { // função que será executada ao carregar a página
        if (xhr.status === 200) {
            callback(xhr.status, xhr.response)
        } else {
            alert('Problemas ao conectar com o servidor')
        }
    }
    xhr.send(); //Manda a resposta

}