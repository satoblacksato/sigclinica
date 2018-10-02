<template>
	<div id="form_estados" class="modal fade" role="dialog">
	  <div class="modal-dialog">

	    <!-- Modal content-->
	    <div class="modal-content">
	      <div class="modal-header">
	        <button type="button" class="close" data-dismiss="modal">&times;</button>
	        
	        <button type="button" class="btn btn-danger" @click="eliminar_turno" >Eliminar este Turno</button>
	      </div>
	      <div class="modal-body">
	      	<p>
	      		<h4 class="modal-title">Cambiar Estado del turno</h4>
	        	<input type="text" name="numero_turno" hidden="hidden" class="clase_turno" id="id_numero_turno">
	        </p>
	        <p>
	        	<select class="form-control" v-model="select_estado" >
	        		<option value="presente">Se encuentra Presente</option>
	        		<option value="cambio" >Cambio el turno</option>
	        	</select>
	        </p>

	      </div>
	      <div class="modal-footer">
	      	<button type="button" class="btn btn-success" @click="guardar_turno" >Guardar</button>
	        <button type="button" class="btn btn-default" data-dismiss="modal">Salir</button>
	      </div>
	    </div>

	  </div>
	</div>
</template>
<script>
	import axios from 'axios'

	const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
  	};

	export default{
		data(){
			return {
				numero_turno: 0,
				select_estado: 'presente'
			}
		},
		methods: {
			error(titulo, texto){
	          setTimeout(function() {
	              toastr.options = {
	                  closeButton: true,
	                  progressBar: true,
	                  showMethod: 'slideDown',
	                  timeOut: 6000
	              };
	              toastr.error(titulo, texto);
	          }, 1300);
	          },
			eliminar_turno(){
				this.numero_turno = $('#id_numero_turno').val();
				axios.delete('/turnos/api/turnos/' + this.numero_turno + '/', config)
				.then((response)=> 
				{
					this.error(' ', 'Este turno fue eliminado del calendario ');
					window.location.href = "/turnos/alta/";
				})
				.catch((error) => 
				{
					console.log(error);
				})
			},
			guardar_turno(){
				let background_color = '#E8EF0C'
				// o cambiar al color verde : #54E311 o rojo : '#F41826'
				if (this.select_estado == 'presente'){
					background_color = '#F41826';
				}
				this.numero_turno = $('#id_numero_turno').val();
				axios.patch('/turnos/api/turnos/' + this.numero_turno + '/', 
					{
						backgroundColor: background_color,
						estado: this.select_estado
					}, config)
				.then((response)=> 
				{
					this.mensaje(' ', 'Se cambio el estado del turno');
					$('#form_estados').modal('hide');
				})
				.catch((error) => 
				{
					console.log(error);
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
	          },
		},
		props: {
		}
	}
</script>