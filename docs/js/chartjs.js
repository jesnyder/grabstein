
console.log(bubble);

  const data = bubble;

  const config = {
    type: 'bubble',
    data: data,
    options: {
    responsive: true,
    plugins: {
      title: {
        display: true,
        text: 'Suicide Rate Coorelated to % of 1 Member Households'
      }
    },
    scales: {
      x: {
        display: true,
        type: 'logarithmic',
        labelString: '% of 1 Member Households'
      },
      y: {
        display: true,
        type: 'logarithmic',
        labelString: 'Suicide Rate'

      }
    }
  },
  };

 const ctx = document.getElementById('myChart');

  new Chart(ctx, config);
