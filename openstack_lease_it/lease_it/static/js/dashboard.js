/*
  Retrieve useful information about OpenStack
  a dictionnary of flavor and for each flavor
   * CPU allocated by flavor
   * RAM allocated by flavor
   * Disk allocated by flavor
   * Total VM w/ this flavor that can be run on Cloud
   * Maximum VM w/ this flavor that can be run on Cloud if it s empty
*/
function openstackStatus() {
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

/*
    Each flavor information is disabled by a materializeCSS card buildCard
    build a div contain all information for a specific flavor w/ its specific
    details (CPU / RAM / Disk / Free / Max)
*/
function buildCard(flavor, details) {
    html = '';
    // Size of card
    flavor_underscore = flavor.replace(/\./g,"");
    if (details.free != 0 ) {
        html += '<div class="col s12 m6 l4 xl3"';
        html += '     data-name="' + flavor_underscore + '"';
        html += '     data-cpu="' + details.cpu + '"';
        html += '     data-ram="' + details.ram + '"';
        html += '     data-disk="' + details.disk + '"';
        html += '     data-free="' + details.free + '"';
        html += '     data-max="' + details.max + '"';
        html += '>';
        html += '  <div class="card hoverable">';
        html += '    <div class="card-image activator">';
        html += '      <div class="activator" id="' + flavor_underscore + '"></div>';
        html += '    </div>';
        html += '    <div class="card-content">';
        html += '      <span class="card-title activator">'
        html += flavor
        html += '       <i class="material-icons right">more_vert</i>';
        html += '      </span>';
        html += '    </div>';
        html += '    <div class="card-reveal">';
        html += '      <span class="card-title">' + flavor
        html += '      <i class="material-icons right">close</i>';
        html += '      </span>';
        html += '      <ul class="collection">';
        html += '          <li class="collection-item"><div><span class="badge">' + details.cpu + '</span>CPU</div></li>';
        html += '          <li class="collection-item"><div><span class="badge">' + details.ram + ' MB</span>RAM</div></li>';
        html += '          <li class="collection-item"><div><span class="badge">' + details.disk + ' GB</span>Disk</div></li>';
        html += '      </ul>';
        html += '      <ul class="collection">';
        html += '          <li class="collection-item"><div><span class="badge">' + details.free + '</span>Flavor Available</div></li>';
        html += '          <li class="collection-item"><div><span class="badge">' + details.max + '</span>Maximum Flavor</div></li>';
        html += '      </ul>';
        html += '      </div>';
        html += '    </div>';
        html += '  </div>';
        html += '</div>';
    }
    return html;
}

/*
    Everyone say dictionary must not be ordered, everbody wants order dictionary until we found a answer,
    we sortOnKey and sortOnParams our dict.
*/
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
