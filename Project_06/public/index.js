function carregarAnimais(){
    axios.get('http://localhost:8000/animais')
    .then(response => console.log(response.data))
}

function app(){
    console.log("App Iniciada!")
    carregarAnimais()
}

app()