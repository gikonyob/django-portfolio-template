"use strict";

var color = Chart.helpers.color;

window.onload = function() {


  var ctx = document.getElementById('canvas').getContext('2d');
  window.myBar = new Chart(ctx, {
    type: 'bar',
    data: {
          labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          datasets: [{
            label: 'Sales',
            backgroundColor: color(window.chartColors.red).alpha(0.7).rgbString(),
            borderColor: window.chartColors.red,
            
            data: [
              40,10,60,90,30,70,30,25,15,75,30,90
            ]
          }, {
            label: 'New Users',
            backgroundColor: color(window.chartColors.blue).alpha(0.7).rgbString(),
            borderColor: window.chartColors.blue,
           
            data: [
              25,15,75,30,80,20,30,60,50,60,70,40
            ]
          }]
    },
    options: {
      responsive: true,
      legend: {
        position: 'bottom',
        display: false,
      },
      title: {
        display: false,
        text: 'Monthly Sales Report'
      }
    }
  });








  var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
  };
  var ctxDoughnut = document.getElementById('chart-area').getContext('2d');
  window.myDoughnut = new Chart(ctxDoughnut, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [
            randomScalingFactor(),
            randomScalingFactor(),
            randomScalingFactor()
          ],
          backgroundColor: [
            window.chartColors.red,
            window.chartColors.orange,
            window.chartColors.blue,
          ],
          label: 'Dataset 1'
        }],
        labels: [
          'Orders',
          'Pending',
          'Deliverd',
        ]
      },
      options: {
        responsive: true,
        legend: {
          position: 'bottom',
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










  

    






};





$(document).ready(function() {

        $('.date-rage').daterangepicker({
          opens : 'left'
        });
});






