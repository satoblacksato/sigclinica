<template>
<div class="col-lg-6">
        <div class="ibox float-e-margins">
            <div class="ibox-title">
                <h5 v-text="titulo"></h5>
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
                <div class="row m-b-lg">
                    <div class="col-lg-12">
                        <div id="drag-fixed" class="slider_red"></div>
                    </div>
                </div>
                <div class="form-group">
                    <label class="font-normal">Nombre</label>
                    <div class="input-group date">
                        <span class="input-group-addon"><i class="fa fa-user"></i></span><input type="text" class="form-control" value="">
                    </div>
                </div>
                <div class="form-group">
                    <label class="font-normal">Apellido</label>
                    <div class="input-group date">
                        <span class="input-group-addon"><i class="fa fa-user"></i></span><input type="text" class="form-control" value="">
                    </div>
                </div>
                <div class="form-group">
                    <label class="font-normal">Tipo de Documento</label>
                    <div class="input-group date">
                        <span class="input-group-addon"><i class="fa fa-user"></i></span><input type="text" class="form-control" value="">
                    </div>
                </div>
                <div class="form-group">
                    <label class="font-normal">Documento</label>
                    <div class="input-group date">
                        <span class="input-group-addon"><i class="fa fa-user"></i></span><input type="text" class="form-control" value="">
                    </div>
                </div>
                <div class="form-group">
                    <label class="font-normal">Foto</label>
                    <div class="input-group date">
                        <span class="input-group-addon"><i class="fa fa-user"></i></span><input type="file" class="form-control" value="">
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import Vue from 'vue'

export default {
   data: function(){
       return {
           titulo: 'Cargar Datos Personales'
       }
   }
}
</script>
