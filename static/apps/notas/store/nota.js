import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'
import recurso from '../recursos/api.json'

Vue.use(Vuex)

export const nota = {
	state: {
		notas: [],
		nota: {
			fecha: '',
			nota: ''
		}
	},
	actions: {
		cargarNotas: (context) => {
			axios.get(recurso.nota)
			.then((response) => {
				context.commit('cargarNotas', response.data)
				console.log(response.data)
			})
		},
		guardarNota: (context, nota) => {
			console.log(nota);
			axios.post(recurso.nota, nota)
			.then((response) => {
				nota = response.data
				context.commit('cargarNota', nota)
			})
		},
		eliminarNota: (context, id) => {
			axios.delete(recurso.nota + id)
			.then((response) => {
				console.log(response)
			})
		}
	},
	mutations: {
		cargarNotas: (state, notas) => {state.notas = notas},
		cargarNota: (state, nota) => {state.notas.push(nota)}
	},
	getters: {
		notas: (state) =>{
			return state.notas
			console.log(state.notas)
		}
	}
}