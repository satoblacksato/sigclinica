import Vue from 'vue'
import listado from './componentes/listado.vue'
import {store} from './store/store'

var app = new Vue({
	el: '#app',
	data: {},
	store,
	components: {
		listado
	}
})
