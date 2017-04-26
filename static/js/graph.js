$(document).ready(function(){


// ============================Single Stock Graph==========================================
    // var createGraph = function(result, tick){
    //     require.config({
    //         baseUrl: '/js',
    //         paths: {
    //         d3: "http://d3js.org/d3.v3.min"
    //           }
    //     });
        
    //     require(["d3", "c3"], function(d3, c3){
            
    //         var data = JSON.parse(result)
    //         // console.log(data)
    //         var cdate = data['date_list']
    //         cdate.unshift('Dates')
    //         var date = data['date_list']
    //         // console.log(cdate[0])
    //         date.shift()
    //         var sp = data['adj_list']
    //         var stock = data['ticker']
    //         var chart = c3.generate({
    //             bindto: '.g'+tick,
    //             data: {
    //                 x: cdate[0],
    //                 columns: [cdate,
    //                     sp,
    //                     stock
    //                 ],
    //             },
    //             axis: {
    //                 y:{
    //                     label: {
    //                         text:"Percent Return",
    //                         position:'inner-middle'
    //                     }
    //                 },
    //                 x: {
    //                     type: 'timeseries',
    //                     tick: {
    //                         format: '%Y-%m-%d'
    //                     }
                   
    //                 }
    //             }
    //         });
    //     });
    // }; 

    // var chartButton = $('.chart_button');
    // chartButton.on('click', function() {
    //     var ticker = this.dataset.ticker
    //     console.log(ticker)
    //     var graph = $('.ct'+ticker);
    //     graph.css('display', 'block');
    //     // var ticker = $('.chart_button_div').data('ticker');
    //     $.ajax({
    //         method: 'GET',
    //         url: '/chart-data/'+ticker,
    //         // method: 'GET',
    //         success: function(result){
    //             var data = result
    //             var date = result['date_list']
    //             var sp = result['adj_list']
    //             var stock = result['ticker']
    //             createGraph(data, ticker)
    //             var close = $('.cg'+ticker)
    //             console.log(close)
    //             close.on('click', function(){
    //                 graph.css('display','none')
    //             })  
    //         }
    //     });

    // });
// ====================================================================================


// ============================Portfolio Graph==========================================
    
    var createPortfolioGraph = function(sentiment, div){
        require.config({
            baseUrl: '/js',
            paths: {
            d3: "http://d3js.org/d3.v3.min"
            }
        });
        console.log(sentiment)
        require(["d3", "c3"], function(d3, c3){
            var data = sentiment
            console.log(typeof data)
            var date_with_title = data['date_list']
            console.log(date_with_title)
            var dates_only = data['date_list']
            dates_only.shift()
            var sp = data['stock']
            console.log(sp)
            var portfolio = sentiment['sentiment']
            console.log(portfolio)
            var chart = c3.generate({
                bindto: '#'+div.attr('id'),
                data: {
                    x: date_with_title[0],
                    columns: [
                        date_with_title,
                        sp,
                        portfolio
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
                            text: 'second axis'
                        }
                        
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
    
    var portfolioGraph = $("#nflx_graph");
    var port_data = $('#nflx_graph').data('returns');
    createPortfolioGraph(port_data, $('#nflx_graph'))
// ====================================================================================

// =================================Portfolio 3yr===============================================
    
//     var portfolioGraphThree = $("#portfolio_vs_sp_three");
//     var port_data_three = $('#portfolio_vs_sp_three').data('returns');
//     createPortfolioGraph(port_data_three, portfolioGraphThree)


// // =================================Portfolio 5yr===============================================

//     var portfolioGraphFive = $("#portfolio_vs_sp_five");
//     var port_data_three = $('#portfolio_vs_sp_five').data('returns');
//     createPortfolioGraph(port_data_three, portfolioGraphFive)
});