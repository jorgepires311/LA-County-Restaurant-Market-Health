function buildMetadata(record) {

    // @TODO: Complete the following function that builds the metadata panel
    
  
    // Use `d3.json` to fetch the metadata for a record
    var url = `/metadata/${record}`;
    d3.json(url).then(function(record){
  
      // Use d3 to select the panel with id of `#record-metadata`
      var record_metadata = d3.select("#losangeles");
  
      // Use `.html("") to clear any existing metadata
      losangeles.html("");
  
      // Use `Object.entries` to add each key and value pair to the panel
      // Hint: Inside the loop, you will need to use d3 to append new
      // tags for each key-value in the metadata.
      Object.entries(record).forEach(function ([key, value]) {
        var row = losangeles.append("p");
        row.text(`${key}: ${value}`);
  });
    }
  )};
  
//   function buildCharts(record) {
  
//     // @TODO: Use `d3.json` to fetch the record data for the plots
//     var url = `/records/${record}`;
//     d3.json(url).then(function(data) {
  
//       // @TODO: Build a Bubble Chart using the record data
//       var x_values = data.otu_ids;
//       var y_values = data.record_values;
//       var m_size = data.record_values;
//       var m_colors = data.otu_ids; 
//       var t_values = data.otu_labels;
  
//       var trace1 = {
//         x: x_values,
//         y: y_values,
//         text: t_values,
//         mode: 'markers',
//         marker: {
//           color: m_colors,
//           size: m_size
//         } 
//       };
    
//       var data = [trace1];
  
//       var layout = {
//         xaxis: { title: "OTU ID"},
//       };
  
//       Plotly.newPlot('bubble', data, layout);
  
//       // @TODO: Build a Pie Chart
//       d3.json(url).then(function(data) {  
//         var pie_values = data.record_values.slice(0,10);
//           var pie_labels = data.otu_ids.slice(0,10);
//           var pie_hover = data.otu_labels.slice(0,10);
    
//           var data = [{
//             values: pie_values,
//             labels: pie_labels,
//             hovertext: pie_hover,
//             type: 'pie'
//           }];
    
//           Plotly.newPlot('pie', data);
    
//         });
//       });   
//     }
    
  
//   function init() {
//     // Grab a reference to the dropdown select element
//     var selector = d3.select("#selDataset");
  
//     // Use the list of record names to populate the select options
//     d3.json("/names").then((recordNames) => {
//       recordNames.forEach((record) => {
//         selector
//           .append("option")
//           .text(record)
//           .property("value", record);
//       });
  
//       // Use the first record from the list to build the initial plots
//       const firstrecord = recordNames[0];
//       buildCharts(firstrecord);
//       buildMetadata(firstrecord);
//     });
//   }
  
//   function optionChanged(newrecord) {
//     // Fetch new data each time a new record is selected
//     buildCharts(newrecord);
//     buildMetadata(newrecord);
//   }
  
  // Initialize the dashboard
  init();
  