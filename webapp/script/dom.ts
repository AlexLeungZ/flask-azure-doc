// Get value from data tag
export function getValue(id: string): string | undefined {
    const value = document.getElementsByName(id).item(0) as HTMLDataElement | null;
    return value?.remove() ?? value?.value;
}

// Get form data from form tag
export function getForm(pop?: string[]): FormData {
    const element = document.querySelector('form') ?? undefined;
    const form = new FormData(element);
    pop?.forEach((r) => form.delete(r));
    return form;
}

// Stop the form resubmission on page refresh
export function stopResub(): void {
    window.history.replaceState(null, '', window.location.href);
}
