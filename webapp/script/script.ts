import * as dom from './dom';

declare global {
    interface Window {
        stopResub: () => void;
    }
}

// Global functions
window.stopResub = dom.stopResub;
