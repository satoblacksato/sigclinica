<template>
	 <div class="ibox-content">
            
            <div class="row">
                <form>
                    <div class="col-sm-5 m-b-xs"><select class="input-sm form-control input-s-sm inline">
                       
                        <option value="apellido">Buscar por Notas</option>

                    </select>
                    </div>
                    
                    <div class="col-sm-3">
                        <div class="input-group"><input type="text" placeholder="Ingrese el texto a buscar" class="input-sm form-control"> <span class="input-group-btn">
                            <button type="submit" class="btn btn-sm btn-primary"> Buscar</button> </span></div>
                    </div>
                    <div class="col-sm-3">
                        <button @click="nuevaNota" type="button" data-toggle="modal" data-target="#paciente_form" class="btn btn-w-m btn-primary"><i class="fa fa-plus"></i> Nuevo</button>
                    </div>
                </form>    
            </div>
        <table class="table">
            <thead>
                <tr>
                	<th>#</th>
                    <th>Fecha</th>
                    <th>Nota</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="nota in notas">
                    <td>
                        <a><img src="/media/logos/notas.png" class="img-rounded" alt="Norway" height="42" width="42"></a>
                    </td>
                    <td><p>{{ nota.fecha | formatoFecha }}</p></td>
                    <td><p v-text="nota.nota"></p></td>
                    <td>
                        <a @click="eliminar(nota.id)" class="btn btn-danger btn-bitbucket">
                        <i class="fa fa-trash"></i>
                        </a>
                    </td>
                </tr>
            </tbody>
           <nota-alta></nota-alta>
        </table>
    </div> 
</template>

<script>
    
    import Vue from 'vue'

    import {mapGetters, mapActions} from 'vuex'
    import notaAlta from './nota_alta.vue'

    //Vue.filter()

	export default{
		data(){
			return{

			}
		},
        methods:{
            ...mapActions(['cargarNotas', 'eliminarNota']),
            nuevaNota(){
                $('#nota_form').modal();
            },
            eliminar(id){
                this.eliminarNota(id);
                this.cargarNotas();
            }
        },
        filters: {
            formatoFecha(value){
                let fechaSinFormato = value.toString();
                let fecha = fechaSinFormato.split('T')[0]
                return fecha.split('-')[2] + '/' + fecha.split('-')[1] + '/' + fecha.split('-')[0]
            }
        },
        mounted(){
            this.cargarNotas();
        },
        components:{
            notaAlta
        },
        computed: mapGetters(['notas'])
	}
</script>