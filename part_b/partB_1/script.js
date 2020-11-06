console.log('change3')
var margin = {top: 20, right: 30, bottom: 30, left: 20};
// var width = 500 - margin.left - margin.right;
var width = 20;
// var barHeight = 20;
var barHeight = 500 - margin.top - margin.bottom
				
var x = d3.scale.linear().range([0, width]);

var chart = d3.select(".chart")
        .attr("width", width + margin.left + margin.right);

var allgroup = chart.append("g")   
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    
var tooltip = chart.append("text")
        .style("visibility", "hidden");        
	
d3.tsv("state_population_gdp.tsv", type, function(error, data) {
        x.domain([0, d3.max(data, function(d) { return d.population; })]);

	chart.attr("height", margin.top + barHeight * data.length);

	var bar = allgroup.selectAll("g")
			.data(data)
		.enter().append("g")
                        .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
	bar.append("rect")
        .attr("height", function(d) { return x(d.population); })
        .attr("width", barHeight - 1)      
        .on("mouseover", function(d, i){
            var tipx = d3.select(this).attr("width");
            var tipy = barHeight* i;
            tooltip.attr("x", tipx); 		
            tooltip.attr("y", tipy);
            tooltip.attr("dx", 35);
            tooltip.attr("dy", 35);
            tooltip.style("visibility", "visible");
            tooltip.style("fill", "black");
            tooltip.text(d.population);})
        .on("mouseout", function(){
            tooltip.style("visibility", "hidden");})
        .on("click", function() {
                d3.selectAll("svg > *").remove();
                margin = {top: 20, right: 30, bottom: 30, left: 20};
                width = 500 - margin.left - margin.right;
                barHeight = 20;
                                                
                x = d3.scale.linear().range([0, width]);
                
                chart = d3.select(".chart")
                        .attr("width", width + margin.left + margin.right);
                
                allgroup = chart.append("g")   
                        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
                    
                tooltip = chart.append("text")
                        .style("visibility", "hidden");        
                        
                d3.tsv("state_population_gdp.tsv", type, function(error, data) {
                        data.sort(compare)
                        x.domain([0, d3.max(data, function(d) { return d.population; })]);
                
                        chart.attr("height", margin.top + barHeight * data.length);
                
                        bar = allgroup.selectAll("g")
                                        .data(data)
                                .enter().append("g")
                                        .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
                        bar.append("rect")
                        .attr("width", function(d) { return x(d.population); })
                        .attr("height", barHeight - 1)      
                        .on("mouseover", function(d, i){
                            tipx = d3.select(this).attr("width");
                            tipy = barHeight* i;
                            tooltip.attr("x", tipx); 		
                            tooltip.attr("y", tipy);
                            tooltip.attr("dx", 35);
                            tooltip.attr("dy", 35);
                            tooltip.style("visibility", "visible");
                            tooltip.style("fill", "black");
                            tooltip.text(d.population);})
                        .on("mouseout", function(){
                            tooltip.style("visibility", "hidden");})
});

function type(d) {
	d.population = +d.population;
	return d;
}

        });

});

function type(d) {
	d.population = +d.population;
	return d;
}

function compare(a, b) {
        if(a.population > b.population) {
                return 1;
        } 
        if(a.population < b.population) {
                return -1;
        }
        return 0;
}
