/**
 * Regex Helper Example
 * This file demonstrates how to use GitHub Copilot for generating and understanding regex patterns.
 * Each section contains regex patterns with explanations and test cases.
 */

class RegexHelper {
    /**
     * Email Validation Pattern
     * Ask questions about:
     * - How does this regex validate emails?
     * - What edge cases are handled?
     * - Why use this pattern over alternatives?
     * - How to customize for specific requirements?
     */
    static EMAIL_PATTERN = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    /**
     * URL Validation Pattern
     * Ask questions about:
     * - What URL formats are supported?
     * - How to handle international domains?
     * - What about query parameters?
     * - Security considerations?
     */
    static URL_PATTERN = /^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$/;

    /**
     * Password Strength Pattern
     * Ask questions about:
     * - What makes a password strong?
     * - How to balance security and usability?
     * - Common password patterns to reject?
     * - Best practices for validation?
     */
    static PASSWORD_PATTERN = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    /**
     * Date Format Pattern
     * Ask questions about:
     * - What date formats are supported?
     * - How to handle different separators?
     * - Validating date ranges?
     * - Localization considerations?
     */
    static DATE_PATTERN = /^(\d{4})-(\d{2})-(\d{2})$/;

    /**
     * Phone Number Pattern
     * Ask questions about:
     * - What formats are supported?
     * - International number handling?
     * - Extension support?
     * - Formatting considerations?
     */
    static PHONE_PATTERN = /^\+?1?\d{9,15}$/;

    /**
     * Validate an email address
     * @param {string} email - The email address to validate
     * @returns {boolean} True if valid, false otherwise
     */
    static validateEmail(email) {
        if (!email) return false;
        return this.EMAIL_PATTERN.test(email);
    }

    /**
     * Validate a URL
     * @param {string} url - The URL to validate
     * @returns {boolean} True if valid, false otherwise
     */
    static validateURL(url) {
        if (!url) return false;
        return this.URL_PATTERN.test(url);
    }

    /**
     * Validate password strength
     * @param {string} password - The password to validate
     * @returns {boolean} True if strong enough, false otherwise
     */
    static validatePassword(password) {
        if (!password) return false;
        return this.PASSWORD_PATTERN.test(password);
    }

    /**
     * Validate a date string (YYYY-MM-DD)
     * @param {string} date - The date string to validate
     * @returns {boolean} True if valid, false otherwise
     */
    static validateDate(date) {
        if (!date) return false;
        if (!this.DATE_PATTERN.test(date)) return false;
        
        const [_, year, month, day] = date.match(this.DATE_PATTERN);
        const d = new Date(year, month - 1, day);
        return d.getMonth() === month - 1 && d.getDate() === parseInt(day);
    }

    /**
     * Validate a phone number
     * @param {string} phone - The phone number to validate
     * @returns {boolean} True if valid, false otherwise
     */
    static validatePhone(phone) {
        if (!phone) return false;
        return this.PHONE_PATTERN.test(phone);
    }

    /**
     * Extract all email addresses from text
     * @param {string} text - The text to search
     * @returns {string[]} Array of found email addresses
     */
    static findEmails(text) {
        if (!text) return [];
        return text.match(this.EMAIL_PATTERN) || [];
    }

    /**
     * Extract all URLs from text
     * @param {string} text - The text to search
     * @returns {string[]} Array of found URLs
     */
    static findURLs(text) {
        if (!text) return [];
        return text.match(this.URL_PATTERN) || [];
    }

    /**
     * Format a phone number consistently
     * @param {string} phone - The phone number to format
     * @returns {string} Formatted phone number or original if invalid
     */
    static formatPhone(phone) {
        if (!phone) return '';
        const digits = phone.replace(/\D/g, '');
        if (digits.length === 10) {
            return digits.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3');
        }
        if (digits.length === 11) {
            return digits.replace(/(\d{1})(\d{3})(\d{3})(\d{4})/, '+$1 ($2) $3-$4');
        }
        return phone;
    }
}

// Example usage and test cases
const testCases = {
    emails: [
        'test@example.com',           // Valid
        'invalid.email@com',          // Invalid
        'user.name+tag@domain.com',   // Valid
        'no@domain',                  // Invalid
    ],
    urls: [
        'https://www.example.com',    // Valid
        'http://sub.domain.co.uk',    // Valid
        'invalid.com',                // Invalid
        'https://invalid',            // Invalid
    ],
    passwords: [
        'StrongPass123!',             // Valid
        'weakpass',                   // Invalid
        'NoDigits!',                  // Invalid
        'no_upper_1',                 // Invalid
    ],
    dates: [
        '2024-01-31',                // Valid
        '2024-13-01',                // Invalid
        '2024-04-31',                // Invalid
        '20240-01-01',               // Invalid
    ],
    phones: [
        '+1 (123) 456-7890',         // Valid
        '123-456-7890',              // Valid
        '1234567890',                // Valid
        '123-456-789',               // Invalid
    ]
};

// Run tests
Object.entries(testCases).forEach(([type, cases]) => {
    console.log(`\nTesting ${type}:`);
    cases.forEach(value => {
        const method = `validate${type.charAt(0).toUpperCase() + type.slice(1, -1)}`;
        const result = RegexHelper[method](value);
        console.log(`${value}: ${result ? 'Valid' : 'Invalid'}`);
    });
});

// Test extraction methods
const text = `
Contact us at support@example.com or sales@company.com
Visit our website: https://www.example.com
Phone: (123) 456-7890
`;

console.log('\nExtracted emails:', RegexHelper.findEmails(text));
console.log('Extracted URLs:', RegexHelper.findURLs(text));
console.log('Formatted phone:', RegexHelper.formatPhone('1234567890'));

// Questions to ask Copilot:
// 1. How does the email validation regex work?
// 2. What are the trade-offs in URL validation patterns?
// 3. How to modify the password pattern for different requirements?
// 4. What are the best practices for phone number validation?
// 5. How to handle international date formats?

// Practice exercises:
// 1. Ask Copilot to explain each regex pattern
// 2. Request variations for different requirements
// 3. Learn about regex performance implications
// 4. Understand common regex pitfalls
// 5. Explore alternative validation approaches

module.exports = RegexHelper; 