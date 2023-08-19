"use strict";

function  main() {
    parseForm("login_form", ["email-input",  "password-input"],  (login, password) => {
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/api/log_in',
            data: JSON.stringify({
                login: login,
                password: password
            }),
            success: (requestData, status) => {
                console.log({requestData});
                console.log({status});
                redirectTo("workspaces");
            },
            contentType: "application/json",
            dataType: 'json'
        }).fail((reason) => {
            console.log("could'nt log in:", reason);
            notify(`could'nt log in: ${reason}`, 1000);
        });
    })};


$(document).ready(main);