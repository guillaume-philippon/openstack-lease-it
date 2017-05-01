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
