<template>
  <div class="home">
    <b-carousel
      id="carousel-1"
      
      :interval="4000"
      controls
      indicators
    
    >
      <b-carousel-slide>
        <b-card slot="img" alt="image slot" img-blank img-alt="Card image">
          <img src="../../static/mercadilibre.jpg" />
        </b-card>
      </b-carousel-slide>
       <b-carousel-slide>
        <b-card slot="img" alt="image slot" img-blank img-alt="Card image">
          <img src="../../static/carosuel1.jpg" />
        </b-card>
      </b-carousel-slide>
      
    </b-carousel>

    <Cartas></Cartas>
    <router-view />
  </div>
</template>
<script>
import Cartas from "@/components/Cartas.vue";
import Navbar from "@/components/Navbar.vue";
import Footer from "@/components/Footer.vue";

import axios from "axios";
const MockAdapter = require("axios-mock-adapter");

import { mapGetters, mapMutations } from "vuex";

export default {
  name: "home",
 
  components: {
    Cartas,
    Navbar,
  
  },
  computed: {
    ...mapGetters(["getProducts", "profile"]),
    traerProducts() {
      return this.getProducts;
    }
  },
  methods: {
    ...mapMutations(["setProducts", "setCount", "setPhone", "setTelevisores"]),
    getProductos() {
      const path = "http://localhost:8000/traeRopa/";
      axios
        .get(path)
        .then(response => {
          this.setProducts(response.data);

          // alert(this.getProducts[0].productos.nombre_producto)
          //alert(this.profile.first_name)
        })
        .catch(err => {
          console.log(err);
        });
    },
    getProducts2() {
      this.$store
        .dispatch("api_trae")
        .then(res => {
          this.setCount(res.data);
        })
        .catch(err => {
          alert(err);
        });
    },
    getProducts3() {
      this.$store.dispatch("api_trea_phone").then(res => {
        this.setPhone(res.data);
      });
    },
    getProducts4() {
      this.$store.dispatch("api_trea_tele").then(res => {
        this.setTelevisores(res.data);
      });
    }
  },
  created() {
    this.getProductos();
    this.getProducts2();
    this.getProducts3();
    this.getProducts4();
  }
};
</script>
<style>
#prehome {
  background-color: black;
  width: 2000px;
  height: 400px;
}
</style>
