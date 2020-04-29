var covid_url = "/covid"
d3.json(covid_url, function(result) {
    console.log(result);

    var USA = [];
    var Spain = [];
    var Italy = [];
    var South_Korea = [];
    var India = [];
    var China = [];

    USA.push(result["US"].Death_Rate, result["US"].Date, result["US"].Confirmed)
    Spain.push(result["Spain"].Death_Rate, result["Spain"].Date, result["Spain"].Confirmed)
    Italy.push(result["Italy"].Death_Rate, result["Italy"].Date, result["Italy"].Confirmed)
    South_Korea.push(["South Korea"].Death_Rate, result["South Korea"].Date, result["South Korea"].Confirmed)
    India.push(["India"].Death_Rate, result["India"].Date, result["India"].Confirmed)
    China.push(["Mainland China"].Death_Rate, result["Mainland China"].Date, result["Mainland China"].Confirmed)

    var trace1 = {
        x: USA[1],
        y: USA[0],
        mode: 'lines',
        name: 'USA Death Rates',
        line: {
            dash: 'solid',
            width: 4
        }
    };

    var trace2 = {
        x: South_Korea[1],
        y: South_Korea[0],
        mode: 'lines',
        name: "South Korea Death Rates",
        line: {
            dash: 'dashdot',
            width: 4
        }
    };

    var trace3 = {
        x: China[1],
        y: China[0],
        mode: 'lines',
        name: "China Death Dates",
        line: {
            dash: 'dot',
            width: 4
        }
    };

    var trace4 = {
        x: India[1],
        y: India[0],
        mode: 'lines',
        name: "India Death Rates",
        line: {
            dash: 'solid',
            width: 4
        }
    };
    var trace5 = {
        x: Italy[1],
        y: Italy[0],
        mode: 'lines',
        name: "Italy Death Rates",
        line: {
            dash: 'dashdot',
            width: 4
        }
    };
    var data = [trace1, trace2, trace3, trace4, trace5];
    var layout = {
        title: 'Death Rates of 5 Selected Countries',
        xaxis: {
            autorange: true
        },
        yaxis: {
            autorange: true
        },
        legend: {
            y: 0.5,
            traceorder: 'reversed',
            font: {
                size: 16
            }
        }
    };
    Plotly.newPlot('my_dataviz', data, layout);

})