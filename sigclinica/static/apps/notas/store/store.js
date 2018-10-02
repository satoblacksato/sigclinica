import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import recurso from '../recursos/api.json'

import {nota} from './nota'

Vue.use(Vuex)

export const store = new Vuex.Store({
	modules: {
		nota
	}
})