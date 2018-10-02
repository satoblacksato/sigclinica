import Vue from 'vue'
import Vuex from 'vuex'

import {chat} from '../../chat/store/chat'

export const store = new Vuex.Store({
	modules: {chat}
})