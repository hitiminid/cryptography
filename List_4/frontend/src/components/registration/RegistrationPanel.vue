<template>
  <div class="registration-panel">
    <div class="registration-panel__wrapper">
      <div class="login100-form validate-form">
        <span class="registration-panel__title">Register</span>

        <div class="registration-panel__input-wrapper validate-input">
          <input
            v-model="email"
            class="registration-panel__input"
            type="text"
            name="email"
            v-validate="'required|email'"
            data-vv-delay="2000"
            :class="{ 'has-val' : !isEmailFieldEmpty}"
          >
          <span class="registration-panel__input-focus" data-placeholder="Email"></span>
        </div>

        <div class="registration-panel__error">
          <p v-show="errors.has('email')">{{ errors.first('email') }}</p>
        </div>

        <div
          class="registration-panel__input-wrapper validate-input"
          data-validate="Valid email is: a@b.c"
        >
          <input
            v-model="username"
            class="registration-panel__input"
            type="text"
            name="username"
            v-validate="'required|min:8'"
            :class="{ 'has-val' : !isUserNameFieldEmpty}"
          >
          <span class="registration-panel__input-focus" data-placeholder="Username"></span>
        </div>

        <div class="registration-panel__error">
          <p v-show="errors.has('username')">{{ errors.first('username') }}</p>
        </div>

        <div
          class="registration-panel__input-wrapper validate-input"
          data-validate="Enter password"
        >
          <span class="btn-show-pass">
            <i class="zmdi zmdi-eye"></i>
          </span>
          <input
            v-model="password"
            class="registration-panel__input"
            type="password"
            ref="password"
            v-validate="'required|min:8'"
            name="password"
            data-vv-delay="2000"
            :class="{ 'has-val' : !isPasswordFieldEmpty}"
          >
          <span class="registration-panel__input-focus" data-placeholder="Password"></span>
        </div>

        <div class="registration-panel__error">
          <p v-show="errors.has('password')">{{ errors.first('password') }}</p>
        </div>

        <div
          class="registration-panel__input-wrapper validate-input"
          data-validate="Enter password"
        >
          <span class="btn-show-pass">
            <i class="zmdi zmdi-eye"></i>
          </span>
          <input
            v-model="passwordConfirmation"
            class="registration-panel__input"
            type="password"
            name="passwordConfirmation"
            data-vv-as="password"
            v-validate="'required|confirmed:password'"
            :class="{ 'has-val' : !isPasswordConfirmationFieldEmpty}"
          >
          <span class="registration-panel__input-focus" data-placeholder="Password Confirmation"></span>
        </div>

        <div class="registration-panel__error">
          <p v-show="errors.has('passwordConfirmation')">{{ errors.first('passwordConfirmation') }}</p>
        </div>

        <div class="registration-panel__button-container">
          <div class="registration-panel__button-wrapper">
            <button
              @click="sendRegistrationRequest"
              class="registration-panel__button-inner"
            >Register</button>
          </div>
        </div>

        <div class="registration-panel__bottom-field">
          <span class="registration-panel__bottom-text">Already registered?</span>
          <router-link tag="a" to="/login" class="registration-panel__bottom-link">Sign in</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from "../../store/store";
// import router from "../../router/index";

// export default {
//   name: "RegistrationPanel",
//   data() {
//     return {
//       email: "",
//       username: "",
//       password: "",
//       passwordConfirmation: ""
//     };
//   },
//   methods: {
//     async sendRegistrationRequest() {
//       await this.validateBeforeSubmit();
//       if (store.getters.isUserLogged) {
//         // router.push({ name: "Home" });
//       }
//     },

//     async validateBeforeSubmit() {
//       const result = await this.$validator.validateAll();

//       if (result) {
//         await this.sendRegistrationData();
//         return true;
//       }
//       alert("Correct them errors!");
//       return false;
//     },

//     async sendRegistrationData() {
//       const userData = {
//         email: this.email,
//         username: this.username,
//         password: this.password
//       };
//       await store.dispatch("registerUser", userData);
//     }
//   },
//   computed: {
//     isEmailFieldEmpty() {
//       return this.email === "";
//     },
//     isUserNameFieldEmpty() {
//       return this.username === "";
//     },
//     isPasswordFieldEmpty() {
//       return this.password === "";
//     },
//     isPasswordConfirmationFieldEmpty() {
//       return this.passwordConfirmation === "";
//     }
//   }
// };
</script>

<style scoped lang="scss">
@import "../../assets/styles/mixins";
@import "../../assets/styles/variables";

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body,
html {
  height: 100%;
  font-family: Poppins-Regular, sans-serif;
}

