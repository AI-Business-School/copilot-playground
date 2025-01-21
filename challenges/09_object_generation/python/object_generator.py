"""
Object Generation Example

This file demonstrates how to use GitHub Copilot to generate objects and factories.
Each method shows a different pattern for object creation and composition.
Your task is to use Copilot to help implement these patterns.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Any
from datetime import datetime

@dataclass
class Preferences:
    """User preferences with default values"""
    theme: str = 'light'
    notifications: bool = True
    language: str = 'en'

@dataclass
class User:
    """User object with validation and instance methods"""
    username: str
    email: str
    preferences: Preferences = field(default_factory=Preferences)
    id: int = field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True

    def __post_init__(self):
        """Validate required fields"""
        if not self.username or not self.email:
            raise ValueError("Username and email are required")
        # TODO: Implement email validation

    def update_preferences(self, **kwargs) -> 'User':
        """Update user preferences"""
        for key, value in kwargs.items():
            if hasattr(self.preferences, key):
                setattr(self.preferences, key, value)
        return self

    def deactivate(self) -> 'User':
        """Deactivate user account"""
        self.is_active = False
        return self

@dataclass
class Product:
    """Product object with inventory management"""
    name: str
    price: float
    category: str
    stock: int = 0
    tags: Set[str] = field(default_factory=set)
    id: int = field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate required fields"""
        if not self.name or self.price is None or not self.category:
            raise ValueError("Name, price, and category are required")
        if self.price < 0:
            raise ValueError("Price must be non-negative")

    def update_stock(self, quantity: int) -> 'Product':
        """Update product stock"""
        if self.stock + quantity < 0:
            raise ValueError("Insufficient stock")
        self.stock += quantity
        return self

    def add_tag(self, tag: str) -> 'Product':
        """Add a tag to the product"""
        self.tags.add(tag)
        return self

    def apply_discount(self, percentage: float) -> 'Product':
        """Apply a discount to the product price"""
        if percentage < 0 or percentage > 100:
            raise ValueError("Invalid discount percentage")
        self.price *= (1 - percentage / 100)
        return self

@dataclass
class CartItem:
    """Shopping cart item"""
    product_id: int
    name: str
    price: float
    quantity: int

@dataclass
class ShoppingCart:
    """Shopping cart with order management"""
    user_id: int
    items: List[CartItem] = field(default_factory=list)
    tax_rate: float = 0.1
    id: int = field(default_factory=lambda: int(datetime.now().timestamp() * 1000))
    created_at: datetime = field(default_factory=datetime.now)

    def add_item(self, product: Product, quantity: int = 1) -> 'ShoppingCart':
        """Add an item to the cart"""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        for item in self.items:
            if item.product_id == product.id:
                item.quantity += quantity
                return self

        self.items.append(CartItem(
            product_id=product.id,
            name=product.name,
            price=product.price,
            quantity=quantity
        ))
        return self

    def remove_item(self, product_id: int) -> 'ShoppingCart':
        """Remove an item from the cart"""
        self.items = [item for item in self.items if item.product_id != product_id]
        return self

    def get_subtotal(self) -> float:
        """Calculate cart subtotal"""
        return sum(item.price * item.quantity for item in self.items)

    def get_tax(self) -> float:
        """Calculate cart tax"""
        return self.get_subtotal() * self.tax_rate

    def get_total(self) -> float:
        """Calculate cart total"""
        return self.get_subtotal() + self.get_tax()

class ObjectGenerator:
    """Factory class for creating objects"""

    @staticmethod
    def create_user(
        username: str,
        email: str,
        preferences: Optional[Dict[str, Any]] = None
    ) -> User:
        """Create a user object"""
        prefs = Preferences(**preferences) if preferences else Preferences()
        return User(username=username, email=email, preferences=prefs)

    @staticmethod
    def create_product(
        name: str,
        price: float,
        category: str,
        stock: int = 0,
        tags: Optional[List[str]] = None
    ) -> Product:
        """Create a product object"""
        return Product(
            name=name,
            price=price,
            category=category,
            stock=stock,
            tags=set(tags or [])
        )

    @staticmethod
    def create_cart(
        user_id: int,
        items: Optional[List[CartItem]] = None,
        tax_rate: float = 0.1
    ) -> ShoppingCart:
        """Create a shopping cart object"""
        return ShoppingCart(
            user_id=user_id,
            items=items or [],
            tax_rate=tax_rate
        )

    @staticmethod
    def create_blog_post(
        title: str,
        content: str,
        author: 'Author',
        tags: Optional[List[str]] = None
    ) -> 'BlogPost':
        """
        TODO: Use GitHub Copilot to implement blog post creation with the following features:
        - Generate unique IDs for posts
        - Validate required fields (title, content, author)
        - Handle optional tags array
        - Format dates in ISO string format
        """
        # TODO: Use GitHub Copilot to implement blog post creation logic
        pass

    @staticmethod
    def convert_to_csv(
        data: List[Dict[str, Any]], 
        columns: Optional[List[str]] = None
    ) -> str:
        """
        TODO: Use GitHub Copilot to implement CSV conversion with the following features:
        - Handle empty arrays
        - Support custom column ordering
        - Escape values containing commas
        - Handle missing fields
        """
        # TODO: Use GitHub Copilot to implement CSV conversion logic
        pass

    @staticmethod
    def generate_profile_card(
        name: str,
        title: str,
        image: str,
        skills: Optional[List[str]] = None
    ) -> str:
        """
        TODO: Use GitHub Copilot to implement profile card generation with the following features:
        - Validate required fields (name, title, image)
        - Handle empty skills array
        - Properly escape HTML special characters
        - Maintain consistent indentation
        """
        # TODO: Use GitHub Copilot to implement profile card generation logic
        pass

    @staticmethod
    def generate_sql_query(
        table_name: str,
        fields: List[str],
        conditions: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        TODO: Use GitHub Copilot to implement SQL query generation with the following features:
        - Support multiple fields in SELECT
        - Handle IN conditions for arrays
        - Properly escape string values
        - Support multiple WHERE conditions
        """
        # TODO: Use GitHub Copilot to implement SQL query generation logic
        pass

def main():
    """Example usage"""
    # Create a user
    user = ObjectGenerator.create_user(
        username="john_doe",
        email="john@example.com",
        preferences={
            "theme": "dark",
            "notifications": False
        }
    )

    # Create a product
    product = ObjectGenerator.create_product(
        name="Laptop",
        price=999.99,
        category="Electronics",
        stock=10,
        tags=["computers", "tech"]
    )

    # Create a cart and add items
    cart = ObjectGenerator.create_cart(user_id=user.id)
    cart.add_item(product, 2)

    # Print results
    print("User:", user)
    print("Product:", product)
    print("Cart:", cart)
    print("Total:", cart.get_total())


if __name__ == "__main__":
    main()

# Challenges:
# 1. Create a blog post factory with comments and reactions
# 2. Implement a task manager with dependencies
# 3. Build a file system with folders and permissions 