<template>
 <div class="ibox-content">
            
            <div class="row">
                <form @submit.prevent="buscar">
                    <div class="col-sm-5 m-b-xs"><select v-model="campo_buscar" class="input-sm form-control input-s-sm inline">
                       
                        <option value="apellido">Buscar por apellido</option>
                        <option value="nombre">Buscar por nombre</option>
                        <option value="documento">Buscar por documento</option>
                        <option value="obra_social">Buscar por obra social</option>

                    </select>
                    </div>
                    
                    <div class="col-sm-3">
                        <div class="input-group"><input v-model="valor_buscar" type="text" placeholder="Ingrese el texto a buscar" class="input-sm form-control"> <span class="input-group-btn">
                            <button type="submit" class="btn btn-sm btn-primary"> Buscar</button> </span></div>
                    </div>
                    <div class="col-sm-3">
                        <button type="button" data-toggle="modal" data-target="#paciente_form" class="btn btn-w-m btn-primary"><i class="fa fa-plus"></i> Nuevo</button>
                    </div>
                </form>    
            </div>
        <table class="table">
            <thead>
                <tr>
                    <th>Foto</th>
                    <th>#</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Edad</th>
                    <th>Documento</th>
                    <th>Obra Social</th>
                    <th>Nº de afiliado</th>
                    <th>Tel. Fijo</th>
                    <th>Tel. Celular</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="paciente in pacientes">
                    <td>
                        <template v-if="paciente.foto">
                            <a @click="detalle(paciente)"><img :src="paciente.foto" class="img-rounded" alt="Norway" height="42" width="42"></a>
                        </template>
                        <template v-if="!paciente.foto">
                            <a  @click="detalle(paciente)"><img src="/media/logos/paciente.png" class="img-rounded" alt="Norway" height="42" width="42"></a>
                        </template>
                    </td>
                    <td @click="detalle(paciente)"><p>{{ paciente.id }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.nombre }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.apellido }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.edad }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.documento }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.obra_social.descripcion }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.numero_afiliado }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.telefono_fijo }}</p></td>
                    <td @click="detalle(paciente)"><p>{{ paciente.telefono_celular }}</p></td>
                    <td><a class="btn btn-success btn-bitbucket" @click="editar(paciente)">
                        <i class="fa fa-edit"></i>
                        </a>
                        <a class="btn btn-danger btn-bitbucket" @click="eliminar(paciente)">
                        <i class="fa fa-trash"></i>
                        </a>
                    </td>
                </tr>
            </tbody>
            <!-- paginacion -->
              <ul class="pager">
                <li v-if="atras" class="previous"><a @click="paginaAtrasAsync"><span aria-hidden="true">&larr;</span> Atrás</a></li>
                <li v-if="siguiente" class="next"><a @click="paginaSiguienteAsync">Siguiente <span aria-hidden="true">&rarr;</span></a></li>
              </ul>
            <!-- paginacion -->
        </table>

        <paciente_form @cargar="cargarPacientesAsync"></paciente_form>
        <paciente_delete @cargar="cargarPacientesAsync" :paciente="paciente_enviar"></paciente_delete>
        <paciente_detail :paciente="paciente_enviar"></paciente_detail>
        <paciente_update @cargar="cargarPacientesAsync" :paciente="paciente_enviar"></paciente_update>

    </div> 

</template>
<script>
    import Vue from 'vue'
    import recurso from '../recursos/api.json'
    import paciente_form from './paciente_create.vue'
    import paciente_delete from './paciente_confirm_delete.vue'
    import paciente_detail from './paciente_detail.vue'
    import paciente_update from './paciente_update.vue'

    import {mapGetters, mapActions} from 'vuex'

    export default{
        data(){
            return {
                api: recurso,
                id_paciente: 0,
                paciente_enviar: [],
                campo_buscar: 'apellido',
                valor_buscar: ''
            }
        },
        methods: {
            ...mapActions(['cargarPacientesAsync', 'paginaSiguienteAsync', 'paginaAtrasAsync', 'buscarAsync']),
            detalle(paciente){
                this.paciente_enviar = paciente;
                $('#paciente_detail').modal();
            },
            eliminar(paciente){
                this.paciente_enviar = paciente;
                $('#paciente_eliminar').modal();
            },
            editar(paciente){
                this.paciente_enviar = paciente;
                $('#paciente_editar').modal();
            },
            buscar(){
                console.log(this.campo_buscar, this.valor_buscar);
                this.buscarAsync({campo: this.campo_buscar, valor: this.valor_buscar});
            }
        },
        mounted(){
            this.cargarPacientesAsync();
        },
        computed: mapGetters(['pacientes', 'siguiente', 'atras']),
        components: {
            'paciente_form': paciente_form,
            'paciente_delete': paciente_delete,
            'paciente_detail': paciente_detail,
            'paciente_update': paciente_update
        }
    }
</script>
