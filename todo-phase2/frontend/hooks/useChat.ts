import { useState, useCallback } from 'react';
import { apiClient, ChatMessage } from '../lib/api-client';

interface UseChatOptions {
  sessionId?: string;
}

interface UseChatReturn {
  messages: ChatMessage[];
  sendMessage: (message: string) => Promise<void>;
  isLoading: boolean;
  error: string | null;
  clearMessages: () => void;
}

export const useChat = (options: UseChatOptions = {}): UseChatReturn => {
  const { sessionId = 'default-session' } = options;
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const sendMessage = useCallback(async (message: string) => {
    if (!message.trim()) return;

    setIsLoading(true);
    setError(null);

    try {
      // Add user message optimistically
      const userMessage: ChatMessage = {
        id: Date.now().toString(),
        role: 'user',
        content: message,
        timestamp: new Date().toISOString(),
      };

      setMessages(prev => [...prev, userMessage]);

      // Send to API
      const response = await apiClient.sendMessage(message, sessionId);

      if (response.error) {
        throw new Error(response.error);
      }

      // Add AI response
      const aiMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: response.data?.response || 'Sorry, I encountered an error.',
        timestamp: response.data?.timestamp || new Date().toISOString(),
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (err) {
      console.error('Error sending message:', err);
      setError(err instanceof Error ? err.message : 'Failed to send message');

      // Add error message to chat
      const errorMessage: ChatMessage = {
        id: (Date.now() + 1).toString(),
        role: 'system',
        content: 'Sorry, I encountered an error. Please try again.',
        timestamp: new Date().toISOString(),
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  }, [sessionId]);

  const clearMessages = useCallback(() => {
    setMessages([]);
    setError(null);
  }, []);

  return {
    messages,
    sendMessage,
    isLoading,
    error,
    clearMessages,
  };
};