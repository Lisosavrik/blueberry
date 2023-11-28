"use strict";

let _workspaces = []
let _tables = {}
let _cards = {}

function deleteWorkspace(workspaceEl, workspace) {
    workspaceEl.children(".delete-workspace-btn").on("click", () => {
        let successFunction = () => {
            const indexDeletedEl = _workspaces.indexOf(workspace);

            _workspaces.splice(indexDeletedEl, 1);
            // alert('done, workspace deleted');

            _tables[workspace.id].forEach(table => {
                delete _cards[table.id]
            })

            delete _tables[workspace.id]

            UpdateWorkspaceUI();
        }

        ServerApi.deleteWorkspace(workspace.id, successFunction).fail(() => {
            alert("workspace not deleted")
        });
    });
};

function deleteTable(tableEl, table) {
    tableEl.children("div").children(".delete-table-btn").on("click", () => {
        let successFunction = () => {
            _tables[table.workspace_id] = _tables[table.workspace_id].filter(el => {
                return el.id !== table.id
            });

            delete _cards[table.id]
            // alert("done");
            UpdateWorkspaceUI()
        }

        ServerApi.deleteTable({ tableId: table.id, successFunction })
            .fail(() => { alert("not delete") });
    });
};

function deleteCard(cardEl, card) {
    cardEl.children(".delete-card-btn").on("click", () => {
        let successFunction = () => {
            _cards[card.table_id] = _cards[card.table_id].filter(el => {
                return el.id !== card.id
            });
            UpdateWorkspaceUI()
        };
        ServerApi.deleteCard(card.id, successFunction).fail(() => {
            alert("not delete")
        });
    });
};

function createWorkspaceUI(workspace) {
    let workspaceEl = $(`
    <ul>
        <p>${workspace.name}</p>
    </ul>

    <input  id="table-input-${workspace.id}">
    <button id="add-table-btn-${workspace.id}">Add Table</button>
    <div>
        <button class="delete-workspace-btn"> Delete WS </button>
        <button class="edit-workspace-btn"> Edit WS </button>
    </div>
    `)
    deleteWorkspace(workspaceEl, workspace)
    return workspaceEl
}

function createTableUI(table) {
    let tableEl = $(
        `<li>
            <ul>
                <a>${table.name}</a>                       
            </ul>

            <input id="key-input-${table.id}">
            <input id="value-input-${table.id}">
            <button id="add-card-btn-${table.id}">Add card</button>
            <div>
                <button class="delete-table-btn"> Delete </button>
                <button class="edit-table-btn"> Edit </button>
            </div>
        </li>`)

    deleteTable(tableEl, table);
    return tableEl;
};

function createCardUI(card) {
    let cardEl = $(
        `<li>
            <a>${card.key}--${card.value}</a>
            <button class="delete-card-btn"> Delete C</button>
            <button class="edit-card-btn">Edit C</button>
        </li>`)
    deleteCard(cardEl, card)
    return cardEl;
}

function UpdateWorkspaceUI() {
    $("#workspaces_table").empty();

    _workspaces.forEach(workspace => {
        const workspaceEl = createWorkspaceUI(workspace)
        const workspaceListEl = workspaceEl[0];
        console.log(workspaceListEl);
        _tables[workspace.id].forEach(table => {
            const tableEl = createTableUI(table)
            const tableListEl = tableEl.children()

            _cards[table.id].forEach(card => {
                const cardEl = createCardUI(card);
                cardEl.appendTo(tableListEl[0]);
            })

            initAddCardButton(table.id, tableEl);
            tableEl.appendTo(workspaceListEl);
        })
        workspaceEl.appendTo("#workspaces_table")
        console.log(_tables)

        initAddTableButton(workspace.id);
    });
}

function addWorkspace(workspace_id, title) {
    let newWorkspace = {
        id: workspace_id,
        name: title
    };

    _workspaces.push(newWorkspace);
    _tables[newWorkspace.id] = [];
}

function addTable(table_id, workspace_id, title) {
    let newTable = {
        id: table_id,
        name: title,
        workspace_id: workspace_id
    };

    _tables[workspace_id].push(newTable);
    _cards[newTable.id] = []
}

function addCard(card_id, key, value, today, tableId) {
    let newCard = {
        id: card_id,
        key: key,
        value: value,
        training_day: today,
        color: "red",
        next_well: 3,
        next_v_vell: 5,
        table_id: tableId
    }

    _cards[tableId].push(newCard)
}

function showWorkspacesTablesCards() {
    let successFunction = ({ workspaces, tables, cards }) => {

        _workspaces = workspaces;
        _tables = tables;
        _cards = cards;

        UpdateWorkspaceUI();
    };

    ServerApi.getAlldata({ successFunction: successFunction })
}

function initAddWorkspaceButton() {
    $("#add_workspace_field").on("keypress", (event) => {
        let key = event.which;
        if (key === 13) {
            event.preventDefault();
            $("#add_workspace_btn").click();
        }
    });

    parseClick({
        clickId: "add_workspace_btn",
        clickValIds: ["add_workspace_field"],
        clearInput: true,

        callback: (title) => {
            let successFunction = ({ workspace_id }) => {
                addWorkspace(workspace_id, title);
                UpdateWorkspaceUI();
            }

            ServerApi.addWorkspace({
                title: title, successFunction: successFunction
            }).fail((reason) => {
                alert("Workspace not added");
            })
        }
    })
}


function initAddTableButton(workspaceId) {
    initEnterEvent(`table-input-${workspaceId}`, `add-table-btn-${workspaceId}`);

    parseClick({
        clickId: `add-table-btn-${workspaceId}`,
        clickValIds: [`table-input-${workspaceId}`],
        clearInput: true,

        callback: (title) => {
            let successFunction = ({ table_id }) => {
                addTable(table_id, workspaceId, title);
                UpdateWorkspaceUI();
            }

            ServerApi.addTable({
                title: title,
                workspaceId: workspaceId,
                successFunction: successFunction
            }).fail(() => {
                alert("table not added");
            });
        }
    })
}

function initAddCardButton(tableId, tableEl) {
    setTimeout(() => {
        initEnterEvent(`key-input-${tableId}`, `add-card-btn-${tableId}`)
        initEnterEvent(`value-input-${tableId}`, `add-card-btn-${tableId}`)
        parseClick({
            clickId: `add-card-btn-${tableId}`,
            clickValIds: [`key-input-${tableId}`, `value-input-${tableId}`],
            clearInput: true,
            parent: tableEl,

            callback: (key, value) => {

                let successFunction = ({ card_id, today }) => {
                    addCard(card_id, key, value, today, tableId);
                    UpdateWorkspaceUI();
                }

                ServerApi.addCard({
                    key: key,
                    value: value,
                    tableId: tableId,
                    successFunction: successFunction
                }).fail(() => {
                    alert("card not added");
                });
            }
        });
    }, 0);
}



function main() {
    initAddWorkspaceButton();
    showWorkspacesTablesCards();

}

$(document).ready(main)