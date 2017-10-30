/*
    buildInstancesView create a full display of Instance on div_name
*/
function buildDatabaseView(div_name) {
    var table_columns = [
        { data: 'instance_id' },
        { data: 'heartbeat_at' },
        { data: 'leased_at' },
        { data: 'lease_end' }
    ];
    $('#table-' + div_name).DataTable({
        ajax: {
            url: '/database',
            dataSrc: function(instances) {
                return instances;
            }
        },
        columns: table_columns,
        lengthChange: false,
        pageLength: 25,
        columnDefs: [
            {
                targets: [0],
                render: function ( data, type, row ) {
                    var now = new Date()
                    var lease_end_date = new Date(row.lease_end)
                    if (lease_end_date < now) {
                        return '<i class="material-icons red-text">delete_forever</i>' +
                            formatText(data, MAX_STRING_LENGTH);
                    } else {
                        return formatText(data, MAX_STRING_LENGTH);
                    }
                }
            }],
        drawCallback: function(settings, json) {
            $(".tooltipped").tooltip();
        },
    });
}
