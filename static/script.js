// DASHBOARD CHARTS CELLS ===================================================================
console.log(cellData)
var cellLabels = ["Pilot Plant", 
                  "Large Hock", 
                  "Half Gal Ross", 
                  "2 Gal Ross", 
                  "10 Gal Ross", 
                  "40 Gal Ross", 
                  "100 Gal Ross", 
                  "Mezz Tanks", 
                  "Activator"];

var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: cellLabels,
        datasets: [{
            label: 'Job Cells',
            data: JSON.parse(cellData),
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        legend: {
            display: false
        }
    }
});

// ================================================================== DASHBOARD CHARTS CELLS




// DASHBOARD CHARTS JOB TYPES =================================================================
var typeLabels = ["Normal", 
                  "Rework", 
                  "DOE"];

var ctx = document.getElementById('reworkchart-day').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: typeLabels,
        datasets: [{
            label: 'Job Cells',
            // data: JSON.parse(typeData),
            data: JSON.parse(typeCountDay),
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 206, 86, 0.5)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Today'
        },
        responsive: true,
        maintainAspectRatio: true,
      plugins: {
        labels: {
          render: 'percentage',
          fontColor: ['#444748', 'red', '#444748'],
          precision: 0
        }
      }

    }
});



var ctx = document.getElementById('reworkchart-week').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: typeLabels,
        datasets: [{
            label: 'Job Cells',
            // data: JSON.parse(typeData),
            data: JSON.parse(typeCountWeek),
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 206, 86, 0.5)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'This Week'
        },
        responsive: true,
        maintainAspectRatio: true,
      plugins: {
        labels: {
          render: 'percentage',
          fontColor: ['#444748', 'red', '#444748'],
          precision: 0
        }
      }

    }
});



var ctx = document.getElementById('reworkchart-month').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: typeLabels,
        datasets: [{
            label: 'Job Cells',
            // data: JSON.parse(typeData),
            data: JSON.parse(typeCountMonth) ,
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 206, 86, 0.5)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'This Month'
        },
        responsive: true,
        maintainAspectRatio: true,
      plugins: {
        labels: {
          render: 'percentage',
          fontColor: ['#444748', 'red', '#444748'],
          precision: 0
        }
      }

    }
});


var ctx = document.getElementById('reworkchart-year').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: typeLabels,
        datasets: [{
            label: 'Job Cells',
            // data: JSON.parse(typeData),
            data: JSON.parse(typeCountYear),
            backgroundColor: [
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 99, 132, 0.5)',
                'rgba(255, 206, 86, 0.5)'
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 206, 86, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'This Year'
        },
        responsive: true,
        maintainAspectRatio: true,
      plugins: {
        labels: {
          render: 'percentage',
          fontColor: ['#444748', 'red', '#444748'],
          precision: 0
        }
      }

    }
});


// =================================================================DASHBOARD CHARTS JOB TYPES








// DASHBOARD EVENT LISTENER =======================================================================
dash_panel_completed_today = document.querySelector("#dash-panel-completed-today")
dash_panel_completed_week = document.querySelector("#dash-panel-completed-week")
dash_panel_completed_month = document.querySelector("#dash-panel-completed-month")

dash_panel_2 = document.querySelector("#panel_2").addEventListener("click", function(){
    dash_panel_completed_today.submit();
    // window.location = "/test_land/"
   });

dash_panel_3 = document.querySelector("#panel_3").addEventListener("click", function(){
dash_panel_completed_week.submit();
    // window.location = "/test_land/"
   });
    
dash_panel_4 = document.querySelector("#panel_4").addEventListener("click", function(){
dash_panel_completed_month.submit();
    // window.location = "/test_land/"
    });
    




// ======================================================================= DASHBOARD EVENT LISTENER




