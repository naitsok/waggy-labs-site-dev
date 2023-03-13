(() => {
    'use strict'
    const highlightCategories = function(categoriesElem, visibleElems) {
        categoriesElem.querySelectorAll('a').forEach(element => {
            element.classList.remove('active');
        });
        const mostVisibleElem = mostVisible('.waggylabs-post-list-item');
        const postCategoriesElem = mostVisibleElem.querySelector('.waggylabs-post-categories');
        postCategoriesElem.querySelectorAll('span').forEach(element => {
            let catElem = categoriesElem.querySelector('a[data-slug="' + element.getAttribute('data-slug') + '"]');
            catElem.classList.add('active');
        });
    }

    window.addEventListener('DOMContentLoaded', function() {
        const categoriesElem = document.querySelector('.waggylabs-post-category-list');
        const postElems = document.querySelectorAll('.waggylabs-post-list-item');
        if (categoriesElem && postElems) {
            highlightCategories(categoriesElem, postElems);
            window.addEventListener('scroll', function() {
                highlightCategories(categoriesElem, postElems);
            });
        }
    });
})()