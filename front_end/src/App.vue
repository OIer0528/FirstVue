<template>
  <div>
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <el-button> {{ buttonName }} </el-button>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
  setup() {
    const buttonName = ref("");
    const getButtonName = async () => {
      buttonName.value = "BUTTON";
      axios
        .get("/api/getButtonName")
        .then((response) => (buttonName.value = response.data.name))
        .catch((error) => console.log(error));
    };
    onMounted(getButtonName);
    return {
      buttonName,
      getButtonName,
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
