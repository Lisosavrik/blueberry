// function main(){
//     reguest = $.get("sign_up.html", dataType="json")

//     $.post("sign_up.html")
// }


// $(document).ready(main())

"use strict";

function authoriseUser(name, login, password) {
    // Create an XMLHttpRequest object
    const request = new XMLHttpRequest();

    // Define a callback function
    request.onload = function() {
        redirectTo("tables");
    }

    // Send a request
    request.open("POST", "http://127.0.0.1:8000/api/sign_up", true);
    request.setRequestHeader("Content-type", "application/json");
    request.send(JSON.stringify({
        name: name,
        login: login,
        password: password
    }));
}


function main() {
    const formEl = document.getElementById("cool-form");
    formEl.addEventListener("submit", (event) => {
        // Prevent default behaviour -> reloading the page
        event.preventDefault();
    
        // Check if user agreed to terms and conditions
        const agreed = document.getElementById("agreement-value").value;
        if (!agreed) {
            notify("check the terms and conditions checkbox");
            return;
        };
    
        const name = document.getElementById("name-field-value").value;
        const login = document.getElementById("email_field_value").value;
        const password = document.getElementById("password_field_value").value;
    
        authoriseUser(name, login, password);
    });
}

$(document).ready(main);