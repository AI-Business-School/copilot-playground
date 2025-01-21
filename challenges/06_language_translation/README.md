# Language Translation Examples

This directory demonstrates GitHub Copilot's ability to help with language translation and internationalization through practical examples in both JavaScript and Python. The examples showcase how to use Copilot to generate and understand translation patterns, formatting rules, and localization best practices.

## Learning Objectives

1. Learn how to use GitHub Copilot to implement translation and localization features
2. Understand different translation patterns and their use cases
3. Practice writing internationalization-ready code
4. Explore formatting rules for dates, numbers, and messages

## Directory Structure

```
javascript/
  translator.js     # JavaScript implementation of translation utilities
python/
  translator.py     # Python implementation of translation utilities
```

## Examples

### Translation Map

```javascript
// JavaScript
const translations = createTranslationMap();
translations.addTranslations("en", {
  greeting: "Hello, {name}!",
  items_count: {
    zero: "No items",
    one: "One item",
    other: "{count} items",
  },
});
```

```python
# Python
translations = create_translation_map()
translations['add_translations']('en', {
    'greeting': 'Hello, {name}!',
    'items_count': {
        'zero': 'No items',
        'one': 'One item',
        'other': '{count} items'
    }
})
```

### Date Formatting

```javascript
// JavaScript
const dateFormatter = createDateFormatter();
console.log(dateFormatter.format(new Date(), { dateStyle: "full" }));
console.log(dateFormatter.formatRelative(new Date()));
```

```python
# Python
date_formatter = create_date_formatter()
print(date_formatter['format'](datetime.now(), {'date_style': 'full'}))
print(date_formatter['format_relative'](datetime.now()))
```

### Number Formatting

```javascript
// JavaScript
const numberFormatter = createNumberFormatter();
console.log(numberFormatter.formatCurrency(1234.56, "USD"));
console.log(numberFormatter.formatUnit(5.7, "kilometer"));
```

```python
# Python
number_formatter = create_number_formatter()
print(number_formatter['format_currency'](1234.56, 'USD'))
print(number_formatter['format_unit'](5.7, 'kilometer'))
```

## Challenges

1. Implement complex pluralization rules for different languages
2. Add support for RTL (Right-to-Left) languages
3. Create a translation file management system
4. Implement context-dependent translations
5. Build a translation memory system

## Tips for Better Translations

1. Start with clear translation keys
2. Use placeholders consistently
3. Consider cultural differences
4. Handle pluralization rules
5. Implement fallback strategies

## What to Observe

1. How Copilot handles different locale formats
2. The way translation patterns are structured
3. Error handling in translations
4. Formatting rules for different locales
5. Internationalization best practices

## Learning Exercises

1. Write translation utilities

   - Create translation maps
   - Implement formatters
   - Handle edge cases

2. Implement formatting

   - Date formatting
   - Number formatting
   - Message formatting

3. Explore localization

   - RTL support
   - Cultural differences
   - Language-specific rules

4. Practice pluralization

   - Simple rules
   - Complex rules
   - Language variations

5. Document translations
   - Translation keys
   - Context information
   - Usage examples

## Questions to Ask

1. Translation Design

   - How should we structure translation keys?
   - What's the best way to handle variables?
   - Should we use nested translations?

2. Formatting Rules

   - How do we handle different date formats?
   - What about number systems?
   - How can we support various units?

3. Localization

   - How do we handle RTL languages?
   - What about cultural differences?
   - How can we manage multiple locales?

4. Best Practices

   - What's the most maintainable approach?
   - How can we ensure consistency?
   - Should we use translation management systems?

5. Implementation
   - How do we implement fallbacks?
   - What's the best way to handle missing translations?
   - How can we make translations more maintainable?
