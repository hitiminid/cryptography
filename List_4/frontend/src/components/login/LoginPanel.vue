<template>
    <div class="login-panel">
        <div class="login-panel__wrapper">
            <div class="login100-form validate-form">
                <span class="login-panel__title">
                    Welcome
                </span>

                <div class="login-panel__input-wrapper validate-input">
                    <input
                            v-model="username"
                            class="login-panel__input"
                            type="text"
                            name="username"
                            v-validate="'required'"
                            :class="{ 'has-val' : !isUserNameFieldEmpty}">
                    <span class="login-panel__input-focus" data-placeholder="Username"></span>
                </div>

                <div class="login-panel__error">
                    <p v-show="errors.has('username')">{{ errors.first('username') }}</p>
                </div>

                <div class="login-panel__input-wrapper validate-input" data-validate="Enter password">

                    <span class="btn-show-pass">
                        <i class="zmdi zmdi-eye"></i>
                    </span>

                    <input
                            v-model="password"
                            class="login-panel__input"
                            type="password"
                            name="password"
                            v-validate="'required'"
                            :class="{ 'has-val' : !isPasswordFieldEmpty}">
                    <span class="login-panel__input-focus" data-placeholder="Password"></span>
                </div>

                <div class="login-panel__error">
                    <p v-show="errors.has('password')">{{ errors.first('password') }}</p>
                </div>

                <div class="login-panel__button-container">
                    <div class="login-panel__button-wrapper">
                        <div class="login-panel__button-background"></div>
                        <button
                                @click="sendLoginRequest"
                                class="login-panel__button-inner">
                            Login
                        </button>
                    </div>
                </div>

                <div class="login-panel__bottom-field">
                    <span class="login-panel__bottom-text">
                        Don’t have an account?
                    </span>
                    <router-link
                            tag="a"
                            to="/register"
                            class="login-panel__bottom-link">
                        Sign Up
                    </router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

  import store from '../../store/store';
  import router from '../../router/index';
  // todo: icon

  export default {
    name: "LoginPanel",
    data() {
      return {
        username: '',
        password: ''
      };
    },
    computed: {
      isUserNameFieldEmpty() {
        return this.username === '';
      },
      isPasswordFieldEmpty() {
        return this.password === '';
      }
    },
    methods: {
      async sendLoginRequest() {
        await this.validateBeforeSubmit();
        if (store.getters.isUserLogged) {
          router.push({name: 'Home'})
        }
      },

      async validateBeforeSubmit() {
        const result = await this.$validator.validateAll();
        if (result) {
          const loginData = {
            username: this.username,
            password: this.password
          };
          await store.dispatch('performUserLogin', loginData);
          return true;
        }
        return false;
      }
    }
  }
</script>

<style scoped lang="scss">

    @import '../../assets/styles/variables';
    @import '../../assets/styles/mixins';



    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body, html {
        height: 100%;
        font-family: Poppins-Regular, sans-serif;
    }

    .login-panel {

        &__wrapper {
            width: 390px;
            background: #fff;
            /*border-radius: 10px;*/
            overflow: hidden;
            padding: 77px 55px 33px 55px;
            box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.1);
            -moz-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.1);
            -webkit-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.1);
            -o-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.1);
            -ms-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.1);
        }

        a {
            /*font-family: Poppins-Regular;*/
            font-size: 14px;
            line-height: 1.7;
            color: #666666;
            margin: 0;
            transition: all 0.4s;
            -webkit-transition: all 0.4s;
            -o-transition: all 0.4s;
            -moz-transition: all 0.4s;

            &:focus {
                outline: none !important;
            }

            &:hover {
                text-decoration: none;
                color: $main-purple;
            }
        }

        &__bottom-field {
            padding-top: 50px;
            text-align: center;
        }

        p {
            font-size: 14px;
            line-height: 1.7;
            margin: 0;
        }

        &__error {
            margin-bottom: 20px;
            font-size: 14px;
            color: red;
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

        &__bottom-text {
            font-size: 13px;
            color: #666666;
            line-height: 1.5;
        }

        &__bottom-link {
            font-size: 13px;
            color: magenta;
            line-height: 1.5;
        }

        .login100-form {
            width: 100%;
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

        &__input-wrapper {
            width: 100%;
            position: relative;
            border-bottom: 2px solid #adadad;
            margin-bottom: 40px;
        }

        &__input {
            font-size: 15px;
            color: #666666;
            line-height: 1.2;
            display: block;
            width: 100%;
            height: 45px;
            background: transparent;
            padding: 0 5px;
        }

        &__input-focus {
            position: absolute;
            display: block;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            pointer-events: none;

            &::before {
                content: "";
                display: block;
                position: absolute;
                bottom: -2px;
                left: 0;
                width: 0;
                height: 2px;
                -webkit-transition: all 0.4s;
                -o-transition: all 0.4s;
                -moz-transition: all 0.4s;
                transition: all 0.4s;
                background: $secondary-purple;
            }

            &::after {
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

                -webkit-transition: all 0.4s;
                -o-transition: all 0.4s;
                -moz-transition: all 0.4s;
                transition: all 0.4s;
            }
        }

        &__input-focus::after {

        }

        &__input:focus + &__input-focus::after {
            top: -15px;
        }

        &__input:focus + &__input-focus::before {
            width: 100%;
        }

        .has-val.login-panel__input + .login-panel__input-focus::after {
            top: -15px;
        }

        .has-val.login-panel__input + .login-panel__input-focus::before {
            width: 100%;
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
                    background: $secondary-purple;
                    @include transition(background-color, 0.3s, ease-out);
                }
            }
        }
    }
</style>