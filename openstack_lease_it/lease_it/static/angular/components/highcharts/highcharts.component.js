angular.module('leaseItHighcharts').
    component('leaseItHighcharts', {
        bindings: {
            details: '<'
        },
        template: '<p>{{ $ctrl.details }}</p>',
        controller: function($scope, $filter){
            /* We create a default configuration where missed
                - chart.renderTo
                - yAxis[0].max = 100
                - yAxis[0].plotBands[0].to = 30
                - yAxis[0].plotBands[1].from = 30
                - yAxis[0].plotBands[1].to = 80
                - series[0].data = [ 20 ]
            */
            var options = {
                chart: {
                    type: 'gauge',
                    height: 180,
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
                    max: 100, // Scale is based on the maximum flavor we can launch
                    plotBands: [{
                        from: 0,
                        to: 30,
                        color: {
                            linearGradient: { cx: 0, cy: 0, r: 0.5 },
                            stops: [
                               [0, '#FF3333'],
                               [1, '#55BF3B']
                            ]
                        },
                        }, {
                        from: 30,
                        to: 80,
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
                    data: [ 20 ],
                    dataLabels: { // Just a custom format
                        format: '<div style="text-align:center"><span style="font-size:25px">{y}</span></div>',
                        borderWidth: 0,
                        y: -100,
                    },
                }],

                loading: false
            };
            ctrl = this.details;

            /* constructor */
            this.$onInit = function () {
                this.options = this.details
                console.log(this.details)
                initCharts(this.details)
            }


            function initCharts (details) {
                console.log(details)
                /* load charts specific config. */
                options.yAxis[0].max = details.max
                options.yAxis[0].plotBands[0].to = details.max/3;
                options.yAxis[0].plotBands[1].from = details.max/3;
                options.yAxis[0].plotBands[1].to = details.max/1.2;

                options.series[0].data = [ details.free ]

                Highcharts.chart($filter('leaseItDotRemove')(details.name), options)
            }

        }
    });