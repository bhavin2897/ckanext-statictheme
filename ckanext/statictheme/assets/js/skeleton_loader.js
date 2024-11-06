document.addEventListener('DOMContentLoaded', function () {
    const skeletonLoaders = document.getElementById('skeleton-loaders');
    const searchResults = document.getElementById('search-results');

    skeletonLoaders.style.display = 'block'; // Show loader
    searchResults.style.display = 'none';

    // Simulate data fetch by monitoring page load
    setTimeout(() => {
        skeletonLoaders.style.display = 'none'; // Hide loader
        searchResults.style.display = 'block'; // Show actual content
    }, 2000); // Adjust timing as needed
});
