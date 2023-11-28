"use strict";

// function getEmailVarificationWindow(code){
//     $("#cool-form").css("display", "none");
//     $("#emailVarification").css("display",  "block");
//     parseClick({
//         clickId: "emailVarificationBtn",
//         clickValIds: ["emailVarificationInput"],
//         clearInput: true,
//         callback: (user_code)=> {
//             if (user_code === code){
//                 alert("Code is right");
//                 return true;
//             }
//             else{
//                 alert("Not right")
//             }
//             }
//         });
    
//     }

// function sendVerificationMsg(login){
//     let code = randInt(1000, 9999);
//     Email.send({
//         Host: "smtp.gmail.com",
//         Username: "Blueberry",
//         Password: "bluemory310352",
//         To: login,
//         From: "blueberryplatform0.0@gmail.com",
//         Subject: "Sending Email using javascript",
//         Body: ` Your code is ${code}`
//     }).then(function (message) {
//         alert("mail sent successfully")})
//         console.log(login)
//         getEmailVarificationWindow(code)
//     }


function main() {
    parseForm(
        "cool-form",
        ["agreement-value", "name-field-value", "email_field_value", "password_field_value"],
        (agreed, name, login, password) => {
            if (!agreed) {
                return;
            };
            ServerApi.signup({
                name: name,
                login: login,
                password: password, 
                successFunction: () => redirectTo("have_to_confirm")
            }).fail((reason) => {
                console.log("could'nt sign up:", reason);
            });
        });
    }


$(document).ready(main);