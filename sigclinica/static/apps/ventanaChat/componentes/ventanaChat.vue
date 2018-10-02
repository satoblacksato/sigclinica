<template>
	<div>
		<!--<div class="small-chat-box fadeInRight animated">

	                <div class="heading" draggable="true">
	                    <small class="chat-date pull-right">
	                        Conversación
	                    </small>
	                    Ventana Mínima
	                </div>

	                <div class="content">

	                    <div class="left">
	                        <div class="author-name">
	                            Monica Jackson <small class="chat-date">
	                            10:02 am
	                        </small>
	                        </div>
	                        <div class="chat-message active">
	                            Lorem Ipsum is simply dummy text input.
	                        </div>

	                    </div>
	                    <div class="right">
	                        <div class="author-name">
	                            Mick Smith
	                            <small class="chat-date">
	                                11:24 am
	                            </small>
	                        </div>
	                        <div class="chat-message">
	                            Lorem Ipsum is simpl.
	                        </div>
	                    </div>
	                    


	                </div>
	                <div class="form-chat">
	                    <div class="input-group input-group-sm">
	                        <input type="text" class="form-control">
	                        <span class="input-group-btn"> <button @click="enviarMensaje"
	                            class="btn btn-primary" type="button">Enviar
	                    </button> </span></div>
	                </div>

	            </div>
	            <div id="small-chat">

	                <span class="badge badge-warning pull-right">5</span>
	                <a class="open-small-chat">
	                    <i class="fa fa-comments"></i>

	                </a>
	            </div> -->
	    </div>        
</template>
<script>

	import Vue from 'vue'
	import {mapGetters} from 'vuex'
	//Vue.use(VueSocketIO);

	/*var server = app.listen(8810)
	var io = require('socket.io').listen(server);*/

	export default{
		data(){
			return{

			}
		},
		methods: {
			enviarMensaje(){
				console.log('apreto el enviar')
			}
		},
		computed: mapGetters(['usuario_seleccion'])
	}

	
</script>