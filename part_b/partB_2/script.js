var margin = {top: 20, right: 30, bottom: 30, left: 20};
var width = 500 - margin.left - margin.right;
var barHeight = 20;
				
var x = d3.scale.linear().range([0, width]);

var chart = d3.select(".chart")
        .attr("width", width + margin.left + margin.right);

var allgroup = chart.append("g")   
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
var tooltip = chart.append("text")
        .style("visibility", "hidden");        
	
d3.tsv("state_population_gdp.tsv", type, function(error, data) {
        console.log(data)
        x.domain([0, d3.max(data, function(d) { return d.gdp; })]);

	chart.attr("height", margin.top + barHeight * data.length);

	var bar = allgroup.selectAll("g")
			.data(data)
		.enter().append("g")
                        .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
	bar.append("rect")
        .attr("width", function(d) { return x(d.gdp); })
        .attr("height", barHeight - 1)      
        .on("mouseover", function(d, i){
            var tipx = d3.select(this).attr("width");
            var tipy = barHeight* i;
            tooltip.attr("x", tipx); 		
            tooltip.attr("y", tipy);
            tooltip.attr("dx", 35);
            tooltip.attr("dy", 35);
            tooltip.style("visibility", "visible");
            tooltip.style("fill", "black");
            tooltip.text(d.gdp);})
        .on("mouseout", function(){
            tooltip.style("visibility", "hidden");})
        });

function type(d) {
	d.gdp = +d.gdp;
	return d;
}
