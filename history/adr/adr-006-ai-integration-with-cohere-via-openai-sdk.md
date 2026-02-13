# ADR-006: AI Integration with Cohere via OpenAI-Compatible SDK

## Status
Accepted

## Date
2026-02-03

## Context
The system needs to integrate with an AI provider for natural language processing capabilities to power the todo management chatbot. We need to decide which AI provider to use and how to integrate with their API. The requirements include using Cohere's API while maintaining compatibility with OpenAI SDK patterns for easier future migration if needed.

## Decision
We will use Cohere's command-r-plus model accessed through the OpenAI-compatible SDK interface. This means configuring the OpenAI SDK to point to Cohere's API endpoint (https://api.cohere.ai/v1/chat) while using OpenAI SDK patterns.

### Components
- **AI Provider**: Cohere (command-r-plus model)
- **SDK**: OpenAI SDK (configured for Cohere endpoint)
- **Configuration**: Environment variables (COHERE_API_KEY, COHERE_MODEL)

## Alternatives Considered

### Direct Cohere SDK
- **Pros**: Native support, potentially better performance, official documentation
- **Cons**: Lock-in to Cohere's API, different patterns than OpenAI, additional learning curve

### OpenAI GPT Models
- **Pros**: Familiar API, extensive documentation, proven reliability
- **Cons**: Different pricing model, doesn't meet requirement to use Cohere

### Anthropic Claude
- **Pros**: Strong reasoning capabilities, safety features
- **Cons**: Different API patterns, doesn't meet requirement to use Cohere

## Consequences

### Positive
- Leverages existing OpenAI SDK knowledge within the team
- Maintains flexibility to potentially switch back to OpenAI if requirements change
- Cohere's command-r-plus model is optimized for enterprise use cases
- Consistent with broader AI ecosystem patterns

### Negative
- Potential performance overhead from using OpenAI-compatible interface
- Possible incompatibilities between OpenAI and Cohere API features
- Additional complexity in configuration and error handling

## References
- specs/phase3/plan.md
- specs/phase3/spec.md