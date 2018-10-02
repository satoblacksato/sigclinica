import Vue from 'vue'
import Vuex from 'vuex'
import axios from'axios'
import {paciente} from '../../pacientes/store/paciente'
import {empleado} from '../../empleados/store/empleado'

Vue.use(Vuex)

const config = {
    headers: {'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()}
 };

export const store = new Vuex.Store({
	state: {

	},
	actions: {
		guardarTurno: (context, turno) => {
			console.log(turno);
			axios.post('/turnos/api/turnos/', turno, config)
			.then((response) => 
			{
				console.log('el turno se guardo con exito')
			})
			.catch((error) => 
			{
				console.log(error)
			})
		}
	},
	mutations: {

	},
	getters: {

	},
	modules: {
		paciente,
		empleado
	}
});