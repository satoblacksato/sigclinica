import Vue from 'vue'
import sala from './componentes/sala.vue'
import {store} from './store/store'
import CxltToastr from 'cxlt-vue2-toastr'


var toastrConfigs = {
    position: 'top right',
    showDuration: 4000
}

Vue.use(CxltToastr, toastrConfigs)

var app = new Vue({
	el: '#app',
	data: {
		titulo: 'Sistema de mensajeria instantanea '
	},
	store,
	components: {
		sala
	}
})