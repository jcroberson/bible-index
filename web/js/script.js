document.querySelector('.search_button').onclick = function() {
    eel.my_func(document.querySelector("input").value, document.querySelector("select").value)(function(result){
        console.log('Searched')
        document.querySelector(".display").innerHTML = result;
        document.querySelector(".display").style.display = "grid";
    })
}