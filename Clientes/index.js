Vue.prototype.$http = axios;
Vue.use(Vuetable);

var app = new Vue({
    el: '#app',
    data: {
        fields: ['cpf', 'nome']
    },
    methods: {
        getAutores(){
            this.$http.get("http://127.0.0.1:5000/").then((response) => {
                console.log(response.data)

            });
        }
    }
});

