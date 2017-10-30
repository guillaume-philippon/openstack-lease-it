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
                targets: [0, 1, 2],
                render: function ( data, type, row ) {
                        return formatText(data, MAX_STRING_LENGTH);
                }
            }],
        drawCallback: function(settings, json) {
            $(".tooltipped").tooltip();
        },
    });
}
