import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import recurso from '../recursos/api.json'
import {cargarPacientesAsync, paginaSiguienteAsync, paginaAtrasAsync, buscarAsync} from './actions'
import {pacientes, siguiente, atras} from './getters'

Vue.use(Vuex)

export const paciente = {
	state: {
		pacientes: [],
		siguiente: '',
		atras: ''
	},
	getters: {pacientes, siguiente, atras},
	mutations: {
		cargarPacientes: (state) => {
			axios.get(recurso.pacientes)
			.then((response) => 
			{
				state.pacientes = response.data.results;
				state.siguiente = response.data.next;
				state.atras = response.data.previous;
			})
		},
		paginaSiguiente: (state) => {
			axios.get(state.siguiente)
			.then((response) => 
			{
				state.pacientes = response.data.results;
				state.siguiente = response.data.next;
				state.atras = response.data.previous;
			})
		},
		paginaAtras: (state) => {
			axios.get(state.atras)
			.then((response) => 
			{
				state.pacientes = response.data.results;
				state.siguiente = response.data.next;
				state.atras = response.data.previous;
			})
		},
		buscar: (state, buscar) => {
			console.log(recurso.pacientes + '?' + buscar.campo + '=' + buscar.valor);
			axios.get(recurso.pacientes + '?' + buscar.campo + '=' + buscar.valor)
			.then((response) => 
			{
				state.pacientes = response.data.results;
				state.siguiente = response.data.next;
				state.atras = response.data.previous;
			})
		}
	},
	actions: {cargarPacientesAsync, paginaSiguienteAsync, paginaAtrasAsync, buscarAsync}
}
