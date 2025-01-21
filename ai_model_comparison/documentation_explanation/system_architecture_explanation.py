"""
Exercise: Microservices Architecture Analysis and Documentation

Context:
Below is a complex microservices-based e-commerce system implementation.
The task is to analyze and provide comprehensive documentation for this architecture.

class OrderService:
    def __init__(self, event_bus, inventory_client, payment_client):
        self.event_bus = event_bus
        self.inventory_client = inventory_client
        self.payment_client = payment_client
        
    async def process_order(self, order_data: Dict) -> OrderResult:
        try:
            # Validate inventory
            inventory_result = await self.inventory_client.check_availability(
                order_data['items']
            )
            if not inventory_result.is_available:
                raise InventoryException("Items not available")
                
            # Process payment
            payment_result = await self.payment_client.process_payment(
                order_data['payment_info']
            )
            if not payment_result.is_successful:
                raise PaymentException("Payment failed")
                
            # Reserve inventory
            await self.inventory_client.reserve_items(order_data['items'])
            
            # Publish events
            await self.event_bus.publish(
                "order.created",
                {"order_id": order_data['id']}
            )
            
            return OrderResult(success=True)
            
        except Exception as e:
            await self.handle_failure(e, order_data)
            raise OrderProcessingException(str(e))

Documentation Requirements:
1. System Overview
   - Architecture explanation
   - Design patterns used
   - System components and their interactions
   - Data flow analysis

2. Technical Details
   - Async processing explanation
   - Error handling strategies
   - Event-driven architecture patterns
   - Scalability considerations

3. Implementation Analysis
   - Code structure and organization
   - Error handling mechanisms
   - Dependency management
   - Transaction management

4. Best Practices Discussion
   - Microservices patterns
   - Resilience patterns
   - Monitoring considerations
   - Security implications

Compare how each AI model:
- Explains technical concepts
- Provides real-world analogies
- Structures documentation
- Addresses different audience levels
- Highlights important implementation details
- Discusses architectural trade-offs
""" 