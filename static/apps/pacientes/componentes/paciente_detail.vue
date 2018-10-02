<template>
  <div class="modal fade" id="paciente_detail" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel"><i class="fa fa-user"></i>  Detalle del Paciente</h4>
      </div>
      <div class="modal-body">
        <form method="post">
      <div class="wrapper wrapper-content">
            <div class="row animated fadeInRight">
                
                <div class="col-md-12">
                    <div class="ibox float-e-margins">
                        <div class="ibox-content">
                            <div>
                                <template v-if="paciente.foto" >
                                    <img alt="image" class="img-circle" height="82" width="82" :src="paciente.foto">
                                </template>
                                <template v-if="!paciente.foto" >
                                    <img alt="image" class="img-circle" height="82" width="82" src="/media/logos/paciente2.jpg">
                                </template>
                                <div class="feed-activity-list">
                                    <div class="feed-element">
                                        <div class="media-body ">
                                            <strong>{{ paciente.nombre }}</strong> {{ paciente.apellido }}  <strong>{{ paciente.documento }}</strong><br>
                                            <div class="well">
                                                Teléfono Fijo: {{ paciente.telefono_fijo }}
                                            </div>
                                            <div class="well">
                                                Teléfono Celular: {{ paciente.telefono_celular }}
                                            </div>
                                            <div class="well">
                                                Observación: {{ paciente.observacion }}
                                            </div>
                                            <div class="well">
                                                Domicilio : {{ paciente.domicilio }}
                                            </div>
                                        </div>
                                    </div>
                                </div>                               

                            </div>

                        </div>
                    </div>

                </div>
            </div>
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
  import modelo from '../recursos/modelo.json'
  import recurso from '../recursos/api.json'
  import tipo_documento from '../recursos/tipo_documento.json'
  import Dropzone from 'vue2-dropzone'
  import vSelect from "vue-select"
  import VeeValidate from 'vee-validate';


  const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
  };

  Vue.use(VeeValidate);

  export default {
    data: function(){
      return {
        
      }
    },
    props: [
        'paciente'
    ]
  }

</script>