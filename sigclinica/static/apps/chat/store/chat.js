import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import recurso from '../recursos/api.json'

Vue.use(Vuex)

export const chat = {
	state: {
		mensajes: [],
		usuarios: [],
		usuario_seleccion: ''
	},
	actions: {
		cargarMensajes: (context) => {
			axios.get(recurso.mensaje)
			.then((response) => context.commit('cargarMensajes', response.data.results))
		},
		guardarMensaje: (context, mensaje) => {
			axios.post(recurso.mensaje, {
				    mensaje: mensaje,
				    leido: false,
				    emisor: null
			})
			.then((response) => context.commit('guardarMensaje', response.data))
		},
		cargarUsuarios: (context) => {
			axios.get(recurso.usuarios)
			.then((response) => {
				context.commit('cargarUsuarios', response.data)
			})
		}
	},
	mutations: {
		cargarMensajes: (state, Mensajes) => state.mensajes = Mensajes.reverse(),
		guardarMensaje: (state, Mensaje) => state.mensajes.push(Mensaje),
		cargarUsuarios: (state, Usuarios) => state.usuarios = Usuarios,
		seleccionUsuario: (state, Usuario) => {
			state.usuario_seleccion = Usuario
			console.log(state.usuario_seleccion)
		}
	},
	getters: {
		mensajes: (state) => {
			return state.mensajes
		},
		usuarios: (state) => {
			return state.usuarios
		},
		usuario_seleccion: (state) => {
			return state.usuario_seleccion
		}
	}
}