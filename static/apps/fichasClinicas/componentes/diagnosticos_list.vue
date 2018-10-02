<template>
    <div>
	<div class="col-lg-12">
        <table class="table">
            <thead>
            <tr>
                <th>#</th>
                <th>Fecha</th>
                <th>Motivo de Consulta</th>
                <th>Antecedentes</th>
                <th>Diagnóstico</th>
                <th>Tratamiento</th>
            </tr>
            </thead>
            <tbody>
            <template v-for="ficha in fichas">	
                <tr>
                	<td v-text="ficha.id" ></td>
                    <td >{{ ficha.fecha | formato_fecha }}</td>
                    <td v-text="ficha.motivo_consulta"></td>
                    <td v-text="ficha.antecedentes_enfermedad"></td>
                    <td v-text="ficha.diagnostico"></td>
                    <td v-text="ficha.tratamiento"></td>
                </tr>
            </template>
            </tbody>
        </table>
   
    </div>
        <ul class="pager">
              <li class="previous" v-if="atras"><a @click="paginaAtras">&larr; Anterior</a></li>
              <li class="next" v-if="siguiente"><a @click="paginaSiguiente">Siguiente &rarr;</a></li>
        </ul>
   </div>     
</template>

<script>
    import axios from 'axios'
    

    const config = {
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        }
    };

	export default{
		data(){
			return{
                fichas: [],
                siguiente: '',
                atras: ''
			}
		},
        methods: {
            cargarFichas(){
                axios.get('/historia/clinica/api/historia_clinica/' + '?paciente=' + this.turno.paciente.id, config)
                .then((response) => 
                {
                    this.fichas = response.data.results;
                    this.siguiente = response.data.next;
                    this.atras = response.data.previous;
                })
            },
            paginaSiguiente(){
                console.log('aca viene');
                 axios.get(this.siguiente, config)
                .then((response) => 
                {
                    console.log(response)
                    this.fichas = response.data.results;
                    this.siguiente = response.data.next;
                    this.atras = response.data.previous;
                })
            },
            paginaAtras(){
                axios.get(this.atras, config)
                .then((response) => 
                {
                    this.fichas = response.data.results;
                    this.siguiente = response.data.next;
                    this.atras = response.data.previous;
                })
            }
        },
        mounted(){
            this.paciente;
            this.cargarFichas();
        },
        props: {
            turno: {
                required: true
            }
        },
        watch: {
            'turno': function(){
               this.cargarFichas();
            }
        },
        filters: {
          formato_fecha(value) {
                console.log(value)
                console.log(value.split('-')[2] + '/' + value.split('-')[1] + '/' + value.split('-')[0])
                return value.split('-')[2] + '/' + value.split('-')[1] + '/' + value.split('-')[0]
          }
        }
	}
</script>