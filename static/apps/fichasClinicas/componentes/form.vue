<template>
	<!-- Modal -->
	<div id="form_ficha_clinica" class="modal fade" role="dialog">
	  <div class="modal-dialog modal-lg">

	  	<form @submit.prevent="guardarFicha">
		    <!-- Modal content-->
		    <div class="modal-content">
		      <div class="modal-header">
		        <button type="button" class="close" data-dismiss="modal">&times;</button>
		        <h4 class="modal-title">Fichas Clínicas <i class="fa fa-heartbeat" aria-hidden="true"></i></h4>
		      </div>
		      <div class="col-lg-12">
	                <table class="table">
	                    <thead>
	                    <tr>
	                        <th>#</th>
	                        <th>Nombre y Apellido</th>
	                        <th>Documento</th>
	                        <th>Edad</th>
	                        <th>Obra Social</th>
	                    </tr>
	                    </thead>
	                    <tbody>
	                    <template v-if="turno.paciente != undefined">	
		                    <tr>
		                    	<td v-text="turno.paciente.id"></td>
		                        <td v-text="turno.paciente.nombre + ' ' + turno.paciente.apellido"></td>
		                        <td v-text="turno.paciente.documento"></td>
		                        <td v-text="turno.paciente.edad"></td>
		                        <td v-text="turno.paciente.obra_social.descripcion"></td>
		                    </tr>
	                    </template>
	                    </tbody>
	                </table>
	            </div>
	             <!-- tabla de diagnosticos -->
	             <template v-if="turno.paciente != undefined">
	            	<diagnostico ref="diagnosticolista" :turno="turno"></diagnostico>
	             </template>	
	            <!-- tabla de diagnosticos -->
		      <div class="modal-body">
		        <p>
		        	<label for="recipient-name" class="control-label">Motivo de Consulta:</label>  
	          			<textarea name="motivo_consulta" v-model="ficha.motivo_consulta" type="text" class="form-control"> </textarea>
		        </p>
		        <p>
		        	<label for="recipient-name" class="control-label">Antecedentes de la Enfermedad:</label>
	          		<textarea type="text" v-model="ficha.antecedentes_enfermedad" class="form-control"> </textarea>
		        </p>
		        <p>
		        	<label for="recipient-name" class="control-label">Diagnóstico:</label>
	          		<textarea type="text" v-model="ficha.diagnostico" class="form-control"> </textarea>
		        </p>
		        <p>
		        	<label for="recipient-name" class="control-label">Tratamiento:</label>
	          		<textarea type="text" v-model="ficha.tratamiento" class="form-control"> </textarea>
		        </p>
		      </div>
		      <div class="modal-footer">
		      	<button type="submit" class="btn btn-success" >Guardar</button>
		        <button type="button" class="btn btn-default" data-dismiss="modal">Salir</button>
		      </div>
		    </div>
		 </form>   
	  </div>
	</div>
</template>
<script>
	import Vue from 'vue'
	import axios from 'axios'
	import VeeValidate from 'vee-validate';
	import diagnostico from './diagnosticos_list.vue'

	Vue.use(VeeValidate);

	const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
  	};

	export default{
		data(){
			return{
				ficha: {
					paciente: '',
					motivo_consulta: '',
					antecedentes_enfermedad: '',
					diagnostico: '',
					empleado: null,
					tratamiento: ''
				}
			}
		},
		methods: {
			guardarFicha(){
				this.$validator.validateAll().then((result) => {
	          		if (result) {
						this.ficha.paciente = this.turno.paciente.id; 
						axios.post('/historia/clinica/api/historia_clinica/', this.ficha, config)
						.then((response) => 
						{
							this.ficha.motivo_consulta = '';
							this.ficha.antecedentes_enfermedad = '';
							this.antecedentes_enfermedad = '';
							this.ficha.diagnostico = '';
							this.ficha.tratamiento = '';
							this.mensaje(' ', 'La ficha se guardo con éxito');
							this.cambiarEstadoTurno();
							this.$emit('cargar');
							this.$refs.diagnosticolista.cargarFichas();		
							
						})
						.catch((error) => 
						{
							console.log(error);
						})
					}
				})
			},
			cambiarEstadoTurno(){
				let background_color = '#54E311';
				axios.patch('/turnos/api/turnos/' + this.turno.id + '/', 
					{
						backgroundColor: background_color,
						estado: 'atendido'
					}, config)
				.then((response)=> 
				{
					console.log(' se cambio el estado del turno')
				})
			},
			mensaje(titulo, texto){
	          setTimeout(function() {
	              toastr.options = {
	                  closeButton: true,
	                  progressBar: true,
	                  showMethod: 'slideDown',
	                  timeOut: 4000
	              };
	              toastr.success(titulo, texto);
	          }, 1300);
          }
		},
		components:{
			diagnostico
		},
		props: {
			turno: {
				required: false
			}
		}
	}
</script>