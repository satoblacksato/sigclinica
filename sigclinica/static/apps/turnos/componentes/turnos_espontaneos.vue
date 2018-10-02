<template>
	<div class="col-lg-6">
<div class="ibox float-e-margins">
	    <div class="ibox-title">
	        <h5>Alta de turnos</h5>
	        <div class="ibox-tools">
	            <a class="collapse-link">
	                <i class="fa fa-chevron-up"></i>
	            </a>
	            <a class="close-link">
	                <i class="fa fa-times"></i>
	            </a>
	        </div>
	    </div>
            <form @submit.prevent="guardar">
                <div class="ibox-content">
        			<p><label for="recipient-name" class="control-label">Seleccione el Paciente:</label>
                        <select v-model="turno.paciente" class="form-control" id="id_paciente">
                            <option v-for="paciente in pacientes" :value="paciente.id" v-text="paciente.nombre + ' ' + paciente.apellido + ' - ' + paciente.documento"> </option>
                        </select>
                        <span  v-if="paciente.error" class="danger">
                          <div class="alert alert-danger" role="alert">
                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            <span class="sr-only">Error:</span>
                              Seleccione un paciente
                            </div>
                        </span>
                    </p>
                    <p><label for="recipient-name" class="control-label">Seleccione el Médico:</label>
                        <select v-model="turno.empleado"  class="form-control" id="id_medico">
                            <option v-for="empleado in empleados" :value="empleado.id" v-text="empleado.nombre + ' ' + empleado.apellido" > </option>
                        </select>
                        <span  v-if="medico.error" class="danger">
                          <div class="alert alert-danger" role="alert">
                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            <span class="sr-only">Error:</span>
                              Seleccione un Médico
                            </div>
                        </span>
                    </p>
                    <div class="modal-footer">
                            <button type="submit" class="btn btn-primary">Guardar Turno</button>
                      </div> 
                </div>
            </form>    
        </div>
    </div>
</template>
<script>

import {mapGetters, mapActions} from 'vuex'

export default{
	data(){
		return{
			turno: {
                paciente: '',
                empleado: '',
                title: '',
                start: '',
                backgroundColor: ''
            },
            paciente: {
                error: false
            },
            medico: {
                error: false
            }
		}
	},
    methods: {
        ...mapActions(['cargarPacientesAsync', 'cargarEmpleados', 'guardarTurno']),
        guardar(){
            var today = new Date();
            var dd = today.getDate();
            var mm = today.getMonth()+1; //January is 0!
            var yyyy = today.getFullYear();
            var hora = today.getHours();
            var minutos = today.getMinutes();
            var segundos = today.getSeconds();

            if(dd<10) {
                dd = '0'+dd
            } 
            if(mm<10) {
                mm = '0'+mm
            } 
            today = yyyy + '-' + mm + '-' + dd + 'T' + hora + ':' + minutos + ':' + segundos;
            this.turno.start = today;
            this.turno.backgroundColor = '#F41826';
            this.turno.paciente = $('#id_paciente').val();
            this.turno.empleado = $('#id_medico').val();
            this.turno.title = $("#id_paciente option:selected").text();
            if ($('#id_paciente').val() && $('#id_medico').val()){
                this.paciente.error = false;
                this.medico.error = false;
                this.guardarTurno(this.turno);
                this.$toast.success({
                    title:'Sistema',
                    message:'El turno por orden de llegada se guardo con éxito'
                })
                $('#id_paciente').val(' ');
                $('#id_medico').val(' ');
            }else{
                if (!$('#id_paciente').val()) this.paciente.error = true
                if (!$('#id_medico').val()) this.medico.error = true
                 this.$toast.error({
                    title:'Sistema',
                    message:'El formulario tiene errores'
                })    
            }
            
        }
    },
    mounted(){
        this.cargarPacientesAsync();
        this.cargarEmpleados();
    },
    computed: mapGetters(['pacientes', 'empleados'])
}
</script>