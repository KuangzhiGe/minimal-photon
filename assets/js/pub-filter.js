document.addEventListener("DOMContentLoaded", function() {
    const filters = document.querySelectorAll("#filters .btn");
    const publications = document.querySelectorAll(".bibliography li");

    filters.forEach(filter => {
        filter.addEventListener("click", function() {
            // Toggle active class on buttons
            filters.forEach(btn => btn.classList.remove("active"));
            this.classList.add("active");

            const filterValue = this.getAttribute("data-filter");

            publications.forEach(pub => {
                if (filterValue === "*" || pub.dataset.tags.includes(filterValue)) {
                    pub.style.display = "";
                } else {
                    pub.style.display = "none";
                }
            });
        });
    });
});