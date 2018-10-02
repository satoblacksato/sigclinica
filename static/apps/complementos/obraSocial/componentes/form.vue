<template>
  <div class="modal fade" id="obra_social_form" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel"><i class="fa fa-user"></i> Nueva Obra Social</h4>
      </div>
      <div class="modal-body">
        <form method="post" @submit.prevent="guardar">
           <div class="row">
              <div class="col-md-6">
                <input type="text" name="descripcion" v-model="modelo.descripcion" class="form-control" >
              </div>
              </div>
                <div class="modal-footer">
                <button type="submit" class="btn btn-primary">Guardar</button>
              </div> 
        </form>
      </div>
      
    </div>
  </div>
</div>
</template>
<script>

  import modelo from '../recursos/modelo.json'
  import api from '../recursos/api.json'
  import axios from 'axios'

  const config = {
      headers: {
          'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
      }
  };

  export default {
    data: function(){
      return {
        modelo: modelo,
        api: api
      }
    },
    methods: {
      guardar(){
        axios.post(this.api.obrasocial, this.modelo, config)
        .then((response) => 
        {
          this.mensaje('', 'La obra social se guardo de forma correcta');
          this.$emit('cargar');
          $('#obra_social_form').modal('hide');
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
    components: {
    },
  }

</script>