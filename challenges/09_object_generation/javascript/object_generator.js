/**
 * Object Generation Example
 * 
 * This file demonstrates how to use GitHub Copilot to generate objects and factories.
 * Each method shows a different pattern for object creation and composition.
 * Your task is to use Copilot to help implement these patterns.
 */

class ObjectGenerator {
    /**
     * TODO: Use GitHub Copilot to implement a user object factory with validation and default values.
     * Try asking Copilot about:
     * 1. How to validate email format?
     * 2. What default values to use?
     * 3. How to handle optional fields?
     * 4. What methods should be included?
     */
    static createUser({ 
        username, 
        email, 
        preferences = {
            theme: 'light',
            notifications: true,
            language: 'en'
        }
    }) {
        // TODO: Use GitHub Copilot to implement email validation and user creation
        if (!username || !email) {
            throw new Error('Username and email are required');
        }

        return {
            id: Date.now(),
            username,
            email,
            preferences,
            createdAt: new Date(),
            isActive: true,

            // Instance methods
            updatePreferences(newPrefs) {
                this.preferences = { ...this.preferences, ...newPrefs };
                return this;
            },

            deactivate() {
                this.isActive = false;
                return this;
            }
        };
    }

    /**
     * TODO: Use GitHub Copilot to implement a product object factory with inventory management.
     * Try asking Copilot about:
     * 1. How to manage stock levels?
     * 2. What validation is needed?
     * 3. How to handle pricing?
     * 4. What about product variants?
     */
    static createProduct({
        name,
        price,
        category,
        stock = 0,
        tags = []
    }) {
        // TODO: Use GitHub Copilot to implement product validation and creation
        if (!name || price === undefined || !category) {
            throw new Error('Name, price, and category are required');
        }

        if (price < 0) {
            throw new Error('Price must be non-negative');
        }

        return {
            id: Date.now(),
            name,
            price,
            category,
            stock,
            tags: new Set(tags),
            createdAt: new Date(),

            // Instance methods
            updateStock(quantity) {
                if (this.stock + quantity < 0) {
                    throw new Error('Insufficient stock');
                }
                this.stock += quantity;
                return this;
            },

            addTag(tag) {
                this.tags.add(tag);
                return this;
            },

            applyDiscount(percentage) {
                if (percentage < 0 || percentage > 100) {
                    throw new Error('Invalid discount percentage');
                }
                this.price *= (1 - percentage / 100);
                return this;
            }
        };
    }

    /**
     * TODO: Use GitHub Copilot to implement a shopping cart factory with order management.
     * Try asking Copilot about:
     * 1. How to calculate totals?
     * 2. What about tax handling?
     * 3. How to manage quantities?
     * 4. What validation is needed?
     */
    static createCart({
        userId,
        items = [],
        taxRate = 0.1
    }) {
        // TODO: Use GitHub Copilot to implement cart creation and management
        return {
            id: Date.now(),
            userId,
            items: [...items],
            taxRate,
            createdAt: new Date(),

            // Instance methods
            addItem(product, quantity = 1) {
                if (quantity <= 0) {
                    throw new Error('Quantity must be positive');
                }

                const existingItem = this.items.find(item => item.productId === product.id);
                if (existingItem) {
                    existingItem.quantity += quantity;
                } else {
                    this.items.push({
                        productId: product.id,
                        name: product.name,
                        price: product.price,
                        quantity
                    });
                }
                return this;
            },

            removeItem(productId) {
                const index = this.items.findIndex(item => item.productId === productId);
                if (index !== -1) {
                    this.items.splice(index, 1);
                }
                return this;
            },

            getSubtotal() {
                return this.items.reduce((sum, item) => sum + item.price * item.quantity, 0);
            },

            getTax() {
                return this.getSubtotal() * this.taxRate;
            },

            getTotal() {
                return this.getSubtotal() + this.getTax();
            }
        };
    }
}

// Example usage
const user = ObjectGenerator.createUser({
    username: 'john_doe',
    email: 'john@example.com',
    preferences: {
        theme: 'dark',
        notifications: false
    }
});

const product = ObjectGenerator.createProduct({
    name: 'Laptop',
    price: 999.99,
    category: 'Electronics',
    stock: 10,
    tags: ['computers', 'tech']
});

const cart = ObjectGenerator.createCart({ userId: user.id });
cart.addItem(product, 2);

console.log('User:', user);
console.log('Product:', product);
console.log('Cart:', cart);
console.log('Total:', cart.getTotal());

module.exports = ObjectGenerator;

// Challenges:
// 1. Create a blog post factory with comments and reactions
// 2. Implement a task manager with dependencies
// 3. Build a file system with folders and permissions 