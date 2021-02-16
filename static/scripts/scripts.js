if (localStorage.getItem("localStyleSelection") === null) {
    localStorage.setItem("localStyleSelection", "/static/styles/light.css")
}

selectedStyle = localStorage.getItem("localStyleSelection")

function changeTheme(value) {
    var stylesheet = document.getElementById("stylesheet")
    stylesheet.href = value
    localStorage.setItem("localStyleSelection", value)
}

changeTheme(selectedStyle)