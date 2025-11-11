// Main JavaScript file for SQL-DAX-Python Helper

document.addEventListener('DOMContentLoaded', function() {
    console.log('SQL-DAX-Python Helper loaded successfully!');
    
    // Add active class to current nav item
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        if (link.pathname === currentPath) {
            link.style.color = '#3498db';
        }
    });
});
