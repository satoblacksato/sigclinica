
import {detalle, fichaSiguiente, fichaAtras} from './actions'
import {get_fichas, get_siguiente, get_previo} from './getters'

export const fichas = {
	state: {
		ficha: [],
		siguiente: '',
		previo: ''
	},
	actions: {detalle, fichaSiguiente, fichaAtras},
	mutations: {
		cargarFicha: (state, ficha ) =>{
			state.ficha = ficha.results
			state.siguiente = ficha.next
			state.previo = ficha.previous
		}
	},
	getters: {get_fichas, get_siguiente, get_previo}
}