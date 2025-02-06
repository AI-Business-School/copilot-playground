# Technical Design Exercise Guideline

This document provides guidelines for creating technical design solutions using GitHub Copilot.

## [Objective]

- Learn how to design scalable software systems
- Practice database schema design
- Understand system architecture patterns
- Master API design principles

## [Exercise Overview]

The exercises demonstrate three major system design challenges in both JavaScript and Python:

### 1. E-commerce Platform Design

```javascript
/**
 * System Components:
 * - User Management
 * - Product Catalog
 * - Shopping Cart
 * - Order Processing
 * - Payment Integration
 * - Inventory Management
 *
 * Technical Requirements:
 * - 100K daily active users
 * - Low latency search
 * - Real-time inventory
 * - Secure payments
 */

// Database Schema Example (Mongoose/SQLAlchemy):
class User {
  schema = {
    id: ObjectId,
    email: String,
    role: Enum[("customer", "seller", "admin")],
    profile: {
      name: String,
      addresses: Array,
    },
    auth: {
      password: String,
      lastLogin: Date,
    },
  };
}

class Product {
  schema = {
    id: ObjectId,
    name: String,
    category: ObjectId,
    price: Decimal,
    inventory: {
      quantity: Number,
      reserved: Number,
    },
    seller: ObjectId,
  };
}
```

### 2. Social Media Platform

```python
"""
Features:
- User Profiles
- Post Creation
- News Feed
- Notifications
- Messaging
- Moderation

Technical Requirements:
- Millions of users
- Real-time updates
- Content delivery
- Data privacy
"""

# Core Architecture Components:
class SocialPlatform:
    def __init__(self):
        self.cache = RedisCache()
        self.message_queue = RabbitMQ()
        self.storage = {
            'posts': PostStorage(),
            'users': UserStorage(),
            'media': CDNStorage()
        }

    async def generate_feed(self, user_id: int):
        """
        Feed Generation Algorithm:
        1. Get user connections
        2. Fetch recent posts
        3. Apply ranking
        4. Cache results
        """
```

### 3. Real-time Chat System

```javascript
/**
 * Features:
 * - 1:1 Messaging
 * - Group Chats
 * - Media Sharing
 * - Presence
 * - History
 * - E2E Encryption
 *
 * Technical Requirements:
 * - Low latency
 * - Offline support
 * - Multi-device
 * - Media storage
 */

class ChatSystem {
  constructor() {
    this.connections = new Map(); // WebSocket connections
    this.messageQueue = new MessageQueue();
    this.storage = new DistributedStorage();
  }

  async handleMessage(senderId, recipientId, content) {
    // 1. Encrypt message
    // 2. Store in database
    // 3. Send to online recipients
    // 4. Queue for offline recipients
  }
}
```

## [System Design Patterns]

1. Scalability Patterns:

   ```javascript
   // Horizontal Scaling
   class ServiceCluster {
     loadBalancer: HAProxy;
     instances: Array<ServiceNode>;
     healthChecks: HeartbeatMonitor;
   }

   // Caching Strategy
   class CacheLayer {
     l1: LocalCache; // In-memory, fast
     l2: RedisCache; // Distributed, persistent
     l3: DatabaseCache; // Fallback, complete
   }
   ```

2. Data Management:

   ```python
   # Data Partitioning
   class StorageManager:
       def partition_key(self, data):
           # Determine shard based on data
           return hash(data.user_id) % NUM_SHARDS

       def store_data(self, data):
           shard = self.get_shard(self.partition_key(data))
           shard.store(data)
   ```

3. Communication Patterns:

   ```javascript
   // Event-Driven Architecture
   class EventBus {
     publishers: Map<string, Publisher>;
     subscribers: Map<string, Subscriber[]>;
     messageQueue: MessageQueue;

     async publish(event, data) {
       await this.messageQueue.send(event, data);
       this.notifySubscribers(event, data);
     }
   }
   ```

## [Design Guidelines]

1. System Architecture:

   ```javascript
   // Layered Architecture
   class SystemArchitecture {
     presentation: {
       web: ReactApp,
       mobile: ReactNative,
       api: RESTGateway,
     };
     business: {
       services: MicroServices,
       workflows: EventProcessors,
     };
     data: {
       cache: DistributedCache,
       storage: DatabaseCluster,
       queue: MessageBroker,
     };
   }
   ```

2. API Design:

   ```python
   # RESTful Endpoints
   @api.route('/users')
   class UserAPI:
       def get(self, user_id):    # Read
           """GET /users/{id}"""

       def post(self):            # Create
           """POST /users"""

       def put(self, user_id):    # Update
           """PUT /users/{id}"""

       def delete(self, user_id): # Delete
           """DELETE /users/{id}"""
   ```

3. Database Design:
   ```javascript
   // Schema Design Principles
   class DatabaseSchema {
     // 1. Normalize for consistency
     // 2. Denormalize for performance
     // 3. Index for query optimization
     // 4. Partition for scalability
   }
   ```

## [Implementation Steps]

1. Requirements Analysis:

   - Functional requirements
   - Non-functional requirements
   - Scale estimations
   - Performance metrics

2. High-Level Design:

   - System components
   - Data flow
   - API contracts
   - Technology stack

3. Detailed Design:

   - Database schema
   - Service interfaces
   - Algorithm details
   - Security measures

4. Scalability Planning:
   - Caching strategy
   - Load balancing
   - Data partitioning
   - Failure handling

## [Practice Exercise]

1. Choose a system to design:

   - E-commerce platform
   - Social media system
   - Chat application

2. Design Steps:

   - Write requirements
   - Create architecture diagram
   - Design data models
   - Define API contracts
   - Plan scaling strategy

3. Implementation Focus:

   - Core components
   - Critical algorithms
   - Data structures
   - Performance optimization

4. Documentation:
   - Architecture overview
   - Component interactions
   - Data flow diagrams
   - API documentation
   - Scaling considerations

## [Best Practices]

1. Follow SOLID principles
2. Use appropriate design patterns
3. Consider maintainability
4. Plan for future growth
5. Document design decisions
6. Include monitoring and logging

## [Examples]

See `technical_design.js` and `technical_design.py` for practical examples of:

- E-commerce system design
- Social media platform architecture
- Content management system
- Real-time messaging platform
