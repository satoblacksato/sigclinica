<template>
	<div>
	<div class="col-lg-12">
        <table class="table">
            <thead>
            <tr>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>Documento</th>
                <th>Nacimiento</th>
                <th>Acciones</th>
            </tr>
            </thead>
            <tbody>
            <template>	
                <tr v-for="paciente in pacientes">
                	<td>{{ paciente.nombre }}</td>
                    <td>{{ paciente.apellido }}</td>
                    <td>{{ paciente.documento }}</td>
                    <td>{{ paciente.edad }}</td>
                    <td><button @click="abrirDetalle(paciente)" type="button" class="btn btn-primary btn-sm"><i class="fa fa-eye"> Ver historial del paciente</i></button></td>
                </tr>
            </template>
            </tbody>
        </table>
            <diagnostico-detail :paciente="paciente_enviar"></diagnostico-detail>
    </div>
        <ul class="pager">
              <li v-if="g_previo" class="previous" @click="atras" ><a>&larr; Anterior</a></li>
              <li v-if="g_siguiente" class="next" @click="siguiente" ><a >Siguiente &rarr;</a></li>
        </ul>
   </div>     
</template>
<script>
    
    import {mapActions, mapGetters} from 'vuex'
    import diagnosticoDetail from './diagnosticoDetail.vue'

	export default{
		data(){
			return{
				paciente_enviar: ''
			}
		},
        methods: {
            ...mapActions(['cargarListado', 'siguientePaciente', 'previoPaciente']),
            abrirDetalle(paciente){
                this.paciente_enviar = paciente
                $('#historia_clinica_detail').modal();
            },
            siguiente(){
                this.siguientePaciente(this.g_siguiente)
            },
            atras(){
                this.previoPaciente(this.g_previo)
            }
        },
        mounted(){
            this.cargarListado();
        },
        computed: mapGetters(['pacientes', 'g_siguiente', 'g_previo']),
        components: {diagnosticoDetail}
	}
</script>