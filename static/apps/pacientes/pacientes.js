import Vue from 'vue'
import pacientes_tabla from './componentes/paciente_list.vue'
import {store} from './store/store'

var app = new Vue({
    el: '#app',
    store: store,
    components: {
        pacientes_tabla
    }
})