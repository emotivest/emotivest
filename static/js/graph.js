$(document).ready(function(){



// ============================Graph==========================================
    
    var createGraph = function(sentiment, div){
        require.config({
            baseUrl: '/js',
            paths: {
            d3: "http://d3js.org/d3.v3.min"
            }
        });
        console.log(sentiment)
        require(["d3", "c3"], function(d3, c3){
            var data = sentiment
            var date_with_title = data['date_list']
            var dates_only = data['date_list']
            dates_only.shift()
            var stockReturns = data['stock']
            var stockSentiment = sentiment['sentiment']
            console.log(stockSentiment)
            var chart = c3.generate({
                bindto: '#'+div.attr('id'),
                data: {
                    x: date_with_title[0],
                    columns: [
                        date_with_title,
                        stockReturns,
                        stockSentiment
                    ],
                    axes: {
                        NFLX:'y',
                        NFLX_Sentiment: 'y2'
                    }
                },
                axis: {
                    y:{
                        label: {
                            text:"Percent Return",
                            position:'inner-middle'
                        }
                    },
                    y2: {
                        label: {
                            text: 'second axis',
                            position:'inner-middle'
                        },
                        show: true
                        
                    },
                    x: {
                        type: 'timeseries',
                        tick: {
                            format: '%Y-%m-%d'
                        }
                    }
                }
            });
        });
    };
    
    var nflxDiv = $("#nflx_graph");
    var nflxData = $('#nflx_graph').data('returns');
    createGraph(nflxData, nflxDiv)

});



