<template>
  <div>
    <router-view/>
  </div>
</template>

<script>
import HomePage from "./components/home/HomePage";

export default {
  name: "app",
  data() {
    return {};
  },
  components: {
    HomePage
  }
};
</script>

<style lang="scss">
</style>
