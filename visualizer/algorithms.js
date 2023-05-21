var svg,
    bandScale,
    text,
    maxElement = 15,
    dataRange = 1000,
    areaHeight = 250,
    areaWidth = 800,
    time = 300,
    traverseColor = "#ffcaa1",
    sortedColor = "green",
    isSorting = false,
    isFound = false

// generating random data
var data = randomData(maxElement, dataRange);

function setSpeed() {
    time = 1000 - document.getElementById("speed").value;
}
//a d3 function for scaling height for all the data this function
var heightScale = d3
    .scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, areaHeight]);

// initialized a chart with random value
createChart(data);

const SearchAlgo = {
    binarySearch() {
        const timer = (ms) => new Promise((res) => setTimeout(res, ms));
        async function search() {
            let left = 0;
            let right = data.length - 1;
            let mid;
            while (left <= right) {
                // If user click on stop button then this function will stop 
                mid = (left + right) / 2 || 0;
                await timer(time);
                changeBarColor(data[mid], traverseColor);
                if (data[mid] == target) {
                    changeBarColor(data[mid], sortedColor);
                    isFound = true;
                    let text = target + " Found at position " + (mid + 1);
                    document.getElementById("foundNotice").innerHTML = text;
                    await timer(time);
                    return target;
                } else if (data[mid] < target) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
                // changing initial smallest bar color
                await timer(time);
            }
            if (!isFound) {
                document.getElementById("foundNotice").innerHTML =
                    target + " doesn't exist.";
            }
            // after complete sorting complete making all the bar green 
            isSorting = false;
        }

        // calling async function here
        search(this);
    },
    interpolationSearch() {
        const timer = (ms) => new Promise((res) => setTimeout(res, ms));
        async function search() {
            let low = 0;
            let high = data.length - 1;
            let pos;
            while (low <= high && target >= data[low] && target <= data[high]) {
                pos = Math.floor(
                    low + ((target - data[low]) * (high - low)) / (data[high] - data[low])
                ) || 0;
                await timer(time);
                changeBarColor(data[pos], traverseColor);
                if (data[pos] === target) {
                    changeBarColor(data[pos], sortedColor);
                    isFound = true;
                    let text = target + " Found at position " + (pos + 1);
                    document.getElementById("foundNotice").innerHTML = text;
                    await timer(time);
                    return target;
                }
                if (data[pos] < target) {
                    low = pos + 1;
                } else {
                    high = pos - 1;
                }
                await timer(time);
            }
            if (!isFound) {
                document.getElementById("foundNotice").innerHTML =
                    target + " doesn't exist.";
            }
            // after complete sorting complete making all the bar green 
            isSorting = false;
        }
        // calling async function here
        search(this);
    },
    jumpSearch() {
        const timer = (ms) => new Promise((res) => setTimeout(res, ms));
        async function search() {
            const n = data.length;
            const step = Math.floor(Math.sqrt(n));
            let prev = 0;
            let current = step;
            // Finding the block where the element is present
            while (current < n && data[current] < target) {
                changeBarColor(data[prev], traverseColor);
                changeBarColor(data[current], traverseColor);
                prev = current;
                current += step;
                await timer(time);
            }
            while (prev <= Math.min(current, n)) {
                if (data[prev] === target) {
                    changeBarColor(data[prev], sortedColor);
                    isFound = true;
                    let text = target + " Found at position " + (prev + 1);
                    document.getElementById("foundNotice").innerHTML = text;
                    await timer(time);
                }
                prev++;
            }
            if (!isFound) {
                document.getElementById("foundNotice").innerHTML =
                    target + " doesn't exist.";
            }
            // after complete sorting complete making all the bar green 
            isSorting = false;
        }
        search(this);
    },

};

function startSearching() {
    let algo = document.getElementById("get-algo").value;
    if (algo == "interpolation-search") {
        const interpolationSearchStarted = SearchAlgo.interpolationSearch.bind(SearchAlgo);
        interpolationSearchStarted();
    }
    if (algo == "binary-search") {
        const binarySearchStarted = SearchAlgo.binarySearch.bind(SearchAlgo);
        binarySearchStarted();
    }
    if (algo == "jump-search") {
        const jumpSearchStarted = SearchAlgo.jumpSearch.bind(SearchAlgo);
        jumpSearchStarted();
    }
}

document.getElementById("search").addEventListener("click", function() {
    target = parseInt(document.getElementById("targetValue").value);
    if (isNaN(target)) {
        alert("Please enter a valid number");
    } else {
        startSearching();
    }
});

document.getElementById("random-data").addEventListener("click", function() {
    svg.remove();
    var data = randomData(maxElement, dataRange);
    createChart(data);
});

document.getElementById("reset").addEventListener("click", function() {
    svg.remove();
    createChart(data)
})