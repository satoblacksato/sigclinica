import Vue from 'vue'
import turnosTabla from './componentes/turnos_list.vue'
import Calendario from './componentes/calendario.vue'
import turno_alta from './componentes/turnos_form.vue'
import turno_lista from './componentes/turnos_list.vue'
import turno_espontaneos from './componentes/turnos_espontaneos.vue'
import Tooltip from 'vue-directive-tooltip'
import {store} from './store/store'
import CxltToastr from 'cxlt-vue2-toastr'


var toastrConfigs = {
    position: 'top right',
    showDuration: 4000
}


Vue.use(Tooltip);
Vue.use(CxltToastr, toastrConfigs)

/*Vue.filter('formatoHora', function (value) {
  console.log(value)
  console.log(value.split('T')[1])      
  return   value.split('T')[1]
})*/


var app = new Vue({
	el: '#app',
	data: {
		titulo: 'Turnos de Pacientes'
	},
	store,
	mounted(){
		console.log(this.titulo);
	},
	components: {
		turnos_tabla: turnosTabla,
		calendario: Calendario,
		turno_alta: turno_alta,
		turno_lista: turno_lista,
		turno_espontaneos: turno_espontaneos
	}
});