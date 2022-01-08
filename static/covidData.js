fetch("https://covid-19-statistics.p.rapidapi.com/reports/total?date=2020-04-07", {

    "method": "GET",

    "headers": {

        "x-rapidapi-key": "4b799c834cmsh34cb8437d9a6ab2p121762jsn6edb511f97c9",

        "x-rapidapi-host": "covid-19-statistics.p.rapidapi.com"

    }

})

.then(response => response.json())

.then(data => {

    let numbers = document.querySelectorAll('.numbers');

    num = new Intl.NumberFormat('en-US');

    numbers[0].innerHTML = num.format(data.data.confirmed);

    numbers[1].innerHTML = num.format(data.data.active);

    numbers[2].innerHTML = num.format(data.data.deaths);

    numbers[3].innerHTML = num.format(data.data.recovered);

})

.catch(err => {

    console.error(err);

});











