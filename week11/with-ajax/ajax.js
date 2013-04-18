var doGet = function (query) {
    var xhr = new XMLHttpRequest(),
        result = document.getElementById("result");
     
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function () {
        if (xhr.readyState !== 4) {
            return;
        }
         
        result.innerHTML = xhr.responseText;    // HTML FTW
    };
    xhr.send("query=" + query);
}
 
window.onload = function () {
    var submit = document.getElementById("submit"),
        query = document.getElementById("query");
     
    submit.onclick = function () {
        doGet(query.value);
        return false;
    };
};
