<style scooped>
.vue-tooltip{background-color:#000;box-sizing:border-box;color:#fff;max-width:320px;padding:6px 10px;border-radius:3px;z-index:100;box-shadow:2px 2px 3px rgba(0,0,0,0.4)}.vue-tooltip .vue-tooltip-content{text-align:center}.vue-tooltip .tooltip-arrow{content:'';width:0;height:0;border-style:solid;position:absolute;margin:5px}.vue-tooltip[x-placement^="top"]{margin-bottom:5px}.vue-tooltip[x-placement^="top"] .tooltip-arrow{border-width:5px 5px 0 5px;border-top-color:#000;border-bottom-color:transparent !important;border-left-color:transparent !important;border-right-color:transparent !important;bottom:-5px;margin-top:0;margin-bottom:0}.vue-tooltip[x-placement^="bottom"]{margin-top:5px}.vue-tooltip[x-placement^="bottom"] .tooltip-arrow{border-width:0 5px 5px 5px;border-bottom-color:#000;border-top-color:transparent !important;border-left-color:transparent !important;border-right-color:transparent !important;top:-5px;margin-top:0;margin-bottom:0}.vue-tooltip[x-placement^="right"]{margin-left:5px}.vue-tooltip[x-placement^="right"] .tooltip-arrow{border-width:5px 5px 5px 0;border-right-color:#000;border-top-color:transparent !important;border-left-color:transparent !important;border-bottom-color:transparent !important;left:-5px;margin-left:0;margin-right:0}.vue-tooltip[x-placement^="left"]{margin-right:5px}.vue-tooltip[x-placement^="left"] .tooltip-arrow{border-width:5px 0 5px 5px;border-left-color:#000;border-top-color:transparent !important;border-right-color:transparent !important;border-bottom-color:transparent !important;right:-5px;margin-left:0;margin-right:0}
</style>

<template>
<div>
	<div class="row">
                <div class="col-lg-12">
                    <div class="ibox float-e-margins">
                        <div class="ibox-title">

                            <div class="ibox-tools">
                                <a class="collapse-link">
                                    <i class="fa fa-chevron-up"></i>
                                </a>
                                <a class="dropdown-toggle" data-toggle="dropdown" href="#">
                                    <i class="fa fa-wrench"></i>
                                </a>
                                
                                <a class="close-link">
                                    <i class="fa fa-times"></i>
                                </a>
                            </div>
                        </div>
                        <div class="ibox-content">
                            <!--<input type="text" class="form-control input-sm m-b-xs" id="filter"
                                   placeholder="Buscar en la tabla"> -->

                            <table class="footable table table-stripped" data-page-size="8" data-filter=#filter>
                                <thead>
                                <tr>
                                    <th>Turno Hora</th>
                                    <th>Nombre y Apellido</th>
                                    <th>Tipo Documento</th>
                                    <th>Documento</th>
                                    <th>Obra Social</th>
                                    <th>Edad</th>

                                    <th>Celular</th>
                                    <th>Teléfono Fijo</th>
                                    <th>Turno Día</th>
                                    
                                    <th>Atender</th>
                                </tr>
                                </thead>
                                <tbody>
                                <template v-for="turno in turnos_dias">    
                                    <tr v-tooltip.left="'El estado de este turno es: ' + turno.estado"  class="gradeX" :bgcolor='turno.backgroundColor'>
                                        <td>{{ turno.start|formatoHora }}</td>
                                        <td  v-text="turno.paciente.nombre + ' ' + turno.paciente.apellido"></td>
                                        <td  v-text="turno.paciente.tipo_documento"></td>
                                        <td  v-text="turno.paciente.documento"></td>
                                        <td  v-text="turno.paciente.obra_social.descripcion"></td>
                                        <td  v-text="turno.paciente.edad"></td>
                                        <td  v-text="turno.paciente.telefono_celular"></td>
                                        <td  v-text="turno.paciente.telefono_fijo"></td>
                                        <td>{{ turno.fecha|formatoFecha }}</td>
                                        <td><button @click="abrirFicha(turno)" class="btn btn-success">Abrir Ficha</button></td>
                                    </tr>
                                </template>
                                </tbody>
                                <tfoot>
                                <tr>
                                    <td colspan="5">
                                        <ul class="pagination pull-right"></ul>
                                    </td>
                                </tr>
                                </tfoot>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Trigger the modal with a button -->
            <fichas-clinicas :turno="paciente_enviar" @cargar="cargarTurnosDia" ></fichas-clinicas>
</div>
</template>
<script>
    import api from '../recursos/api.json'
    import axios from 'axios'
    import fichasClinicas from '../../fichasClinicas/componentes/form.vue'

    export default{
        data(){
            return {
                api: api,
                turnos_dias: [],
                paciente_enviar: []
            }
        },
        methods: {
            cargarTurnosDia(){
                axios.get(this.api.turnos_dia)
                .then((response) => this.turnos_dias = response.data)
            },
            abrirFicha(turno){
                this.paciente_enviar = turno;
                console.log(turno)
                console.log(this.paciente_enviar)
                $('#form_ficha_clinica').modal();
            }
        },
        mounted: function(){
            var self = this;
            self.cargarTurnosDia();
            setInterval(function(){
                self.cargarTurnosDia(); 
            }, 6000);
        },
        components: {
            fichasClinicas
        },
        filters: {
            formatoHora(value){      
                return value.split('T')[1].split(':')[0] + ':' + value.split('T')[1].split(':')[1]
            },
            formatoFecha(value){
                return value.split('-')[2] + '/' + value.split('-')[1] + '/' + value.split('-')[0]
            }
        }
    }
</script>