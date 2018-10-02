<template>
	<div class="modal fade" id="paciente_editar" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel"><i class="fa fa-user"></i>  Editar Paciente</h4>
      </div>
      <div class="modal-body">
        <form method="post" @submit.prevent="guardarPaciente()">
           <div class="row">
      <div class="col-md-6">
          <!-- control input -->
            <p><label for="recipient-name" class="control-label">Nombre:</label>
            <p :class="{ 'control': true }">  
              <input type="text" v-validate="'required'" name="nombre" v-model="paciente.nombre"  class="form-control"required="true">
              <span v-show="errors.has('nombre')" class="danger">
                <div class="alert alert-danger" role="alert">
                  <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                  <span class="sr-only">Error:</span>
                   El campo Nombre es requerido
                </div>
              </span>
            </p>
        </p>
        <!-- control input -->  
        <!-- control input -->  
        <p>
          <label for="recipient-name" class="control-label">Apellido:</label>
          <p :class="{ 'control': true }">  
            <input type="text" v-validate="'required'" name="apellido" v-model="paciente.apellido" class="form-control" required="true">
             <span v-show="errors.has('apellido')" class="danger">
                <div class="alert alert-danger" role="alert">
                  <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                  <span class="sr-only">Error:</span>
                   El campo Apellido es requerido
                </div>
              </span>
          </p>  
        </p>
        <!-- control input -->  

        <p><label for="recipient-name" class="control-label">Tipo:</label>
            <select class="form-control" v-model="paciente.tipo_documento">
                <option v-for="(key, value) in tipo_documento" :value="key" v-text="value"></option>
            </select></p>
        <p>
          <label for="recipient-name" class="control-label">Documento:</label>
          <input type="text" v-model="paciente.documento" class="form-control">
        </p>
         <p>
            <label for="recipient-name" class="control-label">Observación:</label>
            <input type="text" v-model="paciente.observacion" class="form-control">
          </p>
      </div>
      <div class="col-md-6">
        <p>
          <label for="recipient-name" class="control-label">Teléfono Fijo:</label>
          <input type="text" v-model="paciente.telefono_fijo" class="form-control">
        </p>
        <p>
          <label for="recipient-name" class="control-label">Celular:</label>
          <p :class="{ 'control': true }">  
            <input required="true" v-validate="'required'" type="text" name="telefono_celular" v-model="paciente.telefono_celular" class="form-control">
             <span v-show="errors.has('telefono_celular')" class="danger">
                <div class="alert alert-danger" role="alert">
                  <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                  <span class="sr-only">Error:</span>
                   Debe cargar por lo menos un telefono
                </div>
              </span>
          </p> 
        </p>
        <p>
          <label for="recipient-name" class="control-label">Edad:</label>
          <p :class="{ 'control': true }">  
            <input required="true" v-validate="'required|numeric'" type="numeric" name="edad" v-model="paciente.edad" class="form-control">
             <span v-show="errors.has('edad')" class="danger">
                <div class="alert alert-danger" role="alert">
                  <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                  <span class="sr-only">Error:</span>
                    Este campo es requerido y es númerico
                  </div>
              </span>
          </p> 
        </p>
        <!-- control input -->
        <p><label for="recipient-name" class="control-label">Nº de Afiliado:</label>
            <p>  
              <input type="text" name="numero_afiliado" v-model="paciente.numero_afiliado"  class="form-control"required="true">
            </p>
        </p>
        <!-- control input --> 
        <p>
          <label for="recipient-name" class="control-label">Domicilio:</label>
          <input type="text" v-model="paciente.domicilio" class="form-control">
        </p>
        <!-- 
        <p>
          <label for="recipient-name" class="control-label">Foto:</label>
          <dropzone id="myVueDropzone" url="/pacientes/api/fotos/" v-on:vdropzone-success="showSuccess">
                <input type="hidden" name=token :value="toke_foto">
          </dropzone>
        </p>
        -->
      </div>
      <template v-if="paciente.obra_social">
        <div class="col-md-12">
          <label for="recipient-name" class="control-label">Seleccione Obra Social:</label>
          <p :class="{ 'control': true }">
            <select v-validate="'required'" name="obra_social" v-model="paciente.obra_social.id" class="form-control">
            <option v-for="obra in obras" :value="obra.id" v-text="obra.descripcion"></option>
            </select>
             <span v-show="errors.has('obra_social')" class="danger">
              <div class="alert alert-danger" role="alert">
                <span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                <span class="sr-only">Error:</span>
                  Seleccione una obra social 
                </div>
            </span>
          </p>  
        </div>
       </template> 

      <!--<div class="col-md-12">
        <label for="recipient-name" class="control-label">Seleccione Médico:</label>
        <v-select :required="true" label="apellido" multiple :value.sync="selected" :options="options"></v-select>
      </div> -->
      </div>
        <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Salir</button>
        <button type="submit" class="btn btn-primary">Guardar paciente</button>
      </div> 

        </form>
      </div>
      
    </div>
  </div>
</div>
</template>

<script>
  import Vue from 'vue'
  import axios from 'axios'
  import recurso from '../recursos/api.json'
  import tipo_documento from '../recursos/tipo_documento.json'
  import Dropzone from 'vue2-dropzone'
  import vSelect from 'vue-select'
  import VeeValidate from 'vee-validate'
  

  const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
  };

  Vue.use(VeeValidate);

  export default {
    data: function(){
      return {
        tipo_documento: tipo_documento,
        api: recurso,
        toke_foto: config,
        obrasocial_select: null,
        options: [],
        obras: ['obra social 1', 'obra social 2']
      }
    },
    methods: {
      guardarPaciente(){
        this.$validator.validateAll().then((result) => {
          console.log(this.api.pacientes);
          console.log(this.paciente.id);
          console.log(this.paciente);
          if (result) {
            this.paciente.obra_social = this.paciente.obra_social.id;
            axios.put(this.api.pacientes + this.paciente.id + '/', this.paciente)
            .then((response) => 
            {
                this.mensaje('', 'El Paciente se modifico de forma correcta');
                this.$emit('cargar');
                $('#paciente_editar').modal('hide');
            })
          }
        })
      },
      'showSuccess': function (file) {
        this.paciente.foto = '/media/fotos_pacientes/' + file.name;
        console.log(this.paciente.foto);
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
      cargarObraSociales(){
        axios.get(this.api.obrasociales)
        .then((response) => this.obras = response.data)
      }
    },
    mounted: function(){
      this.paciente.tipo_documento = 'LIBRETA ELECTORAL O DNI';
      this.cargarObraSociales();
      axios.get(this.api.empleados)
      .then((response => 
      {
        this.options = response.data;
      }))
    },
    components: {
      Dropzone,
      vSelect
    },
    props:{
    	paciente: {
    		required: true
    	}
    }
  }
</script>