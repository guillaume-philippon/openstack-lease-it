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
function instancesStatus() {
    return $.getJSON("/instances", function(data) {
        return data;
    });
}

/**/
function buildInstanceView(instance, details) {
    return '<tr>' +
           '<td>' + details.name + '</td>' +
           '<td>' + details.project_id + '</td>' +
           '<td>' + details.created_at + '</td>' +
           '<td>' + details.lease_end + '<span class="waves-effect waves-light new badge hoverable"' +
                                 '      data-badge-caption="new lease"></span>' +
           '</td>' +
           '</tr>';
}

/*
    buildInstancesView create a full display of Instance on div_name
*/
function buildInstancesView(instances, div_name){
    $(div_name).html('');
    $.each(instances, function(instance, details){
        $(buildInstanceView(instance, details)).appendTo(div_name);
    });
}