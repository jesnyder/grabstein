var trace1 = {

  x: [1, 2, 3, 4, 5],

  y: [1, 6, 3, 6, 1],

  mode: 'markers',

  type: 'scatter',

  name: 'Team A',

  text: ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],

  marker: {
    size: 10*[1, 6, 3, 6, 1],
    color: ['rgb(255, 119, 180)', 'rgb(255, 119, 255)', 'rgb(255, 119, 180)', 'rgb(255, 119, 180)', 'rgb(255, 119, 180)'],

   }

};


var trace2 = {

  x: [1.5, 2.5, 3.5, 4.5, 5.5],

  y: [4, 1, 7, 1, 4],

  mode: 'markers',

  type: 'scatter',

  name: 'Team B',

  text: ['B-a', 'B-b', 'B-c', 'B-d', 'B-e'],

  marker: { size: 12 }

};

var trace3 = {

  x: [1, 2, 3, 4],

  y: [12, 9, 15, 12],

  mode: 'lines+markers',

  type: 'scatter'

};


var data2 = [trace1, trace2, trace3];


var layout = {

  xaxis: {
    range: [ 0.75, 5.25 ],
    showgrid: false,

    title: {
      text: 'x Axis',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }

    },
  },

  yaxis: {
    range: [0, 8],
    showgrid: false,

    title: {
      text: 'Suicide Rate',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }
    }
  },

  legend: {
    y: 0.5,
    yref: 'paper',
    font: {
      family: 'Courier New, monospace',
      size: 18,
      color: 'grey',
    }

  },

  title:'Data Labels on the Plot'
};



/*
Plotly.newPlot('tester', data2);
*/

TESTER = document.getElementById('tester');

Plotly.newPlot( TESTER, region, layout);
