async function getSamples(sensors, timerange, resolution = 10) {
    const data = {};
    
    for (const sensor of sensors) {
        if (sensor.code=="sensor-1"){   //now
            data[sensor.code] = {
                'temp': await getTEMP(),  //getTEMP(18.0, 28.0, resolution, 1.0),
                'co2': await getCO2(),
                'pm25': await getPM25(),
                'people': null,
                'RH': await getRH()
            };
        }
        else if (sensor.code=="sensor-3"){   //now
            data[sensor.code] = { 
                'temp': null,  //getTEMP(18.0, 28.0, resolution, 1.0),
                'co2': null,
                'pm25': null,
                'people': await getPPL(),
                'RH': null
            };
        }
        else if (sensor.code=="sensor-2"){  //future
            data[sensor.code] = {
                'temp': await future_temp(resolution),  //getTEMP(18.0, 28.0, resolution, 1.0),
                'co2': await future_co2(resolution),
                'pm25': await future_pm25(resolution),
                'people': null,
                'RH': await future_rh(resolution),
            };
        }

        // console.log(await get_value5())
    }
    return {
        count: resolution,
        timestamps: generateTimestamps(timerange.start, timerange.end, resolution),
        data
    };
}

function generateTimestamps(start, end, count) {
    const delta = Math.floor((end.getTime() - start.getTime()) / (count - 1));
    const timestamps = [];
    for (let i = 0; i < count; i++) {
        timestamps.push(new Date(start.getTime() + i * delta));
    }
    return timestamps;
}

const numbers = 1000

async function getTEMP() {
    try {
        const fetch = require('node-fetch');
        const response = await fetch('http://140.116.179.11:9000/value_all/temp?num=8800');
        const values = await response.json();
        //const data = exam
        // console.log(values);
        return values;
    } catch (error) {
        // console.error(error);
    }
}

async function getCO2() {
    try {
        const fetch = require('node-fetch');
        const response = await fetch('http://140.116.179.11:9000/value_all/CO2?num=8800');
        const values = await response.json();
        //const data = exam
        // console.log(values);
        return values;
    } catch (error) {
        // console.error(error);
    }
};

async function getPPL() {
    try {
        const fetch = require('node-fetch');
        const response = await fetch('http://140.116.179.11:9000/value_all/PplCnt?num=8800');
        const values = await response.json();
        //const data = exam
        // console.log(values);
        return values;
    } catch (error) {
        // console.error(error);
    }
};

async function getPM25() {
    try {
        const fetch = require('node-fetch');
        const response = await fetch('http://140.116.179.11:9000/value_all/PM25?num=8800');
        const values = await response.json();
        //const data = exam
        // console.log(values);
        return values;
    } catch (error) {
        // console.error(error);
    }
};

async function getRH() {
    try {
        const fetch = require('node-fetch');
        const response = await fetch('http://140.116.179.11:9000/value_all/RH?num=8800');
        const values = await response.json();
        //const data = exam
        // console.log(values);
        return values;
    } catch (error) {
        // console.error(error);
    }
};

function generateRandomValues(min, max, count, maxDelta) {
    const values = [];
    let lastValue = min + Math.random() * (max - min);
    for (let i = 0; i < count; i++) {
        values.push(lastValue);
        lastValue += (Math.random() - 0.5) * 2.0 * maxDelta;
        if (lastValue > max) {
            lastValue = max;
        }
        if (lastValue < min) {
            lastValue = min;
        }
    }
    return values;
}


async function future_temp(count) {
    const fetch = require('node-fetch');
    var currentTemp = await getTEMP();
    const response = await fetch('http://140.116.179.11:9000/get_predict/Temp?data=['+currentTemp+']');
    const data = await response.json();
    // console.log(currentTemp.slice(1900))
    // console.log('http://140.116.179.11:9000/get_predict/Temp?data=['+value+']');
    // console.log(data)
    return data
}

async function future_co2(count) {
    const fetch = require('node-fetch');
    var currentTemp = await getCO2();
    const response = await fetch('http://140.116.179.11:9000/get_predict/CO2?data=['+currentTemp+']');
    const data = await response.json();
    // console.log(currentTemp.slice(1900))
    // console.log('http://140.116.179.11:9000/get_predict/Temp?data=['+value+']');
    console.log(data)
    return data
}

async function future_rh(count) {
    const fetch = require('node-fetch');
    var currentTemp = await getRH();
    const response = await fetch('http://140.116.179.11:9000/get_predict/RH?data=['+currentTemp+']');
    const data = await response.json();
    // console.log(currentTemp.slice(1900))
    // console.log('http://140.116.179.11:9000/get_predict/Temp?data=['+value+']');
    // console.log(data)
    return data
}

async function future_pm25(count) {
    const fetch = require('node-fetch');
    var currentTemp = await getPM25();
    const response = await fetch('http://140.116.179.11:9000/get_predict/PM25?data=['+currentTemp+']');
    const data = await response.json();
    // console.log(currentTemp.slice(1900))
    // console.log('http://140.116.179.11:9000/get_predict/Temp?data=['+value+']');
    // console.log(data)
    return data
}

module.exports ={
    getSamples
};
