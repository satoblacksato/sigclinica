<template>
	<div class="col-lg-6">
    <div class="ibox float-e-margins">
        <div class="ibox-title">
            <h5>Lista de Obra Sociales </h5>
            <div class="ibox-tools">
                 <p>
                    <button type="button" data-toggle="modal" data-target="#obra_social_form" class="btn btn-w-m btn-primary"><i class="fa fa-plus"></i> Nuevo</button>
                </p>    
            </div>
        </div>
        <div class="ibox-content">

            <table class="table table-bordered">
                <thead>
                <tr>
                    <th>#</th>
                    <th>Descripción</th>
                    <th>Acción</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="obra_social in obra_sociales">
                    <td v-text="obra_social.id"></td>
                    <td v-text="obra_social.descripcion"></td>
                    <td>
                        <a class="btn btn-danger btn-bitbucket" @click="eliminar(paciente.id)">
                        <i class="fa fa-trash"></i>
                        </a>
                    </td>
                </tr>
                </tbody>
            </table>
            <formObra @cargar="cargar"></formObra>
        </div>
    </div>
 </div>   
</template>
<script>

    import axios from 'axios'
    import formObra from './form.vue'

    import {mapGetters, mapActions} from 'vuex'

	export default{
		data(){
			return {

			}
		},
        methods: {
            ...mapActions(['cargar'])
        },
        mounted(){
            this.cargar();
        },
        components: {
            formObra
        },
        computed: mapGetters(['obra_sociales'])
	}
</script>