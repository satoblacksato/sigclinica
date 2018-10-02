import Vue from 'vue'
import Vuex from 'vuex'
import notaLista from './complementos/nota_lista.vue'
import {store} from './store/store'

Vue.use(Vuex)


var app = new Vue({
	el: '#app',
	data: {
		titulo: 'Cree y liste sus notas'
	},
	store,
	components:{
		notaLista
	}
})