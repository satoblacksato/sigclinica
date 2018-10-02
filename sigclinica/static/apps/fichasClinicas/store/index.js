import Vue from 'vue'
import Vuex from 'vuex'

import {cargarListado, siguientePaciente, previoPaciente} from './actions'
import {pacientes, g_siguiente, g_previo} from './getters'
import {fichas} from './fichas'

Vue.use(Vuex)

export const store = new Vuex.Store({
	state: {
		pacientes: [],
		previo: '',
		siguiente: ''
	},
	actions: {
		cargarListado, siguientePaciente, previoPaciente
	},
	mutations: {
		cargarPacientes: (state, data) => {
			state.pacientes = data.results;
			state.previo = data.previous;
			state.siguiente = data.next;
		}
	},
	getters: {
		pacientes, 
		g_siguiente, 
		g_previo
	},
	modules: {fichas}
})