Vue.prototype.$http = axios;
Vue.use(Vuetable);

var app = new Vue({
    el: '#app',
    data: {
        fields: ['cpf', 'nome'],
        cpf: "",
        nome: ""
    },
    methods: {
        getAutores(){
            this.$http.get("http://127.0.0.1:5000/autor").then((response) => {
                console.log(response.data)
            });
        },
        addAutor(){
            console.log("cpf: " + this.cpf);
            console.log("nome: " + this.nome);
            this.$http.post("http://127.0.0.1:5000/autor/", {
                cpf : this.cpf,
                nome : this.nome
            }).then((response) => {
                alert("Refresh the page to see inserted data")
            });
        }
    }
});

