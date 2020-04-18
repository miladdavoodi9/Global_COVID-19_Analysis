var url = "/global_covid"
var covid_url = "/covid"

d3.json(url,function(response){
  console.log(response);
  var country = []
  // var confirmed = []
  // var death = []
  // var country_confirmed = []
  var DataPoints = [];
  var dps = []; 
  for (var countryName in response) {
    DataPoints.push({ 
      y: response[countryName].Confirmed, 
      label: (countryName)
    })
    dps.push({ 
      y: response[countryName].Deaths, 
      label: (countryName)
    })
  }
  
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    title:{
      text:"COVID-19 Confirmed Cases and Deaths"
    },
    // axisX:{
    //   interval: 1
    // },
    axisY:{
      interlacedColor: "rgba(1,77,101,.2)",
      gridColor: "rgba(1,77,101,.1)",
      title: "Number of Cases",
      _scaleBreaks: {
        customBreaks: {
          startValue: 300000,
          endValue: 800000
        }
      },
      // get scaleBreaks() {
      //   return this._scaleBreaks;
      // },
      // set scaleBreaks(value) {
      //   this._scaleBreaks = value;
      // },
    },
    data: [
      {
      type: "bar",
      name: "Confirmed",
      axisYType: "secondary",
      color: "#014D65",
      dataPoints: DataPoints
    }, 

    {
      type: "bar",
      name: "Deaths",
      axisYType: "secondary", 
      color: "#ed0202", 
      dataPoints: dps
    }
  ]
});
chart.render();
});


