import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import recurso from '../recursos/api.json'

Vue.use(Vuex)

export const store = new Vuex.Store({
	state: {
		obra_sociales: []
	},
	getters: {
		obra_sociales: (state) => {
			return state.obra_sociales
		}
	},
	mutations: {
		cargarObrasSociales: (state) => {
            axios.get(recurso.obrasocial)
            .then((response) => state.obra_sociales = response.data)
        }
	},
	actions: {
		cargar: (context) => {
			context.commit('cargarObrasSociales');
		}
	}
})