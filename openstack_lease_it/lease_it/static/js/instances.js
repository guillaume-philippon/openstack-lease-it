/*
  Retrieve useful information about OpenStack
  a dictionnary of instances
   * Id of instance
   * User
   * Creation date
   * Last time we see the instance
   * Last lease date
   * Lease expiration
*/

/*
    buildInstancesView create a full display of Instance on div_name
*/
function buildInstancesView(div_name, get_option, show_user){
    table_columns = [
        { data: 'name' },
        { data: 'project' },
        { data: 'created_at' },
        { data: 'lease_end' }
    ];
    if (show_user) {
        table_columns.unshift({data: 'user'});
    }
    $('#table-' + div_name).DataTable({
        ajax: {
            url: '/instances?' + get_option,
            dataSrc: function(instances) {
                /* We add a lease button @ the end of the End Of Life line */
                for (instance=0; instance < instances.length; instance++) {
                    instances[instance].lease_end += '<span class="waves-effect waves-light ' +
                         ' new badge hoverable"' +
                         ' data-badge-caption="new lease" onClick="updateLease(\''+
                         instances[instance].id + '\')"></span>';
                }
                return instances;
            }
        },
        columns: table_columns,
        lengthChange: false,
        pageLength: 25
    });
    $( "#progress-bar-" + div_name ).hide();
}

/*
    Update lease status on click
*/
function updateLease(instance) {
    return $.getJSON("/instances/" + instance, function(data){
    }).success(function(data){
        var text,
            color;

        try {
            text = data.instance.name;
        } catch(err) {
            text = data.message;
        }
        if (data.status == "success") {
            color = "teal";
        } else {
            color = "red";
        }
        $('#table-instances').DataTable().ajax.reload();
        /* If table-admin-instances exist, we also update it. */
        if ( $('#table-admin-instances').length ) {
            $('#table-admin-instances').DataTable().ajax.reload();
        }
        Materialize.toast(text, 2000, color);
    });
}