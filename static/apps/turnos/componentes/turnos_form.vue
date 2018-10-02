<template>
	<div class="col-lg-3">
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
            <form @submit.prevent="guardarTurno">
                <div class="ibox-content">
                    <p><label for="recipient-name" class="control-label">Seleccione el Paciente:</label>
                        <select v-model="turno.paciente" class="form-control" id="id_paciente">
                            <option v-for="paciente in pacientes" :value="paciente.id" >{{ paciente.nombre + ' ' + paciente.apellido + ' ' + paciente.documento }}</option>
                        </select>
                        <span v-show="errores.paciente"  class="danger">
                          <div class="alert alert-danger" role="alert">
                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            <span class="sr-only">Error:</span>
                              Seleccione un paciente
                            </div>
                        </span>
                    </p>
                    <p>
                        <label for="recipient-name" class="control-label">Fecha:</label><input id="id_fecha" type="text" class="form-control"></input> 
                        <span v-show="errores.fecha"  class="danger">
                          <div class="alert alert-danger" role="alert">
                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            <span class="sr-only">Error:</span>
                              Seleccione una Fecha
                            </div>
                        </span>
                    </p>
                    <p>
                        <label for="recipient-name" class="control-label">Hora:</label><input class="form-control" id="id_hora" type="text" name="">
                        <span v-show="errores.hora"  class="danger">
                          <div class="alert alert-danger" role="alert">
                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            <span class="sr-only">Error:</span>
                              Seleccione una hora válida
                            </div>
                        </span>
                    </p>
                    <!--<p>
                        <label for="recipient-name" class="control-label">Motivo de consulta:</label>
                        <textarea class="form-control" type="text" name=""></textarea>
                    </p> -->
                    <p>
                        <label for="recipient-name" class="control-label">Seleccione el Médico:</label>
                        <select id="id_empleado" v-model="turno.empleado" class="form-control">
                            <option v-for="medico in medicos" :value="medico.id" v-text="medico.nombre + ' ' + medico.apellido"></option>
                        </select>
                        <span v-show="errores.medico"  class="danger">
                          <div class="alert alert-danger" role="alert">
                            <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                            <span class="sr-only">Error:</span>
                              Seleccione un médico
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
import Vue from 'vue'
import axios from 'axios'
import Datepicker from 'vuejs-datepicker'
import vSelect from "vue-select"
import recurso from '../recursos/api.json'
import turno from '../recursos/modelo.json'

const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
  };

export default {
    data: function(){
        return {
            pacientes: [],
            medicos: [],
            turno: turno,
            hora_turno: 0,
            fecha_turno: 0,
            errores: {
              medico: false,
              fecha: false,
              hora: false,
              paciente: false
            }
        }
    },
    methods:{
        cargarPaciente(){
            axios.get(recurso.pacientes_select)
            .then((response) => 
            {
                this.pacientes = response.data;
            })
        },
        cargarMedicos(){
            axios.get(recurso.empleados + '?categoria=medico')
            .then((response) => this.medicos = response.data)
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
        validar(){
          if (!$("#id_empleado").val()){
            this.errores.medico = true;
          }else{
            this.errores.medico = false; 
          }
          if (!$('#id_fecha').val()){
            this.errores.fecha = true;
          }else{
            this.errores.fecha = false; 
          }
          if (!$('#id_hora').val()){
            this.errores.hora = true;
          }else{
            this.errores.hora = false; 
          }
          if (!$('#id_paciente').val()){
            this.errores.paciente = true;
          }else{
            this.errores.paciente = false; 
          }
        },
        guardarTurno(){
            this.validar();
            this.turno.start = $('#id_fecha').val().split('/')[2] + '-' + $('#id_fecha').val().split('/')[1] + '-' + $('#id_fecha').val().split('/')[0] + ' ' + $('#id_hora').val();
            this.turno.paciente = $('#id_paciente').val();
            this.turno.title = $("#id_paciente option:selected").text();
            this.turno.empleado = $("#id_empleado").val();
            console.log('****************************')
            console.log(this.turno.empleado)
            console.log('****************************')
            if (this.turno.empleado != null){
                axios.post(recurso.turnos, this.turno, config)
                .then((response) => 
                {
                    this.mensaje(' ', 'El turno se agendo con éxito');
                    window.location.href = "/turnos/alta/";
                })
                .catch((error) => {
                    console.log(error);
                  });
            }else{
                this.error(' ', 'El formulario contiene errores, verifique los campos cargados. El turno no se asigno! ');
            }
        }
    },
    mounted: function(){
        this.cargarPaciente();
        this.cargarMedicos();
    },
    components:{
        Datepicker: Datepicker,
        vSelect: vSelect
    }
}
	
</script>