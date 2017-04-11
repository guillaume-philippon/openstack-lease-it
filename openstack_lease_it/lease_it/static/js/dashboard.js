function hypervisorsDetails() {
    var total_cpus = 0
    var free_cpus = 0
    var flavors = {};
    var div_flavors = '';

    return $.getJSON("/flavors", function(data) {
        var free = 0
        var max = 0
        data_sorted = sortOnKeys(data)
    }).then(function(){
        return data_sorted
    });
}

function buildCard(flavor, details) {
    html = '';
    // Size of card
    flavor_underscore = flavor.replace(/\./g,"");
    if (details.free != 0 ) {
        html += '<div class="col s12 m6 xl3">';
        html += '  <div class="card">';
        html += '    <div class="card-image waves-effect waves-block waves-light">';
        html += '      <div class="activator" id="' + flavor_underscore + '"></div>';
        html += '    </div>';
        html += '    <div class="card-content">';
        html += '      <span class="card-title activator">'
        html += flavor
        html += '       <i class="material-icons right">more_vert</i>';
        html += '      </span>';
        html += '    </div>';
        html += '    <div class="card-reveal">';
        html += '      <span class="card-title">'
        html += '      <i class="material-icons right">close</i>';
        html += '      </span>';
        html += '      <p>';
        html += '          CPU: ' + details.cpu + '<br/>';
        html += '          RAM: ' + details.ram / 1024 + ' GB<br/>';
        html += '          Disk: ' + details.disk + ' GB<br/>';
        html += '      </p>';
        html += '      </div>';
        html += '    </div>';
        html += '  </div>';
        html += '</div>';
    }
    return html;
}


function sortOnKeys(dict) {
    var sorted = [];
    for(var key in dict) {
        sorted[sorted.length] = key;
    }
    sorted.sort(function (a, b) {
        return a.toLowerCase().localeCompare(b.toLowerCase());
    });

    var tempDict = {};
    for(var i = 0; i < sorted.length; i++) {
        tempDict[sorted[i]] = dict[sorted[i]];
    }

    return tempDict;
}

function sortOnParams(params, dict, isReverse) {
    var sorted = [];
    for(var key in dict) {
        sorted[sorted.length] = dict[key];
    }
    sorted.sort(function (a, b) {
        if (isReverse) {
            return b[params].toLowerCase().localeCompare(a[params].toLowerCase());
        }
        else {
            return a[params].toLowerCase().localeCompare(b[params].toLowerCase());
        }
    });
    return sorted;
}
