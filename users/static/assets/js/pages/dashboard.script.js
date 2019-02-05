"use strict";

var presets = window.chartColors;
  var utils = Samples.utils;
  var inputs = {
    min: -100,
    max: 100,
    count: 8,
    decimals: 2,
    continuity: 1
  };

  function generateData(config) {
    return utils.numbers(Chart.helpers.merge(inputs, config || {}));
  }

  function generateLabels(config) {
    return utils.months(Chart.helpers.merge({
      count: inputs.count,
      section: 3
    }, config || {}));
  }




          // reset the random seed to generate the same data for all charts
          utils.srand(8);

          new Chart('chart-2', {
            type: 'line',

            data: {
              labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June'],
              datasets: [{
                backgroundColor: utils.transparentize(presets.blue),
                borderColor: presets.blue,
                data: generateData(),
                label: 'Dataset',
                fill: 'start',
              }]
            },
            
            options: {
              maintainAspectRatio: false,
              spanGaps: false,
              scaleShowLabels : false,
              elements: {
                line: {
                  tension: 0.000001
                }
              },
              plugins: {
                filler: {
                  propagate: false
                }
              },
              scales: {
                xAxes: [{
                  display: false,
                  ticks: {
                    autoSkip: false,
                    maxRotation: 0,
                    display: false
                  }
                }],
                yAxes: [{
                  display: false,
                  ticks: {
                    display: false
                  }
                }]
              },
              title: {
                display: false
              },
              legend: {
                display: false
              },
            }
          });



          new Chart('chart-3', {
            type: 'line',

            data: {
              labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June'],
              datasets: [{
                backgroundColor: utils.transparentize(presets.red),
                borderColor: presets.red,
                data: generateData(),
                label: 'Dataset',
                fill: 'start',
              }]
            },
            
            options: {
              maintainAspectRatio: false,
              spanGaps: false,
              scaleShowLabels : false,
              elements: {
                line: {
                  tension: 0.000001
                }
              },
              plugins: {
                filler: {
                  propagate: false
                }
              },
              scales: {
                xAxes: [{
                  display: false,
                  ticks: {
                    autoSkip: false,
                    maxRotation: 0,
                    display: false
                  }
                }],
                yAxes: [{
                  display: false,
                  ticks: {
                    display: false
                  }
                }]
              },
              title: {
                display: false
              },
              legend: {
                display: false
              },
            }
          });


          new Chart('chart-4', {
            type: 'line',

            data: {
              labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June'],
              datasets: [{
                backgroundColor: utils.transparentize(presets.green),
                borderColor: presets.green,
                data: generateData(),
                label: 'Dataset',
                fill: 'start',
              }]
            },
            
            options: {
              maintainAspectRatio: false,
              spanGaps: false,
              scaleShowLabels : false,
              elements: {
                line: {
                  tension: 0.000001
                }
              },
              plugins: {
                filler: {
                  propagate: false
                }
              },
              scales: {
                xAxes: [{
                  display: false,
                  ticks: {
                    autoSkip: false,
                    maxRotation: 0,
                    display: false
                  }
                }],
                yAxes: [{
                  display: false,
                  ticks: {
                    display: false
                  }
                }]
              },
              title: {
                display: false
              },
              legend: {
                display: false
              },
            }
          });


          new Chart('chart-5', {
            type: 'line',

            data: {
              labels: ['Jan', 'Feb', 'March', 'April', 'May', 'June'],
              datasets: [{
                backgroundColor: utils.transparentize(presets.yellow),
                borderColor: presets.yellow,
                data: generateData(),
                label: 'Dataset',
                fill: 'start',
              }]
            },
            
            options: {
              maintainAspectRatio: false,
              spanGaps: false,
              scaleShowLabels : false,
              elements: {
                line: {
                  tension: 0.000001
                }
              },
              plugins: {
                filler: {
                  propagate: false
                }
              },
              scales: {
                xAxes: [{
                  display: false,
                  ticks: {
                    autoSkip: false,
                    maxRotation: 0,
                    display: false
                  }
                }],
                yAxes: [{
                  display: false,
                  ticks: {
                    display: false
                  }
                }]
              },
              title: {
                display: false
              },
              legend: {
                display: false
              },
            }
          });




var color = Chart.helpers.color;
var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
  };
  var ctxDoughnut = document.getElementById('chart-doughnut').getContext('2d');
  window.myDoughnut = new Chart(ctxDoughnut, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor()
          ],
          borderWidth : 6,
          hoverBorderColor : 'white',
          backgroundColor: [
            color(window.chartColors.red).alpha(0.7).rgbString(),
            color(window.chartColors.yellow).alpha(0.7).rgbString(),
            color(window.chartColors.blue).alpha(0.7).rgbString(),
          ],
          label: 'Dataset 1'
        }],
        labels: [
          'Europe',
          'Asia',
          'Other',
        ]
      },
      options: {
        responsive: true,
        cutoutPercentage: 70,
        legend: {
          position: 'bottom',
          display: false,
        },
        title: {
          display: false,
          text: 'Chart.js Doughnut Chart'
        },
        animation: {
          animateScale: true,
          animateRotate: true
        }
      }
  });





$(document).ready(function() {

        $('.date-rage').daterangepicker({
          opens : 'left'
        });

        $('#calendar').fullCalendar({
          header: false,
          events: [
        {
          title: 'All Day Event',
          start: '2018-06-01'
        },
        {
          title: 'Long Event',
          start: '2018-06-07',
          end: '2018-06-10'
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: '2018-06-09T16:00:00'
        },
        {
          id: 999,
          title: 'Repeating Event',
          start: '2018-06-16T16:00:00'
        },
        {
          title: 'Conference',
          start: '2018-06-11',
          end: '2018-06-13'
        },
        {
          title: 'Meeting',
          start: '2018-06-12T10:30:00',
          end: '2018-06-12T12:30:00'
        },
        {
          title: 'Lunch',
          start: '2018-03-12T12:00:00'
        },
        {
          title: 'Meeting',
          start: '2018-06-12T14:30:00'
        },
        {
          title: 'Happy Hour',
          start: '2018-06-12T17:30:00'
        },
        {
          title: 'Dinner',
          start: '2018-06-12T20:00:00'
        },
        {
          title: 'Birthday Party',
          start: '2018-06-13T07:00:00'
        },
        {
          title: 'Click for Google',
          url: 'http://google.com/',
          start: '2018-06-28'
        }
      ]
        });


        $('#prev').on('click', function() {
          $('#calendar').fullCalendar('prev'); // call method
        });

        $('#next').on('click', function() {
          $('#calendar').fullCalendar('next'); // call method
        });

        $('#today').on('click', function() {
          $('#calendar').fullCalendar('today'); // call method
        });


        $('#list-view').on('click', function() {
          $('#calendar').fullCalendar( 'changeView', 'list'); // call method
        });

        $('#week-view').on('click', function() {
          $('#calendar').fullCalendar( 'changeView', 'basicWeek'); // call method
        });

        $('#day-view').on('click', function() {
          $('#calendar').fullCalendar( 'changeView', 'agenda'); // call method
        });

        $('#month-view').on('click', function() {
          $('#calendar').fullCalendar( 'changeView', 'month'); // call method
        });


});