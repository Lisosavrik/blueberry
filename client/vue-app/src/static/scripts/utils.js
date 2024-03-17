// function notify(msg, timeout) {
//     let notifyContainer = document.createElement("div");
//     notifyContainer.classList.add("notify-class");
//     notifyContainer.innerText = msg;
    
//     document.body.appendChild(notifyContainer);

//     setTimeout(() => {
//         notifyContainer.remove();
//     }, timeout);
// }

function redirectTo(location) {
    window.location.href = `http://127.0.0.1:8000/${location}`;
}

// function parseForm(formId, formValueIds, callback) {
//     $(`#${formId}`).on("submit", (event) => {
//         event.preventDefault();

//         const parsedVals = formValueIds.map((formVal) => {
//             return $(`#${formVal}`).val();
//         });

//         callback(...parsedVals);
//     })
// }
// /**
//  * @param {string} clickId
//  * @param {string[]} clickValIds
//  * @param {Function} callback
//  * @param {boolean} [clearInput=false]
//  */



// function parseClick({clickId, clickValIds, callback, clearInput, parent}) {
//     function lookForElement(elementId) {
//         if (parent) return parent.children(elementId)
//         return $(elementId)
//     }

//     if (clearInput === undefined) clearInput = false;
//     console.log(clickId, clickValIds)

//     lookForElement(`#${clickId}`).on("click", (event) => {
//         const parsedVals = clickValIds.map((clickVal) => {
//             const val = lookForElement(`#${clickVal}`).val();

//             lookForElement(`#${clickVal}`).val('');
            
//             return val;
            
//         });
//         callback(...parsedVals);
//     })
// }

// function initEnterEvent(fieldEnterId, buttonClickId){
//     $(`#${fieldEnterId}`).on("keypress", (event) =>{
//         let key = event.which;
//         if (key === 13) {
//             event.preventDefault(); 
//             $(`#${buttonClickId}`).click();
//         }
//     });
// }

export function randInt(a, b) {
    return a + Math.floor(Math.random() * (b - a + 1));
}
