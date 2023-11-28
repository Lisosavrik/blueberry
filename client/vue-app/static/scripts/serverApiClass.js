"use strict";

const my_api = "http://127.0.0.1:8000"
class _ServerApi {
    
    get({url, successFunction}){
        return $.ajax({
            type: "GET",
            url: url,
            success: successFunction,
            contentType: "application/json",
            dataType: 'json'
        });
    }

    post({url, data, successFunction}){
        return $.ajax({
            type: 'POST',
            url: url,
            data: JSON.stringify(data),
            success: successFunction, 

            contentType: "application/json",
            dataType: 'json',
        });
    }

    delete({url, successFunction}){
        return $.ajax({
            type: "DELETE",
            url: url,
            success: successFunction,
            contentType: "application/json",
            dataType: 'json'
        });
    }
    
    login({login, password, successFunction}) {
        return this.post({
            url: my_api + "/api/log_in", 
            data: {login: login, password: password}, 
            successFunction: successFunction
        });
    }

    signup({name, login, password, successFunction }) {
        return this.post({
            url: my_api + "/api/sign_up",
            data: {
                name: name,
                login: login,
                password: password
            },
            successFunction: successFunction
        });
    }
    getAlldata({successFunction}){
        return this.get({
            url: my_api + "/api/user/get_workspaces_with_tables_and_cards",
            successFunction: successFunction
        });
    }

    addWorkspace({title, successFunction}){
        return this.post({
            url: my_api + "/api/add_workspace",
            data: {title: title},
            successFunction: successFunction,
        });
    }

    addTable({title, workspaceId, successFunction}){
        return this.post({
            url: my_api + "/api/add_table",
            data: {title: title, workspace_id: workspaceId},
            successFunction: successFunction
        });
    }

    addCard({key, value, tableId, successFunction}){
        return this.post({
            url: my_api + "/api/add_card",
            data:{
            key: key,
            value: value,
            table_id: tableId
            },
            successFunction: successFunction
        });
    }

    deleteWorkspace(workspaceId, successFunction) {
        return this.delete({
            url: my_api + `/api/workspace/delete/${workspaceId}`,
            successFunction: successFunction
        });
    }

    deleteTable({tableId, successFunction}) {
        return this.delete({
            url: my_api + `/api/tables/delete/${tableId}`,
            successFunction: successFunction
        });
    }
    deleteCard(cardId, successFunction){
        console.log(cardId)
        return this.delete({
            url: my_api + `/api/cards/delete/${cardId}`,
            successFunction: successFunction
        });
    }
}

const ServerApi = new _ServerApi();