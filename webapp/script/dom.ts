// Stop the form resubmission on page refresh
export function stopResub(): void {
    window.history.replaceState(null, '', window.location.href);
}
