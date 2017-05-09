/*
  Define useful variable for flavor display
  * FLAVORS: list of flavors w/ there parameters
  * FLAVOR_SORT_PARAMS: Which parameter will be use to sort flavors
  * FLAVOR_MIN: Minimum value of free flavor available to be displayed
  * FLAVOR_DIV_NAME: The <div> section that will host view
*/
var FLAVORS = {};
var FLAVOR_SORT_PARAMS = 'free';
var FLAVOR_MIN = 0;
var FLAVOR_DIV_NAME = '#flavors-list';
var FLAVOR_ORDER = 1;
var FLAVOR_PARAMS_DESC = {
    'free': 'Free',
    'name': 'Name',
    'cpu': 'CPU',
    'ram': 'RAM',
    'disk': 'Disk',
    'max': 'Max'
};



function activeFlavorMenu() {
    var sort_css='';
    if (!FLAVOR_ORDER) {
        sort_css = 'bottom-up';
    }
    /* build refreshFlavorDiv call for active li */
    var onClick = 'refreshFlavorDiv(\'' + FLAVOR_SORT_PARAMS + '\', FLAVOR_MIN, ' + !(FLAVOR_ORDER) + ')';

    $('#'+FLAVOR_SORT_PARAMS).attr('onClick',onClick);
    return '<i class="material-icons sort-icon ' + sort_css + '">sort</i>';
}

/*
  Function to refresh the div name based on user input
*/
function refreshFlavorDiv(sort_params, min_value, sort_order) {
    /* Cleanup current selection */
    $("#"+FLAVOR_SORT_PARAMS).removeClass("active");
    $('#'+FLAVOR_SORT_PARAMS+'_desc').html(FLAVOR_PARAMS_DESC[FLAVOR_SORT_PARAMS]);

    /* Change global variable */
    FLAVOR_SORT_PARAMS = sort_params;
    FLAVOR_ORDER = sort_order;

    /* Active modification */
    $("#"+FLAVOR_SORT_PARAMS).addClass("active");
    $('#'+FLAVOR_SORT_PARAMS+'_desc').html(FLAVOR_PARAMS_DESC[FLAVOR_SORT_PARAMS] + activeFlavorMenu());
    FLAVOR_MIN = min_value;
    var sorted_data = sortOnParams(FLAVOR_SORT_PARAMS, FLAVORS, FLAVOR_ORDER);

    buildFlavorsView(sorted_data, FLAVOR_MIN, FLAVOR_DIV_NAME);
}
