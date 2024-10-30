import * as dom from './dom';

declare global {
    interface Window {
        b741fef5: () => void;
    }
}

// Global functions
window.b741fef5 = dom.stopResub;
