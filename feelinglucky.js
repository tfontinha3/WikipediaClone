function feelingLucky() {
    const query = document.querySelector('.search-input').value;
    if (query) {
        const url = `https://www.google.com/search?q=${encodeURIComponent(query)}&btnI=I`;
        window.location.href = url;
    }
}