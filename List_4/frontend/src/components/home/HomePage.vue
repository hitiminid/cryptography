<template>
  <div class="home-page">
    <registration-page></registration-page>
    <login-page></login-page>
    <password-reset-page></password-reset-page>
  </div>
</template>

<script>
import RegistrationPage from "../registration/RegistrationPage";
import PasswordResetPage from "../password_reset/PasswordResetPage";
import LoginPage from "../login/LoginPage";

export default {
  name: "HomePage",
  components: {
    RegistrationPage,
    LoginPage,
    PasswordResetPage
  }
};
</script>

<style scoped lang="scss">
.home-page {
  width: 98vw;
  height: 98vh;
  background: #f1f1f1;
}
</style>