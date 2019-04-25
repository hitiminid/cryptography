import axios from "axios";
import Cookies from "js-cookie";

let HTTP = axios.create({
  // headers: {},
  baseURL: "http://127.0.0.1:8000/", // todo: there might be a problem with CORS
  timeout: 30000 // TODO: this might be a problem
});

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

const csrftoken = Cookies.get("csrftoken");
console.log("CSRF TOKEN:\t\t" + csrftoken);

export default HTTP;
