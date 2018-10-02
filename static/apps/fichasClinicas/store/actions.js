import Vue from 'vue'
import axios from 'axios'

export const cargarListado = (context) => {
	axios.get('/historia/clinica/api/historia_informe/')
	.then((response) => {
		context.commit('cargarPacientes', response.data)
	})
}

export const siguientePaciente = (context, siguiente) => {
	axios.get(siguiente)
	.then((response) => {
		context.commit('cargarPacientes', response.data)
	})
}

export const previoPaciente = (context, previo) => {
	axios.get(previo)
	.then((response) => {
		context.commit('cargarPacientes', response.data)
	})
}