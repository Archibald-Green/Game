$(document).ready(function() {
    $("#loginInput").change(function(event) {
        var inputValue = event.target.value;
        var loginRegex = /^[a-zA-Z0-9]+$/;

        var loginValid = loginRegex.exec(inputValue);

        if (!loginValid){
            $("#loginInputError").removeClass("d-none");
        }
        else {
            $("#loginInputError").addClass("d-none");
        }
    })
    $("#passwordInput").change(function(event) {
        var inputValue = event.target.value;
    })
})