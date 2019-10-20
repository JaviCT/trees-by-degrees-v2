
function getCountries(jQuery) {
    $.getJSON("data/countries.json", function(data) {
        var size = 0, key;
        for (key in data) {
            if (data.hasOwnProperty(key)) size++;
        }

        for (var i = 0; i < size -1; i++) {
            var x = document.getElementById("selectCountries");
            var c = document.createElement("option");
            var keys = Object.keys( data );
            c.text = keys[i];
            x.options.add(c, 1);
        };
    });
    // $.getJSON("data/cities.json", function(data) {
    //     console.log(data["Afghanistan"]);
    //     var aux = data["Afghanistan"]

    //     for (var i = 0; i < data["Afghanistan"].lenght -1; i++) {
    //         console.log(i);
            
    //         var x = document.getElementById("selectCities");
    //         var c = document.createElement("option");
    //         var keys = Object.keys( data[1] );
    //         c.text = keys[i];
    //         x.options.add(c, 1);
    //     };
    // });
}