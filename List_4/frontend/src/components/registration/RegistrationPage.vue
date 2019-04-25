<template>
  <div class="registration-page">
    <div class="registration-page__content">
      <div>
        <!--REGISTER-->
        <h1>Register</h1>
        <p>Mail:</p>
        <input class type="text" name="email" placeholder="Mail">

        <p>Password</p>
        <input class type="text" name="email" placeholder="Password">
        <p></p>
        <button @click="performRegister">Register</button>
      </div>
    </div>
  </div>
</template>

<script>
import httpService from "../../services/httpService.js";

export default {
  name: "RegistrationPage",
  components: {},
  methods: {
    performRegister() {
      alert("Register");
    }
  }
};
</script>

<style scoped lang="scss">
.registration-page {
  width: 100%;
  height: 40%;
  margin: 0 auto;

  &__content {
    width: 100%;
    min-height: 30vh;
    display: -webkit-box;
    display: -webkit-flex;
    display: -moz-box;
    display: -ms-flexbox;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    padding: 15px;
    background: #f1f1f1;
  }
}
</style>