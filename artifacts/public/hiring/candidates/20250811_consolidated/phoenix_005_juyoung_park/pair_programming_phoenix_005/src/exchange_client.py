"""Abstract base class for exchange clients with resilience patterns."""

from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class ExchangeClient(ABC):
    """Abstract base class for cryptocurrency exchange clients.
    
    Provides common interface and resilience patterns for all exchange implementations.
    """
    
    def __init__(self, api_key: str, base_url: str, timeout: float = 30.0):
        """Initialize exchange client.
        
        Args:
            api_key: API key for authentication
            base_url: Base URL for the exchange API
            timeout: Request timeout in seconds
            
        TODO: Implement secure API key handling
        """
        # TODO: How should we securely handle the API key?
        # TODO: What validation should we do on base_url?
        pass
    
    @abstractmethod
    async def get_price(self, symbol: str) -> Dict[str, Any]:
        """Get current price for a trading symbol.
        
        Args:
            symbol: Trading pair symbol (e.g., 'BTCUSD')
            
        Returns:
            Dict containing price information
            
        Raises:
            ExchangeError: When API call fails
            ValidationError: When symbol is invalid
        """
        pass
    
    async def _make_request(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make HTTP request with resilience patterns.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            JSON response data
            
        TODO: Implement with retry logic and circuit breaker
        """
        # TODO: How should we implement exponential backoff with jitter?
        # TODO: When should the circuit breaker open/close?
        # TODO: What errors warrant retries vs immediate failure?
        pass
    
    def _validate_symbol(self, symbol: str) -> None:
        """Validate trading symbol format.
        
        Args:
            symbol: Symbol to validate
            
        Raises:
            ValidationError: If symbol format is invalid
            
        TODO: Implement symbol validation
        """
        # TODO: What makes a valid symbol?
        # TODO: Should this be configurable per exchange?
        pass


class ExchangeError(Exception):
    """Base exception for exchange-related errors."""
    pass


class ValidationError(ExchangeError):
    """Raised when input validation fails."""
    pass


class RetryableError(ExchangeError):
    """Raised when operation can be retried."""
    pass


class NonRetryableError(ExchangeError):
    """Raised when operation should not be retried."""
    pass