<template>
	<div class="modal fade" id="nota_form" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="exampleModalLabel"><i class="fa fa-user"></i>  Nueva Nota</h4>
      </div>
      <div class="modal-body">
        <form @submit.prevent="guardar">
           <div class="row">
      <div class="col-md-6">
        <!-- control input -->
        <p><label for="recipient-name" class="control-label">Nota:</label>
            <p>  
              <input v-model="nota.nota" class="form-control" required="true" > 
            </p>
        </p>
        <!-- control input -->          
      </div>
      </div>
        <div class="modal-footer">
        <button type="button" class="btn btn-default" data-dismiss="modal">Salir</button>
        <button type="submit" class="btn btn-primary">Guardar</button>
      </div> 

        </form>
      </div>
      
    </div>
  </div>
</div>
</template>
<script>
  
  import {mapActions} from 'vuex'

	export default{
		data(){
			return{
        nota: {
          nota: ''
        }
			}
		},
    methods: {
      ...mapActions(['guardarNota']),
      guardar(){
        this.guardarNota(this.nota);
        console.log(this.nota)
      }
    }
	}
</script>