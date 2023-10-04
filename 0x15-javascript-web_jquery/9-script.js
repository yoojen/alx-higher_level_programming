const $ = window.$;
$.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", {hello: "any"})
    .done(function(jsondata){
        $("DIV#hello").text(jsondata.hello)
    })
