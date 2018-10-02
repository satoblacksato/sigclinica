import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import recurso from '../recursos/api.json'

import {paciente} from './paciente'

Vue.use(Vuex)

export const store = new Vuex.Store({
	modules: {
		paciente
	}
})