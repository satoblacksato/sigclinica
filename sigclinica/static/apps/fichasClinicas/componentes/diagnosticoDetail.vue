<template>
	<div class="modal fade" id="historia_clinica_detail" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel"><i class="fa fa-user"></i> Detalle del Paciente y sus Estudios </h4>
      </div>
      <div class="modal-body">
        <div class="col-lg-12">
        <table class="table">
            <thead>
            <tr>
                <th>#</th>
                <th>Fecha</th>
                <th>Motivo de Consulta</th>
                <th>Antecedentes</th>
                <th>Diagnóstico</th>
                <th>Tratamiento</th>
            </tr>
            </thead>
            <tbody>
            <template v-for="ficha in get_fichas">	
                <tr>
                	<td v-text="ficha.id" ></td>
                    <td >{{ ficha.fecha | formato_fecha }}</td>
                    <td v-text="ficha.motivo_consulta"></td>
                    <td v-text="ficha.antecedentes_enfermedad"></td>
                    <td v-text="ficha.diagnostico"></td>
                    <td v-text="ficha.tratamiento"></td>
                </tr>
            </template>
            </tbody>
        </table>
   
    </div>
        <ul class="pager">
              <li class="previous" v-if="get_previo" @click="atras"><a>&larr; Anterior</a></li>
              <li class="next" v-if="get_siguiente" @click="siguiente"><a>Siguiente &rarr;</a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import {mapActions, mapGetters} from 'vuex'

export default{	
	data(){
		return{

		}
	},
	methods: {
		...mapActions(['detalle', 'fichaSiguiente', 'fichaAtras']),
    siguiente(){
      this.fichaSiguiente(this.get_siguiente)
    },
    atras(){
      this.fichaAtras(this.get_previo)
    }
	},
	props: {
		paciente: {
			required: true
		}
	},
	watch: {
		paciente(value){
			this.detalle(value.id)
		}
	},
    computed: mapGetters(['get_fichas', 'get_siguiente', 'get_previo']),
    filters: {
          formato_fecha(value) {
                return value.split('-')[2] + '/' + value.split('-')[1] + '/' + value.split('-')[0]
          }
        }
}
</script>