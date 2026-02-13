import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface Message {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
}

interface ChatInterfaceProps {
  onTasksChanged?: () => void;
  onAddTask?: (title: string, description?: string) => Promise<void>;
  onUpdateTask?: (taskId: number, title: string, description?: string) => Promise<void>;
  onDeleteTask?: (taskId: number) => Promise<void>;
  onToggleComplete?: (taskId: number, completed: boolean) => Promise<void>;
}

const ChatInterface: React.FC<ChatInterfaceProps> = ({
  onTasksChanged,
  onAddTask,
  onUpdateTask,
  onDeleteTask,
  onToggleComplete
}) => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      role: 'assistant',
      content: 'Hello! I\'m your AI assistant. How can I help you manage your tasks today?',
      timestamp: new Date().toISOString(),
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Effect to handle task refresh when tool messages indicate success
  useEffect(() => {
    // Check the last message to see if it's a tool success message
    const lastMessage = messages[messages.length - 1];
    if (lastMessage && lastMessage.role === 'tool' && typeof lastMessage.content === 'object' && lastMessage.content.success) {
      // If the tool operation was successful, trigger a refresh of tasks
      if (onTasksChanged) {
        // Add a small delay to ensure the UI updates properly
        setTimeout(() => {
          onTasksChanged();
        }, 500);
      }
    }
  }, [messages, onTasksChanged]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleSendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: inputValue.trim(),
      timestamp: new Date().toISOString(),
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the backend API at port 8000
      const response = await fetch('http://localhost:8000/api/chat/converse', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('better_auth_token') || localStorage.getItem('token')}` // Better Auth token
        },
        body: JSON.stringify({
          message: inputValue.trim(),
          session_id: 'default-session', // In a real app, use actual session ID
          user_id: localStorage.getItem('user_id') || 'default-user' // In a real app, use actual user ID
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();

      // Execute any frontend tool operations directly from callbacks
      if (data.tool_calls && data.tool_calls.length > 0) {
        for (const toolCall of data.tool_calls) {
          const { name, parameters } = toolCall;
          try {
            switch (name) {
              case 'create_task':
                if (onAddTask) {
                  await onAddTask(parameters.title, parameters.description);
                }
                break;
              case 'update_task':
                if (onUpdateTask) {
                  await onUpdateTask(parameters.task_id, parameters.title, parameters.description);
                }
                break;
              case 'delete_task':
                if (onDeleteTask) {
                  await onDeleteTask(parameters.task_id);
                }
                break;
              case 'complete_task':
                if (onToggleComplete) {
                  await onToggleComplete(parameters.task_id, true);
                }
                break;
            }
          } catch (error) {
            console.error(`Error executing tool ${name}:`, error);
          }
        }
      }

      // Refresh tasks if needed
      if (data.refresh_tasks && onTasksChanged) {
        onTasksChanged();
      }

      // Add AI response
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'assistant',
        content: data.response,
        timestamp: new Date().toISOString(),
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);

      // Add error message
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        role: 'system',
        content: 'Sorry, I encountered an error. Please try again.',
        timestamp: new Date().toISOString(),
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="flex flex-col h-full bg-gray-900 border border-cyan-500 rounded-lg shadow-lg shadow-cyan-500/20 overflow-hidden">
      {/* Chat Header */}
      <div className="bg-gradient-to-r from-purple-900 to-cyan-900 p-4 border-b border-cyan-500">
        <h2 className="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-400">
          AI Task Assistant
        </h2>
        <p className="text-xs text-cyan-300">Powered by Cohere AI</p>
      </div>

      {/* Messages Container */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 max-h-[400px]">
        <AnimatePresence>
          {messages.map((message) => (
            <motion.div
              key={message.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className={`flex ${
                message.role === 'user' ? 'justify-end' : 'justify-start'
              }`}
            >
              <div
                className={`max-w-[80%] rounded-xl p-3 ${
                  message.role === 'user'
                    ? 'bg-gradient-to-r from-blue-600 to-indigo-700 text-white ml-auto'
                    : message.role === 'assistant'
                    ? 'bg-gradient-to-r from-gray-800 to-gray-700 text-cyan-100 border border-cyan-500/30'
                    : 'bg-gradient-to-r from-red-900/50 to-red-800/50 text-red-200 border border-red-500/30'
                }`}
              >
                <div className="whitespace-pre-wrap">{message.content}</div>
                <div className="text-xs mt-1 opacity-70">
                  {new Date(message.timestamp).toLocaleTimeString()}
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="border-t border-cyan-500/30 p-3 bg-gray-900">
        <div className="flex gap-2">
          <textarea
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask me to manage your tasks..."
            className="flex-1 bg-gray-800 border border-cyan-500/30 rounded-lg p-2 text-white placeholder-gray-400 resize-none focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:border-transparent"
            rows={2}
            disabled={isLoading}
          />
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleSendMessage}
            disabled={!inputValue.trim() || isLoading}
            className={`px-4 py-2 rounded-lg font-medium transition-colors ${
              inputValue.trim() && !isLoading
                ? 'bg-gradient-to-r from-cyan-600 to-blue-600 text-white hover:from-cyan-500 hover:to-blue-500'
                : 'bg-gray-700 text-gray-400 cursor-not-allowed'
            }`}
          >
            {isLoading ? (
              <span className="flex items-center">
                <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Sending...
              </span>
            ) : (
              'Send'
            )}
          </motion.button>
        </div>
        <div className="mt-2 text-xs text-cyan-400/70 text-center">
          Ask me to create, update, or manage your tasks using natural language
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;