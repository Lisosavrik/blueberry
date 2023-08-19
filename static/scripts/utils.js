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

function parseForm(formId, formValueIds, callback) {
    $(`#${formId}`).on("submit", (event) => {
        event.preventDefault();

        const parsedVals = formValueIds.map((formVal) => {
            return $(`#${formVal}`).val();
        });

        callback(...parsedVals);
    })
}
/**
 * @param {string} clickId
 * @param {string[]} clickValIds
 * @param {Function} callback
 * @param {boolean} [clearInput=false]
 */
function parseClick(clickId, clickValIds, callback, clearInput) {
    if (clearInput === undefined) clearInput = false;

    $(`#${clickId}`).on("click", (event) => {
        const parsedVals = clickValIds.map((clickVal) => {
            const val = $(`#${clickVal}`).val();
            $(`#${clickVal}`).val('');
            return val;
        });
        callback(...parsedVals);
    })
}

class ServerApi {

    get(url, callback, error)  {
        return $ajax({
            type: 'GET',
            url: url,
            success: callback
        }).fail(error);
    }

    post(url, callback, error) {
        return $ajax({
            type: 'POST',
            url: url,
            success: callback
        }).fail(error);
    }

    getTables(callback) {
        this.get("tables_url", callback, (error) => {
            notify(error);
        })
    }
}