// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart','bar']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);


// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Pilot', 6],
    ['Large Hock', 12],
    ['Ross 100', 2],
    ['Ross 40', 1],
    ['Ross 10', 1],
    ['Ross 2', 2],
    ['Ross 1/2', 1],
    ['Activator', 1],
    ['Mezz', 1]
  ]);

  // Set chart options
  var options = {'title':'Current Equipment Demand',
                 'width':500,
                 'height':300,
                'fontSize':16};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}



google.charts.setOnLoadCallback(drawMultSeries);

function drawMultSeries() {
      var data = google.visualization.arrayToDataTable([
        ['Day', 'Target', 'Actual'],
        ['Monday', 20, 17],
        ['Tuesday', 20, 21],
        ['Wednesday', 20, 15],
        ['Thursday', 20, 23],
        ['Friday', 20, 18],
        ['Saturday', 20, 18],
      ]);

      var options = {
        title: 'Current Week output',
        chartArea: {width: '50%'},
        fontSize: 16,
        height: 300,
        width: 500,
        hAxis: {
          title: '',
          minValue: 0
        }

      };

      var chart = new google.visualization.BarChart(document.getElementById('chart_div2'));
      chart.draw(data, options);
    }




    google.charts.setOnLoadCallback(drawColChart);
    function drawColChart() {
      var data = google.visualization.arrayToDataTable([
        ['Work Cells', 'Daily Target', 'Total', 'LG Hock','Pilot','Ross 100','Ross 40','Ross 10','Ross 2','Ross 1/2','Activator','Mezz'],
        ['Jobs Completed', 20, 17, 7,6,0,1,1,0,2,0,0]
        
      ]);

      var options = {
          chart: {
          title: 'Daily output',
        },
        bars: 'vertical',
        vAxis: {format: 'decimal'},
        height: 400,
        width: 1000,
        colors: ['#9E560B','#1B9E77','#23809E','#4F2B9E']
      };

      var chart = new google.charts.Bar(document.getElementById('col_chart_div'));

      chart.draw(data, google.charts.Bar.convertOptions(options));

      var btns = document.getElementById('btn-group');

      btns.onclick = function (e) {

        if (e.target.tagName === 'BUTTON') {
          options.vAxis.format = e.target.id === 'none' ? '' : e.target.id;
          chart.draw(data, google.charts.Bar.convertOptions(options));
        }
      }
    }