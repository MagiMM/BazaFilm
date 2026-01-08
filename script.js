function addMovie() {
    var movieTitle  = document.getElementById("inputTitle").value;
    var movieYear   = document.getElementById("inputYear").value;
    var movieActors = document.getElementById("inputActors").value;

    console.log(movieTitle);
    console.log(movieYear);
    console.log(movieActors);

    if (!movieTitle || !movieYear || !movieActors) {
        alert("Uzupełnij wszystkie pola!");
        return;
    }

    var li = document.createElement("li");
    li.className = "movie-item";
    li.innerHTML = "<label><input type='checkbox'>"
                   + movieTitle + ", " + movieYear + ", " + movieActors + "</label>";

    document.getElementById("moviesList").appendChild(li);
    document.getElementById("inputTitle").value  = "";
    document.getElementById("inputYear").value   = "";
    document.getElementById("inputActors").value = ""; 
}

function deleteMovies() {
    var checkedBoxes = document.querySelectorAll("input[type='checkbox']:checked");
    console.log("checkedBoxes:", checkedBoxes);
    for (var i = 0; i < checkedBoxes.length; i++) {
        document.getElementById("moviesList")
                .removeChild(checkedBoxes[i].parentNode.parentNode);
    }
}