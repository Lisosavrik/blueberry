"use strict";

let _workspaces = []
let _tables = []
let _cards = []


function UpdateWorkspaceUI() {
    $("#workspaces_table").empty();
    _workspaces.forEach(workspace => {
        let tablesTemplate = _tables[workspace.id].map(table => {
            let cardsTemplate = _cards[table.id].map(card => {
                return `<li><a>${card[1]}--${card[2]}</a></li>`
            }).join("\n")
            return `<li>
                        <ul>
                            <a>${table.name}</a>
                            ${cardsTemplate}
                        </ul>
                    </li>`
        }).join("\n");
        let template = $(`<ul>${workspace.name}
        ${tablesTemplate}</ul>`);

        template.appendTo("#workspaces_table");
    });
}

function  main() {
    initAddWorkspaceButton();
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000//api/user/get_workspaces_with_tables_and_cards',
        success: ({workspaces, tables, cards}) => {

            _workspaces = workspaces;
            _tables = tables;
            _cards = cards;

            UpdateWorkspaceUI();
        },
        contentType: "application/json",
        dataType: 'json'
    })
}

function addWorkspace(workspace_id, title) {
    let newWorkspace = {
        id: workspace_id,
        name: title
    };

    _workspaces.push(newWorkspace);
    _tables[newWorkspace.id] = [];
}

function initAddWorkspaceButton() {
    $("#add_workspace_field").on("x", (event) => {
        let key = event.which;
        if (key === 13) {
            event.preventDefault(); 
            $("#add_workspace_btn").click();
        }
    });


    parseClick("add_workspace_btn", ["add_workspace_field"], (title) => {
    $.ajax({
        type: "POST",
        url: 'http://127.0.0.1:8000//api/add_workspace',
        data: JSON.stringify({title: title}),
        success: ({workspace_id}, status) => {
            
            addWorkspace(workspace_id, title);
            UpdateWorkspaceUI();
        },
            contentType: "application/json",
            dataType: 'json',
        }).fail((reason) => {
            console.log("could'nt add workspace:", reason);
            alert("Workspace not added");
        })
    }, true)
}



$(document).ready(main);