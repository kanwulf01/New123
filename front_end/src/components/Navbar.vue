<template >

<div id="navbarx">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<nav class="navbar navbar-expand-lg navbar-dark bg-info">
  <a class="navbar-brand" href="/">NEUROMARKET</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="#">Opciones</a>
      </li>
     
       <li class="nav-item dropdown">
         
       <b-form-select v-model="selected" :options="this.categorias"  @change="getProductos()"  class="nav-item"  >
                  <!-- This slot appears above the options from 'options' prop -->
                  <template slot="first" style="background-color:black;">
                    <option :value="null" disabled style="background-color:black; "><strong>Categorias</strong></option>
                    
                  </template>
                </b-form-select>   
      </li>
     
     
       <form class="form-inline my-2 my-lg-0" v-on:submit.prevent="claveproductos()">
      <input class="form-control mr-sm-2" type="search" v-model="clave" placeholder="Que estas buscando?" aria-label="">
      <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Buscar</button>
    </form>
     
       <li class="nav-item">
        
        
      </li>
       <li class="nav-item right" v-if="this.TraeNombre">
        <a></a>
      
      </li>
      <li class="nav-item" v-else>
          <a class="nav-link" href="r" >Registrarse</a>
      </li>
     <li class="nav-item" v-if="this.TraeNombre">
       <a class="nav-link" href="carrito"> Shopping<i class="fas fa-cart-plus size:5x" size:5x id="carrito"></i></a>
      
     </li>
     
       <li class="nav-item right" v-if="this.TraeNombre">
        
       <strong> <a class="nav-link" href="profile" >{{profile.first_name}}</a></strong>
      </li>
      <li class="nav-item" v-if="this.TraeNombre">
        <a class="nav-link" href="vende">Vender</a>
      </li>
      <li class="nav-item" v-if="this.TraeNombre">
        <button class="nav-link btn btn-primary" @click="deleteUser()"><i class="fas fa-sign-out-alt"></i></button>
      </li>
      <li class="nav-item" v-else>
        <a class="nav-link" href="login" >Login</a>
      </li>
     
    </ul>
   
  </div>
    

</nav>

</div>

</template>

<script>


import Cartas from '@/components/Cartas.vue'
import sawl from 'sweetalert'
import { mapGetters, mapMutations} from 'vuex'
import axios from "axios";


