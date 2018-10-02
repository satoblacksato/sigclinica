import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import recurso from '../recursos/api.json'

Vue.use(Vuex)

const config = {
    headers: {'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()}
};

export const empleado = {
	state: {
		empleados: []
	},
	actions: {
		cargarEmpleados: (context) => {
			axios.get(recurso.empleados + '?categoria=medico', config)
			.then((response) => 
			{
				context.commit('cargarEmpleados', response.data)
			})
		}
	},
	mutations: {
		cargarEmpleados: (state, empleados) => state.empleados = empleados 
	},
	getters: {
		empleados: (state) => {
			return state.empleados
		}
	}
}