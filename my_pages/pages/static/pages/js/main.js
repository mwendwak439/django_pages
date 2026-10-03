// Log when page loads (check console)
console.log('Django pages app loaded ✅');

// Confirm before deleting anything
document.addEventListener('DOMContentLoaded', () => {
    const deleteLinks = document.querySelectorAll('a[href*="delete"]');
    deleteLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            if (!confirm('Are you sure you want to delete this?')) {
                e.preventDefault();
            }
        });
    });
});