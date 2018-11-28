$(function(){

    //sacar los mensajes de error
    $("errorcorreo").hide();
    $("errorrut").hide();
    $("errortelefono").hide();
 
    //variables que indican valor de estado validacion
    var error_correo = false;
    var error_rut = false;
    var error_telefono = false;
    
    //estas funciones llaman a las funciones de validacion cuando los campos son seleccionados y editados
    $("#errorcorreo").focusout(function() {
 
        check_correo();
         
    });
 
    $("#errorrut").focusout(function() {
 
        check_rut();
         
    });
 
    $("#errortelefono").focusout(function() {
 
        check_telefono();
         
    });
 
    // esta funcion determina que el correo sea valido
    function check_correo() {
 
        var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
     
        if(pattern.test($("#correo").val())) {
            $("#errorcorreo").hide();
        } else {
            $("#errorcorreo").html("Direccion inválida");
            $("#errorcorreo").show();
            error_correo = true;
        } 
    }
 
    // esta funcion valida el rut ingresado con la formula matematica de calculo de rut	
    function check_rut() {
     
        var rut_length = $("#rut").val().length;
        var rut= $('#rut').val().substring(0,$("#rut").val().length-2);
        var aux;
        var aux2;
        var save=rut;
        var veri= $('#rut').val().substring($("#rut").val().length-1,$("#rut").val().length);
        var final;
        var cont=0;
        var valor=0;
        var numero=0;
        for (var i =0;i<save.length;i++){
            if(cont==0){
                numero=2;
            }
            else if(cont==1){
                numero=3;
            }
            else if (cont==2){
                numero=4;
            }
            else if(cont==3){
                numero=5;
            }
            else if(cont==4){
                numero=6;
            }
            else if(cont==5){
                numero=7;
                cont=-1;
            }
            aux=rut.substring(rut.length-1,rut.length);
            valor=valor+aux*numero;
            cont=cont+1
            rut=rut.substring(0,rut.length-1);
        }
        aux=0;
        aux=Math.trunc(valor/11);
        aux2=valor-(11*aux);
        final=11-aux2;
        var veri_cal;
        if(final==10){
            veri_cal="k";
        }
        else if(final==11){
            veri_cal=0;
        }
        else{
            veri_cal=final;
        }
        //veri=toString(veri).toLowerCase();
        if( (rut_length>8 && rut_length<11) && (final>0 && final<12) && veri==veri_cal ) {
            $("#errorrut").hide();
        } else {
            $("#errorrut").html("rut invalido");
            $("#errorrut").show();
            error_rut = true;
        }


        error_rut=true;
    }
    //esta Funcion valida que el telefono este correctamente ingresado
    function check_telefono() {
     
        var tel = $("#telefono").val().length;
         
        if(tel < 9) {
            $("#errortelefono").html("minimo 9 caracteres");
            $("#errortelefono").show();
            error_telefono = true;
        } else {
            $("#errortelefono").hide();
        }
     
    }
    //Esta funcion envia si todos los campos fueron rellenados correctamente
    $("#registration_form").submit(function() {
 
        error_correo = false;									
        error_rut = false;
        error_telefono = false;
 
        check_correo();									
        check_rut();
        check_telefono();
         
        if(error_rut == false && error_telefono == false && error_correo == false) {
            return true;
        } else {
            return false;	
        }
    });
 });