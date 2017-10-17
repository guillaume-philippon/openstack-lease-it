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
function buildInstancesView(div_name, get_option){
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
        columns: [
            { data: 'name' },
            { data: 'project' },
            { data: 'created_at' },
            { data: 'lease_end' }
        ]
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
            color,
            type;

        try {
            text = data.instance.name;
        } catch(err) {
            text = data.message;
        }
        if (data.status == "success") {
            color = "teal-text";
            type = "check";
        } else {
            color = "red-text";
            type = "clear";
        }
        $('#table-instances').DataTable().ajax.reload();
        Materialize.toast(text + ' <i class="material-icons tiny ' + color + '">' + type + '</i>',
         1000, 'rounded');
    });
}