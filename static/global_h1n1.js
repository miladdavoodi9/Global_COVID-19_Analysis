// Plot the default route once the page loads
var URL = "/global_h1n1";

function buildPlot(){
  d3.json(URL,function(response){
    console.log(response);
    
    var country = []
    var confirmed = []
    var death = []

    for (var countryName in response) {

      death.push(response[countryName].Deaths);
      confirmed.push(response[countryName].Confirmed);
      country.push(countryName);
    };

    console.log(country);
    console.log(confirmed);
    console.log(death);
  

  
    var trace = {
      type: "bar",
      name: "Confirmed Cases",
      x: country,
      y: confirmed
    };
    var trace1 = {
      type: "bar", 
      name: "Deaths", 
      x: country, 
      y: death
    }; 

    var data = [trace, trace1]; 
    var layout = {
      title: "Global H1N1 Confirmed Cases and Deaths", 
      xaxis: { autorange: true, type: "category"}, 
      yaxis: {autorange: true}
    };
    
    Plotly.newPlot("my_dataviz", data, layout);
  }) 
}
buildPlot(); 


















// // set the dimensions and margins of the graph
// var margin = {top: 10, right: 30, bottom: 30, left: 60},
//     width = 460 - margin.left - margin.right,
//     height = 400 - margin.top - margin.bottom;

// // append the svg object to the body of the page
// var svg = d3.select("#my_dataviz")
//   .append("svg")
//     .attr("width", width + margin.left + margin.right)
//     .attr("height", height + margin.top + margin.bottom)
//   .append("g")
//     .attr("transform",
//           "translate(" + margin.left + "," + margin.top + ")");

// //Read the data
// var parseTime = d3.timeParse("%d-%m-%Y");

// var url = '/covid'
// d3.json(url).then(function(response) {
//   var responses = console.log(response); 
  
//   for (response=0; response < responses.length; response++) { 
//     var Confirmed = 

  
//   var Confirmed = response[0][0]["Confirmed"]; 
//   var Date = response[0][0]["Date"]; 

//   Date.forEach(function(data){ 
//     data.Date = parseTime(data.Date); 
//   })

//   Confirmed.forEach(function(data){
//     Confirmed = 
//   })
  
//   var xTimeScale = d3.scaleTime()
//   .domain(d3.extent(response, data => data.Date))
//   .range([0, chartWidth]);
  
//   var yLinearScale = d3.scaleLinear()
//   .domain([0, d3.max(response, data => data.Confirmed)])
//   .range([chartHeight, 0]);

//   var bottomAxis = d3.axisBottom(xTimeScale);
//   var leftAxis = d3.axisLeft(yLinearScale);

//   var drawLine = d3.line()
//     .x(data => xTimeScale(data.Date))
//     .y(data => yLinearScale(data.Confirmed));

//   chartGroup.append("path").attr("d", drawLine(response)).classed("line", true);

//   chartGroup.append("g").classed("axis", true).call(leftAxis);
  
//   chartGroup.append("g")
//   .classed("axis", true)
//   .attr("transform", `translate(0, ${chartHeight})`)
//   .call(bottomAxis);
// }).catch(function(error) {
//   console.log(error);
// });


// //   return{Date: d3.timeParse("%d-%m-%Y") (d.Date, value: d.value)}
// // }
// //   // Now I can use this dataset:
// //   function(data) {

// //     // Add X axis --> it is a date format
// //     var x = d3.scaleTime()
// //       .domain(d3.extent(data, function(d) { return d.date; }))
// //       .range([ 0, width ]);
// //     svg.append("g")
// //       .attr("transform", "translate(0," + height + ")")
// //       .call(d3.axisBottom(x));

// //     // Add Y axis
// //     var y = d3.scaleLinear()
// //       .domain([0, d3.max(data, function(d) { return +d.value; })])
// //       .range([ height, 0 ]);
// //     svg.append("g")
// //       .call(d3.axisLeft(y));

// //     // Add the line
// //     svg.append("path")
// //       .datum(data)
// //       .attr("fill", "none")
// //       .attr("stroke", "steelblue")
// //       .attr("stroke-width", 1.5)
// //       .attr("d", d3.line()
// //         .x(function(d) { return x(d.date) })
// //         .y(function(d) { return y(d.value) })
// //         )

// // })






















// // // Define SVG area dimensions
// // var svgWidth = 960;
// // var svgHeight = 660;

// // // Define the chart's margins as an object
// // var chartMargin = {
// //   top: 30,
// //   right: 30,
// //   bottom: 30,
// //   left: 30
// // };

// // // Define dimensions of the chart area
// // var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
// // var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// // // Select body, append SVG area to it, and set the dimensions
// // var svg = d3
// //   .select("my_dataviz")
// //   .append("svg")
// //   .attr("height", svgHeight)
// //   .attr("width", svgWidth);

// // // Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// // // to the margins set in the "chartMargin" object.
// // var chartGroup = svg.append("g").attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// // //Read in JSON data through Flask
// // var url = "/global_h1n1";
// // d3.json(url).then(function(response) {
// //   console.log(response); 
// //   var country = response[0]; 
// //   var date = response[0][1]["Date"]; 
// //   var confirmed = response [0][0]["Confirmed"];
// //   var death_rate = response[0][0]["Death_Rate"];
// //   var deaths = respone[0][0]["Deaths"]; 
// //   var recovered_rate = response[0][0]["Recovery_Rate"]; 
// //   var recovered = response[0][0]["Recovered"]; 

