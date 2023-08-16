function notify(msg, timeout) {
    let notifyContainer = document.createElement("div");
    notifyContainer.classList.add("notify-class");
    notifyContainer.innerText = msg;
    
    document.body.appendChild(notifyContainer);

    setTimeout(() => {
        notifyContainer.remove();
    }, timeout);
}

function redirectTo(location) {
    window.location.href = `http://127.0.0.1:8000/${location}`;
}

class ServerApi {
    get()
    post()
    delete()

    authenticateUser() {

    }
}