import Vue from 'vue'
import Vuex from 'vuex'

import {empleado} from './empleado'

Vue.use(Vuex)

export const store = new Vuex.Store({
	modules: {empleado}
})