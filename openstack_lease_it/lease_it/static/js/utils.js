/*
    Everyone say dictionary must not be ordered, everbody wants order dictionary until we found a answer,
    we sortOnKey and sortOnParams our dict.
*/
function sortOnParams(params, dict, isReverse) {
    var sorted = [];
    for(var key in dict) {
        sorted[sorted.length] = dict[key];
    }
    sorted.sort(function (a, b) {
        if ($.isNumeric(a[params])) {
            if (isReverse) {
                return b[params] - a[params];
            } else {
                return a[params] - b[params];
            }
        } else {
            if (isReverse) {
                return b[params].toLowerCase().localeCompare(a[params].toLowerCase());
            } else {
                return a[params].toLowerCase().localeCompare(b[params].toLowerCase());
            }
        }
    });

    var tempDict = {};
    for(var i = 0; i < sorted.length; i++) {
        tempDict[sorted[i].name] = dict[sorted[i].name];
    }
    return tempDict;
}

/*
    Notify user by a toast message and reload dataTables
*/
function notify(data) {
    var text = 'Default message',
        color;
    var datatables = [
        '#table-instances',
        '#table-admin-instances',
        '#table-admin-database'
    ];
    try {
        text = data.instance.name;
        if (typeof text === "undefined") {
            text = data.instance.id;
        }
    } catch(err) {
        text = data.message;
    }
    if (data.status == "success") {
        color = "teal";
    } else {
        color = "red";
    }
    for (let datatable=0; datatable < datatables.length; datatable++) {
        if ($(datatables[datatable]).length) {
            $(datatables[datatable]).DataTable().ajax.reload();
        }
    }
    Materialize.toast(text, 2000, color);
}