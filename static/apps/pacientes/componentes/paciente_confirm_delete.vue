<template>
  <div class="modal fade" id="paciente_eliminar" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel"><i class="fa fa-user"></i>  Eliminar Paciente</h4>
      </div>
       <div class="modal-body">
          <p>Desea eliminar este paciente?</p>
        </div>
        <div class="modal-footer">
          <button type="button" data-dismiss="modal" class="btn">Cancelar</button>
          <button type="button" data-dismiss="modal" @click="confirmar" class="btn btn-primary">Confirmar</button>
        </div>
    </div>
  </div>
</div>
</template>
<script>
  import Vue from 'vue'
  import axios from 'axios'
  import recurso from '../recursos/api.json'

  const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
  };

  export default {
    data: function(){
      return {
          recurso: recurso
      }
    },
    methods: {
       mensaje(titulo, texto){
          setTimeout(function() {
              toastr.options = {
                  closeButton: true,
                  progressBar: true,
                  showMethod: 'slideDown',
                  timeOut: 4000
              };
              toastr.error(titulo, texto);
          }, 1300);
      },
      confirmar(){
        axios.delete('/pacientes/api/pacientes/' + this.paciente.id + '/')
        .then((response) => 
        {
           this.$emit('cargar');
           this.mensaje('', 'El Paciente se elimino con éxito');
           $('#paciente_eliminar').modal('hide');
        })
      }
    },
    props: [
      'paciente'
    ]
  }

</script>