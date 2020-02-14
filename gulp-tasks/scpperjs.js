import Scpper from "scpper.js";

const api = new Scpper({ site: "en" });

console.log(api.getPage("1956234"));