import Vue from 'vue'
import Vuex from 'vuex'

import {store} from './store/store'

Vue.use(Vuex)

import ventanaChat from './componentes/ventanaChat.vue'

var ventana = new Vue({
	el: '#ventana',
	data: {
		titulo: 'Ventana de Chat'
	},
	store,
	components: {
		ventanaChat
	}
})
