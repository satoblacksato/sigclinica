<template>
	<div class="col-lg-9">
        <div class="ibox float-e-margins">
            <div class="ibox-title">
                <h5>Calendario </h5>
                <div class="ibox-tools">
                    <a class="collapse-link">
                        <i class="fa fa-chevron-up"></i>
                    </a>
                    <a class="close-link">
                        <i class="fa fa-times"></i>
                    </a>
                </div>
            </div>
            <div class="ibox-content">
                <div id="calendar"></div>
            </div>
            <estado></estado>
        </div>
    </div>
</template>

<script>

	import Vue from 'vue'
    import estado from './estado_turno.vue'

    
	 $(document).ready(function() {

        /* initialize the external events
         -----------------------------------------------------------------*/


        $('#external-events div.external-event').each(function() {

            // store data so the calendar knows to render an event upon drop
            $(this).data('event', {
                title: $.trim($(this).text()), // use the element's text as the event title
                stick: true // maintain when user navigates (see docs on the renderEvent method)
            });

            // make the event draggable using jQuery UI
            $(this).draggable({
                zIndex: 1111999,
                revert: true,      // will cause the event to go back to its
                revertDuration: 0  //  original position after the drag
            });

        });


        /* initialize the calendar
         -----------------------------------------------------------------*/
        var date = new Date();
        var d = date.getDate();
        var m = date.getMonth();
        var y = date.getFullYear();

        $('#calendar').fullCalendar({
            events: '/turnos/api/turnos/',
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay'
            },
            buttonText: {
                prev: 'Previo',
                next: 'Siguiente',
                today: 'Hoy',
                month: 'Mes',
                week: 'Semana',
                day: 'día'
            },
            monthNames: ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],
            monthNamesShort: ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'],
            dayNames: ['Domingo','Lunes','Martes','Miércoles','Jueves','Viernes','Sábado'],
            dayNamesShort: ['Dom','Lun','Mar','Mié','Jue','Vie','Sáb'],
            editable: false,
            droppable: false, // this allows things to be dropped onto the calendar
            drop: function() {
                // is the "remove after drop" checkbox checked?
                if ($('#drop-remove').is(':checked')) {
                    // if so, remove the element from the "Draggable Events" list
                    $(this).remove();
                }
            },
            dayClick: function(date, allDay, jsEvent, view) {
                $('#calendar').fullCalendar('changeView', "agendaDay");
                //$('#calendar') 
                //    .fullCalendar('changeView', 'agendaDay'/* or 'basicDay' */) 
                //    .fullCalendar('gotoDate', date.getFullYear(), date.getMonth(), date.getDate());*/
                },
             eventClick: function(calEvent, jsEvent, view) {
                $('#form_estados').modal('show');
                $("#form_estados .modal-title").html("Cambiar estados del turno");
                $("#form_estados .clase_turno").val(calEvent.id);

                // change the border color just for fun
                $(this).css('border-color', 'red');

            }    
        });


    });


	export default{
		data: function(){
			return{
				
			}
		},
        methods: {
            prueba(){
                console.log('******************************************');
                console.log('******************************************');
            }
        },  
        components:{
            estado
        }
	}
</script>