export default {

  data(){
    return{
      categorias:[],
      selected: null,
      clave:null
    }
  },
components:{
  Cartas,
 
},methods:{
...mapMutations([
  'setFieldProfilename',
   'setCategorias',
   'setInfo',
   'setCarritox',
   'setFUllsaldo',
   'BorraElementoCarrito',
   'BorraCantidades',
   'setUsername',
   "BorraCompletoCantidades",
   "setCantidadActual"
   
  
   

]),deleteUser: function(){
   this.restauraCantidadesenBasedatos()
    this.setFieldProfilename("");
    this.setFUllsaldo(0);
    this.setUsername("")
    this.setCantidadActual("")
    //Aca borrar producto, carrito de compras y detalles ESTO PRODUCE UN ERROR DE LAS CANTIDADES DESCONTADAS DE LA BASE DE DATOS
    
   
  
  
   
    this.BorraCompletoCantidades([])
     //debo crear un metodo que me restaura los valores de las cantidad de los productos seleccionadas cuando se cierre sesion
    for(let i=0; i<this.getCarrito.length; i++ ){
       this.BorraElementoCarrito(i)// aca lo borra
    }
   
    sawl('Usted cerro su sesion','','success')
    this.$router.push({path: '/'});
        },
          getCategorias(){
      const path =  'http://localhost:8000/api/v1.0/categoria/'
      axios.get(path).then((response)=>{
          this.categorias = [];             
          this.setCategorias(response.data)
          for (var i = response.data.length - 1; i >= 0; i--) {
            var categoria = { value: response.data[i].id_categoria, text: response.data[i].nombre_categoria };
            this.categorias.push(categoria);
          
          }
          console.log(this.categorias)
      }).catch((err)=>{
          console.log(err)
          
      })
  },
  getProductos(){
  
    const path = 'http://localhost:8000/buscaCate/'+this.selected+'/'
    axios.get(path).then((res=>{
      this.setInfo(res.data)
      this.$router.push({path: '/busqueda'})
       

    }))
  },
  claveproductos(){
    
    if(this.clave !=null){
      this.$store.dispatch('B_P',this.clave)
      .then(res=>{
        if(res.data!="No"){this.$router.push({path: '/busqueda'})
        this.setInfo(res.data)}else{sawl('No se encontro el producto','','error')}
        this.clave="";
      })
    }else{swal('Ingrese un nombre de producto','','error')}
  },borraTodo(){
        this.setCarritox("");
      },
      restauraCantidadesenBasedatos(){
//debo hacer un for que me busque si hay elementos en el carrito de compras, si no hay elementos no debo restaurar 
//nada, si hay algun elemento, eso quiere decir que no elimino algun elemento del carrito por ende debo
//buscar en el arreglo de cantidad y id dle producto contra carrito para restaurar el producto del carrito que no elimino
// del carrito de compras

    if(this.getCarrito.length == 0){//no haga nada}
    }
    else{
      for(let i= 0; i<this.getCarrito.length;i++){

         this.getCantidadSeleccionada.forEach(element => {alert(element.id_producto + ""+this.getCarrito[i].productos.id_producto)
           if(element.id_producto==this.getCarrito[i].productos.id_producto){// si se cumple es porque dejo elementos sin borrar en carrito
      //debo hacer una peticion por cada id y cantidad que esta en el arreglo de objtos, getCantidadesSeleccioanda
    //con el fin de restuarar esa cantidad si la persona cierra sesion sin haber eliminado productso del carrito
    this.$store.dispatch('restauraCantidad',element)
    .then(res=>{
      alert("success")
    })
           }else{}
   
  });
}

      }

    }
 
},created(){
  this.getCategorias()
  
},

computed:{
...mapGetters([
  'profile',
  'getInfo',
  'getCarrito',
  'getDetails',
  "getCarrito",
  
  'getCantidadSeleccionada'



]),
  TraeNombre(){
    if(this.profile.first_name==""){
      return false
    }else{return true}
    
},
 
  
  /*
 this.$store.dispatch('Pro_cate',this.selected)
 .then(res=>{
   alert(res.data)
 }).catch(err => {
          alert(err)
        })*/


}}

</script>

<style scoped>

#navbarx{
    position: fixed;
    top: 0%;
    left: 0;
    width: 100%;
}
/* adds some margin below the link sets  */
.navbar .dropdown-menu div[class*="col"] {
   margin-bottom:1rem;
}

.navbar .dropdown-menu {
  border:none;
  background-color:black!important;
}

/* breakpoint and up - mega dropdown styles */
@media screen and (min-width: 600px) {
  
  /* remove the padding from the navbar so the dropdown hover state is not broken */
.navbar {
  padding-top:0px;
  padding-bottom:0px;
}

/* remove the padding from the nav-item and add some margin to give some breathing room on hovers */
.navbar .nav-item {
  padding:.5rem .5rem;
  margin:0 .25rem;
  color:black
}

/* makes the dropdown full width  */
.navbar .dropdown {position:static;}

.navbar .dropdown-menu {
  width:100%;
  left:0;
  right:0;
/*  height of nav-item  */
  top:45px;
  
  display:block;
  visibility: hidden;
  opacity: 0.9;
  transition: visibility 0s, opacity 0.3s linear;
  
}
  
 

  
  /* shows the dropdown menu on hover */
.navbar .dropdown:hover .dropdown-menu, .navbar .dropdown .dropdown-menu:hover {
  display:block;
  visibility: visible;
  opacity: 2;
  transition: visibility 0s, opacity 0.3s linear;
}
  
  .navbar .dropdown-menu {
    border: 1px solid rgba(0,0,0,.15);
    background-color: #fff;
  }

}

a{
color:black
}


</style>
