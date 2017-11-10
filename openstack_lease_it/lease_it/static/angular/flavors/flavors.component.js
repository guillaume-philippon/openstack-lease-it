angular.module('leaseItFlavors').
    component('leaseItFlavors', {
        templateUrl: 'flavors/flavors.template.html',
        controller: function leaseItFlavors ($scope) {
            this.flavors = {
                'os.12': {
                    name: "os.12",
                    max: 151,
                    ram: 24576,
                    free: 8,
                    disk: 20,
                    cpu: 12
                },
                'm1.small': {
                    name: "m1.small",
                    max: 1669,
                    ram: 2048,
                    free: 281,
                    disk: 15,
                    cpu: 1
                },
                'os.10': {
                    name: "os.10",
                    max: 183,
                    ram: 20480,
                    free: 10,
                    disk: 20,
                    cpu: 10
                },
                'os.11': {
                    name: "os.11",
                    max: 164,
                    ram: 22528,
                    free: 8,
                    disk: 20,
                    cpu: 11
                },
                'os.16': {
                    name: "os.16",
                    max: 106,
                    ram: 32768,
                    free: 7,
                    disk: 20,
                    cpu: 16
                },
                'os.17': {
                    name: "os.17",
                    max: 93,
                    ram: 34816,
                    free: 6,
                    disk: 20,
                    cpu: 17
                },
                'os.14': {
                    name: "os.14",
                    max: 127,
                    ram: 28672,
                    free: 8,
                    disk: 20,
                    cpu: 14
                },
                'os.15': {
                    name: "os.15",
                    max: 127,
                    ram: 30720,
                    free: 8,
                    disk: 20,
                    cpu: 15
                },
                'os.30': {
                    name: "os.30",
                    max: 45,
                    ram: 61440,
                    free: 2,
                    disk: 20,
                    cpu: 30
                },
                'os.31': {
                    name: "os.31",
                    max: 45,
                    ram: 63488,
                    free: 1,
                    disk: 20,
                    cpu: 31
                },
                'os.32': {
                    name: "os.32",
                    max: 37,
                    ram: 65536,
                    free: 1,
                    disk: 20,
                    cpu: 32
                },
                'os.19': {
                    name: "os.19",
                    max: 82,
                    ram: 38912,
                    free: 3,
                    disk: 20,
                    cpu: 19
                },
                'os.18': {
                    name: "os.18",
                    max: 82,
                    ram: 36864,
                    free: 5,
                    disk: 20,
                    cpu: 18
                },
                'm1.large': {
                    name: "m1.large",
                    max: 378,
                    ram: 8192,
                    free: 48,
                    disk: 60,
                    cpu: 4
                },
                'x3550.whole': {
                    name: "x3550.whole",
                    max: 217,
                    ram: 15000,
                    free: 14,
                    disk: 95,
                    cpu: 8
                },
                'os.8': {
                    name: "os.8",
                    max: 244,
                    ram: 16384,
                    free: 18,
                    disk: 20,
                    cpu: 8
                },
                'os.9': {
                    name: "os.9",
                    max: 209,
                    ram: 18432,
                    free: 14,
                    disk: 20,
                    cpu: 9
                },
                'c6320.whole': {
                    name: "c6320.whole",
                    max: 11,
                    ram: 94000,
                    free: 0,
                    disk: 800,
                    cpu: 48
                },
                'os.1': {
                    name: "os.1",
                    max: 1459,
                    ram: 2048,
                    free: 256,
                    disk: 20,
                    cpu: 1
                },
                'os.2': {
                    name: "os.2",
                    max: 871,
                    ram: 4096,
                    free: 132,
                    disk: 20,
                    cpu: 2
                },
                'os.3': {
                    name: "os.3",
                    max: 610,
                    ram: 6144,
                    free: 85,
                    disk: 20,
                    cpu: 3
                },
                'os.4': {
                    name: "os.4",
                    max: 475,
                    ram: 8192,
                    free: 56,
                    disk: 20,
                    cpu: 4
                },
                'os.5': {
                    name: "os.5",
                    max: 404,
                    ram: 10240,
                    free: 43,
                    disk: 20,
                    cpu: 5
                },
                'os.6': {
                    name: "os.6",
                    max: 335,
                    ram: 12268,
                    free: 31,
                    disk: 20,
                    cpu: 6
                },
                'os.7': {
                    name: "os.7",
                    max: 288,
                    ram: 14336,
                    free: 22,
                    disk: 20,
                    cpu: 7
                },
                'm1.xlarge': {
                    name: "m1.xlarge",
                    max: 175,
                    ram: 16384,
                    free: 12,
                    disk: 100,
                    cpu: 8
                },
                'os.29': {
                    name: "os.29",
                    max: 45,
                    ram: 59392,
                    free: 2,
                    disk: 20,
                    cpu: 29
                },
                'os.28': {
                    name: "os.28",
                    max: 45,
                    ram: 57344,
                    free: 2,
                    disk: 20,
                    cpu: 28
                },
                'os.27': {
                    name: "os.27",
                    max: 45,
                    ram: 55296,
                    free: 2,
                    disk: 20,
                    cpu: 27
                },
                'os.26': {
                    name: "os.26",
                    max: 45,
                    ram: 53248,
                    free: 2,
                    disk: 20,
                    cpu: 26
                },
                'os.25': {
                    name: "os.25",
                    max: 45,
                    ram: 51200,
                    free: 2,
                    disk: 20,
                    cpu: 25
                },
                'os.24': {
                    name: "os.24",
                    max: 58,
                    ram: 49152,
                    free: 2,
                    disk: 20,
                    cpu: 24
                },
                'os.23': {
                    name: "os.23",
                    max: 71,
                    ram: 47104,
                    free: 3,
                    disk: 20,
                    cpu: 23
                },
                'os.22': {
                    name: "os.22",
                    max: 71,
                    ram: 45056,
                    free: 3,
                    disk: 20,
                    cpu: 22
                },
                };

                for (flavor in this.flavors) {
                    // buildHighCharts(flavor, this.flavors[flavor]);
                }

/**/
                function buildHighCharts(flavor, details) {
                    /*
                        flavor can have . in name that is not a valid name for
                        HTML id or class. We remove it.
                    */
                    console.log('***');
                    console.log(flavor);
                    console.log(details);
                    console.log('###');
                    flavor_underscore = details.name.replace(/\./g,"");
                    console.log('***');
                    console.log(flavor_underscore);
                    console.log(details);
                    console.log('###');
                    return new Highcharts.Chart({ //nosonar
                        /*
                            solidgauge is easiest to read
                        */
                        chart: {
                            renderTo: flavor_underscore,
                            type: 'gauge',
                            height: 200,
                        },

                        title: null, // No title needed

                        pane: {
                            size: '200%', // As the image will be splited by 2, we double up the size to can all spaces
                            startAngle: -45, // Only half circle
                            endAngle: 45, // Only half circle
                            center: [ '50%', '125%' ], // Fix the center point as by default it s defined for circle
                            background: null,
                        },

                        yAxis: [{
                            min: 0,
                            max: details.max, // Scale is based on the maximum flavor we can launch
                            plotBands: [{
                                from: 0,
                                to: details.max/3,
                                color: {
                                    linearGradient: { cx: 0, cy: 0, r: 0.5 },
                                    stops: [
                                       [0, '#FF3333'],
                                       [1, '#55BF3B']
                                    ]
                                },
                                }, {
                                from: details.max/3,
                                to: details.max/1.2,
                                color: {
                                    linearGradient: { cx: 0, cy: 0, r: 0.5 },
                                    stops: [
                                       [0, '#55BF3B'],
                                       [1, '#FFFFFF']
                                    ]
                                },
                                }
                            ],
                        }],
                        series:[{
                            data : [ details.free ],
                            dataLabels: { // Just a custom format
                                format: '<div style="text-align:center"><span style="font-size:25px">{y}</span></div>',
                                borderWidth: 0,
                                y: -100,
                            },
                        }],
                    });
                }
/**/


        }
    });