"use strict";

function authoriseUser(name, login, password) {
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:8000/api/sign_up',
        data: JSON.stringify({
            name: name,
            login: login,
            password: password
        }),
        success: (requestData, status) => {
            console.log({requestData});
            console.log({status});
            redirectTo("log_in");
        },
        contentType: "application/json",
        dataType: 'json'
    }).fail((reason) => {
        console.log("could'nt sign up:", reason);
        notify(`could'nt sign up: ${reason}`, 1000);
    });
}


function main() {
    parseForm(
        "cool-form",
        ["agreement-value", "name-field-value", "email_field_value", "password_field_value"],
        (agreed, name, login, password) => {
            if (!agreed) {
                notify("check the terms and conditions checkbox");
                return;
            };

            authoriseUser(name, login, password);
        }
    );
}

$(document).ready(main);