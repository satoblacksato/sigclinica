
import Vue from 'vue'
import axios from 'axios'


export const detalle = (context, paciente) => {
	axios.get("/historia/clinica/api/historia_clinica/" + '?paciente=' + paciente)
	.then((response) => {
		context.commit('cargarFicha', response.data)
	})
}

export const fichaSiguiente = (context, siguiente) => {
	axios.get(siguiente)
	.then((response) => {
		context.commit('cargarFicha', response.data)
	})
}

export const fichaAtras = (context, previo) => {
	axios.get(previo)
	.then((response) => {
		context.commit('cargarFicha', response.data)
	})
}