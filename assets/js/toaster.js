// Initialize Notyf instance
const notyf = new Notyf({
    duration: 3000, // Default duration for all toasts
    position: { x: 'right', y: 'top' }, // Toast position
    dismissible: true, // Allow users to dismiss toasts manually
});

// Function to handle toast notifications
function showToast(message, tag) {
    if (tag === 'success') {
        notyf.success(message);
    } else if (tag === 'info') {
        notyf.open({ type: 'info', message: message });
    } else if (tag === 'warning') {
        notyf.warning(message);
    } else if (tag === 'error') {
        notyf.error(message);
    } else {
        // Default for unsupported tags
        console.warn(`Unhandled tag: ${tag}, displaying as info.`);
        notyf.open({ type: 'info', message: message });
    }
}

// Expose the function globally for custom JavaScript calls
window.showToast = showToast;
