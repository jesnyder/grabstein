var layout = {

  xaxis: {
    //type: 'log',
    //range: [ 0, 40 ],
    showgrid: false,

    title: {
      text: 'Percentage of Households with 1 Member',
      font: {
        family: 'Courier New, monospace',
        size: 18,
        color: '#7f7f7f'
      }

    },
  },

  yaxis: {
    //range: [0, 45],
    //type: 'log',
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

  title:'Suicide Rate Coorelated to % of Single Person Households'
};



/*
Plotly.newPlot('tester', data2);
*/

var region = [Europe, Africa, Americas, Asia, Oceania];

console.log("region = ")
console.log(region)
TESTER = document.getElementById('tester');

Plotly.newPlot( TESTER, region, layout);
