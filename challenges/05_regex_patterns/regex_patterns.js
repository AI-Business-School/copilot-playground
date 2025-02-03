// Example 1: Email Validation
/**
 * Creates a regex pattern that validates email addresses with the following rules:
 * - Contains exactly one @ symbol
 * - Local part can contain letters, numbers, dots, and underscores
 * - Domain part can contain letters, numbers, dots, and hyphens
 * - Must end with a valid TLD (2-6 characters)
 * @param {string} email - Email address to validate
 * @returns {boolean} - Whether the email is valid
 */
function validateEmail(email) {
    const pattern = /^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}$/;
    return pattern.test(email);
}

// Example 2: Phone Number Format
/**
 * Creates a regex pattern that formats phone numbers:
 * - Input can be any string of 10 digits
 * - Output should be in format: (XXX) XXX-XXXX
 * - Should handle inputs with or without existing formatting
 * @param {string} phone - Phone number to format
 * @returns {string} - Formatted phone number
 */
function formatPhoneNumber(phone) {
    // First remove all non-digit characters
    const digitsOnly = phone.replace(/\D/g, '');
    if (digitsOnly.length !== 10) {
        throw new Error("Phone number must contain exactly 10 digits");
    }
    
    const pattern = /(\d{3})(\d{3})(\d{4})/;
    return digitsOnly.replace(pattern, '($1) $2-$3');
}

// Example 3: URL Parser
/**
 * Creates a regex pattern that parses URLs into components:
 * - Protocol (optional, defaults to http)
 * - Domain (required)
 * - Path (optional)
 * - Query parameters (optional)
 * @param {string} url - URL to parse
 * @returns {Object} - Parsed URL components
 */
function parseUrl(url) {
    const pattern = /^(?:(?<protocol>https?):\/\/)?(?<domain>[\w.-]+)(?<path>\/[\w\/.-]*)?(?:\?(?<query>[\w=&]+))?$/;
    const match = url.match(pattern);
    if (!match) {
        throw new Error("Invalid URL format");
    }
    
    return match.groups;
}

// Example 4: Custom Log Format
/**
 * Creates a regex pattern that parses log entries with format:
 * [YYYY-MM-DD HH:MM:SS] [LEVEL] Message (optional: {key1=value1, key2=value2})
 * Example: [2024-01-30 14:30:00] [INFO] User logged in {user_id=123, ip=192.168.1.1}
 * @param {string} logLine - Log line to parse
 * @returns {Object} - Parsed log components
 */
function parseLogEntry(logLine) {
    const pattern = /^\[(?<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(?<level>\w+)\] (?<message>[^{]+)(?:\s*{(?<metadata>.*)})?$/;
    const match = logLine.match(pattern);
    if (!match) {
        throw new Error("Invalid log format");
    }
    
    const result = match.groups;
    if (result.metadata) {
        const metadata = {};
        result.metadata.split(',').forEach(pair => {
            const [key, value] = pair.trim().split('=');
            metadata[key.trim()] = value.trim();
        });
        result.metadata = metadata;
    }
    return result;
} 