// // });






// // function buildBar(){ 
// //   d3.json(url),then(function(response){ 
// //     console.log(response);"Date"]; 
    
// //     var recovered_rate = response[0][1]["Recovery_Rate"]; 
// //     var recovered = response[0][1]["Recovered"]; 
// //     var parseTime = d3.timeParse("%d-%b-%Y");
// //     date.forEach(function(d) {
// //       d.date = parseTime(d.date);})

// //     var svgWidth = 960;
// //     var svgHeight = 500;
      
// //     var margin = { top: 20, right: 40, bottom: 60, left: 50 };
      
// //     var width = svgWidth - margin.left - margin.right;
// //     var height = svgHeight - margin.top - margin.bottom;
    
// //     var svg = d3.select("my_dataviz").append("svg").attr("width", svgWidth).attr("height", svgHeight);
// //     var chartGroup = svg.append("g").attr("transform", `translate(${margin.left}, ${margin.top})`);


  
// //   Plotly.newPlot("my_dataviz", data)
// // }
// // buildPlot();







// // var svgWidth = 960;
// // var svgHeight = 500;

// // var margin = { top: 20, right: 40, bottom: 60, left: 50 };

// // var width = svgWidth - margin.left - margin.right;
// // var height = svgHeight - margin.top - margin.bottom;

// // // Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
// // var svg = d3
// //   .select("body")
// //   .append("svg")
// //   .attr("width", svgWidth)
// //   .attr("height", svgHeight);

// // var chartGroup = svg.append("g")
// //   .attr("transform", `translate(${margin.left}, ${margin.top})`);

  

// //     var country = response[0] ; 
// //     var date = response[0][1]["Date"]; 
// //     var confirmed = response[0][1]["Confirmed"] ; 
// //     var death_rate = response[0][1]["Death_Rate"]; 
// //     var deaths = response[0][1]["Deaths"]; 
// //     var recovered_rate = response[0][1]["Recovery_Rate"]; 
// //     var recovered = response[0][1]["Recovered"]; 

// // var parseTime = d3.timeParse("%d-%b-%Y");

// // date.forEach(function(d) {
// //   d.date = parseTime(d.Date);
// // })

// // d3.select("#selectButton")
// // .selectAll('myOptions')
// // .data(country)
// // .enter()
// // .append('option')
// // .text(function (d) { return d; }) // text showed in the menu
// // .attr("value", function (d) { return d; }) // corresponding value returned by the button

// // // A color scale: one color for each group
// // var myColor = d3.scaleOrdinal()
// // .domain(country)
// // .range(d3.schemeSet2);

// // // Add X axis --> it is a date format
// // var x = d3.scaleLinear()
// // .domain(d3.extent(data, function(d) { return d.date; }))
// // .range([ 0, width ]);
// // svg.append("g")
// // .attr("transform", "translate(0," + height + ")")
// // .call(d3.axisBottom(x).ticks(7));

// //  // Add Y axis
// //  var y = d3.scaleLinear()
// //  .domain([0, d3.max(data, function(d) { return +d.n; })])
// //  .range([ height, 0 ]);
// // svg.append("g")
// //  .call(d3.axisLeft(y));

// // // Initialize line with first group of the list
// // var line = svg.append('g')
// // .append("path")
// // .datum(data.filter(function(d){return d.confirmed}))
// // .attr("d", d3.line()
// // .x(function(d) { return x(d.date) })
// // .y(function(d) { return y(+d.n) })
// // )
// // .attr("stroke", function(d){ return myColor("valueA") })
// // .style("stroke-width", 4)
// // .style("fill", "none")

// //  // A function that update the chart
// //  function update(selectedGroup) {
// //    // Create new data with the selection?
// //    var dataFilter = data.filter(function(d){return d.country==selectedGroup})

// //    // Give these new data to update line
// //    line.datum(dataFilter).transition().duration(1000)
// //    .attr("d", d3.line()
// //    .x(function(d) { return x(d.date) })
// //    .y(function(d) { return y(+d.n) })
// //    )
// //    .attr("stroke", function(d){ return myColor(selectedGroup) })
// // }
// // // When the button is changed, run the updateChart function
// // d3.select("#selectButton").on("change", function(d) {
// //   // recover the option that has been chosen
// //   var selectedOption = d3.select(this).property("value")
// //   // run the updateChart function with this selected option
// //   update(selectedOption)
// // })

// // })



















// // // //     var trace = {
// // // //       type: "scatter",
// // // //       mode: "lines",
// // // //       name: "COVID Confirmed",
// // // //       x: d.date,
// // // //       y: d.confirmed,
// // // //       line: {
// // // //         color: "#17BECF"
// // // //       }
// // // //     };

// // // //     var trace1 = {
// // // //       type: "scatter", 
// // // //       mode: "lines", 
// // // //       name: "COVID Deaths", 
// // // //       x: response.map(data => data.Date),
// // // //       y: response.map(data => data.Deaths),
// // // //       line: {
// // // //         color: "##cf1795"
// // // //       }
// // // //     }
// // // //     var data = [trace, trace1];

// // // //     var layout = {
// // // //       title: "COVID Confirmed vs. Deaths",
// // // //       xaxis: {
// // // //         type: "date"
// // // //       },
// // // //       yaxis: {
// // // //         autorange: true,
// // // //         type: "linear"
// // // //       }
// // // //     };

// // // //     Plotly.newPlot("#my_dataviz", data, layout);
// // // //   });
// // // // }

// // // // buildPlot();
