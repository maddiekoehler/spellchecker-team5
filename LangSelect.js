$(function () {
    let lang = localStorage.getItem("appLang");
    let lng = "";
    if (lang === "English") {
      lng = "en";
    } else if (lang === "Irish") {
      lng = "ir";
    } else if (lang === "Spanish") {
      lng = "es";
    } else {
      lng = "en";
    }
    $("#main_app").multilang({
      defaultLang: lng,
      menu: false,
    });
  });
  
  function changeLanguage(event) {
    if (typeof Storage !== "undefined") {
      localStorage.setItem("appLang", event.value);
    } else {
      console.log("web storage is not supported.");
    }
    let lng = "";
    if (event.value === "English") {
      lng = "en";
    } else if (event.value === "Irish") {
      lng = "ir";
    } else if (event.value === "Spanish") {
      lng = "es";
    } else {
      lng = "en";
    }
    $("#main_app").multilang({
      defaultLang: lng,
      menu: false,
    });
  }