"use strict";

function  main() {
    parseForm("login_form", ["email-input",  "password-input"],  (login, password) => {
        ServerApi.login({
            loign:login, password: password, 
            successFunction: () => redirectTo("workspaces")
        }).fail((reason) => {
            console.log("could'nt log in:", reason);
            notify(`could'nt log in: ${reason}`, 1000);
        });
    })};


$(document).ready(main);