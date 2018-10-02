<template>
	   <div class="row">
        <div class="col-lg-12">

                <div class="ibox chat-view">

                    <div class="ibox-title">
                        <small class="pull-right text-muted"></small>
                         Chat room panel
                    </div>


                    <div class="ibox-content">

                        <div class="row">
                        <nav aria-label="...">
                              <ul class="pager">
                                <li><a href="#">Ver Mensajes Anteriores</a></li>
                              </ul>
                            </nav>
                            <div class="col-md-9 ">
                                <div class="chat-discussion">
                                    
                                    <template v-for="mensaje in mensajes">
                                    <!-- mensajes de chat -->
                                    <div class="chat-message right ">
                                        <div class="message ">
                                            <a class="message-author" href="#" v-if="mensaje.emisor != null" v-text="mensaje.emisor.username"> </a>
                                            <span class="message-date" v-text="mensaje.fecha + ' ' + mensaje.hora "> </span>
                                            <span class="message-content " v-text="mensaje.mensaje">
											 
                                            </span>
                                        </div>
                                    </div>  
                                     <!-- mensajes de chat -->
                                     </template>

                                </div>

                            </div>



                            <div class="col-md-3">
                                <div class="chat-users">


                                    <div class="users-list">
                                        <template v-for="usuario in usuarios">
                                            <div class="chat-user">
                                                <i class="fa fa-user-circle fa-3x" aria-hidden="true"></i>
                                                <div class="chat-user-name">
                                                    <a @click="seleccionUsuario(usuario)" v-text="usuario.username"></a>
                                                </div>
                                            </div>
                                        </template>

                                    </div>

                                </div>
                            </div>

                        </div>
                        <div class="row">
                            <div class="col-lg-12">

                                <div class="chat-message-form">
                                    <form @submit.prevent="guardar">
                                        <div class="form-group">
                                            <textarea v-model="mensaje" class="form-control message-input" name="message" placeholder="Ingrese su mensaje aquí"></textarea>
                                            <div class="form-group">
                                                
                                            <button type="submit" class="btn btn-info btn-lg" >Enviar</button>
                                            </div> 
                                        </div>
                                    </form>
                                       <br><br><br> 
                                </div>
                            </div>
                        </div>


                    </div>

                </div>
        </div>

    </div>

</template>

<script>
    import {mapGetters, mapActions} from 'vuex'

    import ventanaChat from '../../ventanaChat/componentes/ventanaChat.vue'

	export default{
		data(){
			return{
                mensaje: ''	
			}
		},
        methods: {
            ...mapActions(['cargarMensajes', 'guardarMensaje', 'cargarUsuarios']),
            guardar(){
                this.guardarMensaje(this.mensaje);
                this.mensaje = '';
            },
            seleccionUsuario(usuario){
                this.$store.commit('seleccionUsuario', usuario)
            }
        },
        components: {
            ventanaChat
        },
        mounted(){
            var self = this;
            self.cargarMensajes();
            self.cargarUsuarios();
            setInterval(function(){
                self.cargarMensajes();
                //self.$toast.success({
                //    title:'Sistema',
                //    message:'Tiene Mensajes sin leer !'
                //})
            }, 6000);
        },
        computed: mapGetters(['mensajes', 'usuarios'])
	}
</script>
