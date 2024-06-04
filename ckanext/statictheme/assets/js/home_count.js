document.addEventListener('DOMContentLoaded', function () {
    // Get the dataset count from the data attribute
    const datasetCountElement = document.getElementById('dataset-count');
    const datasetCount = parseInt(datasetCountElement.getAttribute('data-dataset-count'), 10);

    // Proceed with the animation using the datasetCount
    animateCount(0, datasetCount, 500); // Animate over 500 milliseconds

    function animateCount(start, end, duration) {
        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            const currentCount = Math.floor(progress * (end - start) + start);
            datasetCountElement.innerText = currentCount.toLocaleString(); // Format with commas
            if (progress < 1) {
                window.requestAnimationFrame(step);
            }
        };
        window.requestAnimationFrame(step);
    }
});
