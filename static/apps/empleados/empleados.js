import Vue from 'vue'
import perfil_alta from './componentes/perfil_alta.vue'

var app = new Vue({
    el: '#app',
    data: {
        titulo: 'Carga de Datos personales'
    },
    components: {
        perfil_alta
    }
});