.registration-panel {
  &__error {
    margin-bottom: 20px;
    font-size: 14px;
    color: red;
    padding: 0 4px;
  }

  .registration-panel__wrapper {
    @include box-shadow(0 5px 10px 0px rgba(0, 0, 0, 0.1));

    width: 390px;
    background: #fff;
    overflow: hidden;
    padding: 77px 55px 33px 55px;
  }

  a {
    font-size: 14px;
    line-height: 1.7;
    color: #666666;
    margin: 0;
    transition: all 0.4s;
    -webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;

    &:focus {
      outline: none;
    }

    &:hover {
      text-decoration: none;
      color: $secondary-purple;
    }
  }

  .registration-panel__bottom-field {
    padding-top: 50px;
    text-align: center;
  }

  p {
    font-size: 1rem;
    line-height: 1.7;
    margin: 0;
  }

  input {
    outline: none;
    border: none;

    &:focus {
      border-color: transparent;
    }
  }

  button {
    outline: none;
    border: none;

    &:hover {
      cursor: pointer;
    }
  }

  .registration-panel__bottom-text {
    font-size: 13px;
    color: #666666;
    line-height: 1.5;
  }

  .registration-panel__bottom-link {
    font-size: 13px;
    color: #333333;
    line-height: 1.5;
  }

  &__title {
    display: block;
    font-size: 30px;
    color: #333333;
    font-weight: bold;
    line-height: 1.2;
    text-align: center;
    margin-bottom: 30px;
  }

  .registration-panel__input-wrapper {
    width: 100%;
    position: relative;
    border-bottom: 2px solid #adadad;
    margin-bottom: 37px;
  }

  .registration-panel__input {
    font-size: 15px;
    color: #555555;
    line-height: 1.2;

    display: block;
    width: 100%;
    height: 45px;
    background: transparent;
    padding: 0 5px;
  }

  .registration-panel__input-focus {
    position: absolute;
    display: block;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    pointer-events: none;

    &::before {
      @include transition(all, 0.4s);
      background: $secondary-purple;

      content: "";
      display: block;
      position: absolute;
      bottom: -2px;
      left: 0;
      width: 0;
      height: 2px;
    }

    &::after {
      @include transition(all, 0.4s);
      font-size: 15px;
      color: #999999;
      line-height: 1.2;
      content: attr(data-placeholder);
      display: block;
      width: 100%;
      position: absolute;
      top: 16px;
      left: 0;
      padding-left: 5px;
    }
  }

  .registration-panel__input-focus::after {
  }

  .registration-panel__input:focus + .registration-panel__input-focus::after {
    top: -15px;
  }

  .registration-panel__input:focus + .registration-panel__input-focus::before {
    width: 100%;
  }

  .has-val.registration-panel__input + .registration-panel__input-focus::after {
    top: -15px;
  }

  .has-val.registration-panel__input
    + .registration-panel__input-focus::before {
    width: 100%;
  }

  .registration-panel__button {
    &-container {
      display: -webkit-box;
      display: -webkit-flex;
      display: -moz-box;
      display: -ms-flexbox;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      padding-top: 13px;
    }

    &-wrapper {
      width: 100%;
      display: block;
      position: relative;
      z-index: 1;
      overflow: hidden;
      margin: 0 auto;
    }

    &-background {
      position: absolute;
      z-index: -1;
      width: 300%;
      background: #371c57;
      &:hover {
        background: #57367e;
        @include transition(background-color, 0.3s, ease-out);
      }
    }

    &-inner {
      font-size: 15px;
      color: #fff;
      line-height: 1.2;
      text-transform: uppercase;
      display: -webkit-box;
      display: -webkit-flex;
      display: -moz-box;
      display: -ms-flexbox;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 0 20px;
      width: 100%;
      height: 50px;
    }
  }

  .registration-panel__button-wrapper:hover
    .registration-panel__button-background {
    left: 0;
  }

  &__button {
    &-container {
      display: -webkit-box;
      display: -webkit-flex;
      display: -moz-box;
      display: -ms-flexbox;
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      padding-top: 13px;
    }

    &-wrapper {
      width: 100%;
      display: block;
      position: relative;
      z-index: 1;
      overflow: hidden;
      margin: 0 auto;
    }

    &-inner {
      font-size: 15px;
      background: $main-purple;
      color: #fff;
      line-height: 1.2;
      text-transform: uppercase;
      display: -webkit-box;
      display: -webkit-flex;
      display: -moz-box;
      display: -ms-flexbox;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 0 20px;
      width: 100%;
      height: 50px;
      &:hover {
        @include transition(background-color, 0.3s, ease-out);
        background: $secondary-purple;
      }
    }
  }
}
</style>