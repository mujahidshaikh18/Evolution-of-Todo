import React, { useState, useEffect } from 'react';
import ChatInterface from './ChatInterface';
import { motion, AnimatePresence } from 'framer-motion';

interface ChatContainerProps {
  isOpen: boolean;
  onClose: () => void;
  onTasksChanged?: () => void;
  onAddTask?: (title: string, description?: string) => Promise<void>;
  onUpdateTask?: (taskId: number, title: string, description?: string) => Promise<void>;
  onDeleteTask?: (taskId: number) => Promise<void>;
  onToggleComplete?: (taskId: number, completed: boolean) => Promise<void>;
}

const ChatContainer: React.FC<ChatContainerProps> = ({
  isOpen,
  onClose,
  onTasksChanged,
  onAddTask,
  onUpdateTask,
  onDeleteTask,
  onToggleComplete
}) => {
  const [isVisible, setIsVisible] = useState(isOpen);

  useEffect(() => {
    if (isOpen) {
      setIsVisible(true);
    }
  }, [isOpen]);

  const handleClose = () => {
    setIsVisible(false);
    setTimeout(onClose, 300); // Match the animation duration
  };

  return (
    <AnimatePresence>
      {isVisible && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm"
          onClick={handleClose}
        >
          <motion.div
            initial={{ scale: 0.8, y: 50 }}
            animate={{ scale: 1, y: 0 }}
            exit={{ scale: 0.8, y: 50 }}
            className="w-full max-w-2xl h-[600px] flex flex-col bg-gray-900 border-2 border-cyan-500 rounded-xl shadow-2xl shadow-cyan-500/30 overflow-hidden"
            onClick={(e) => e.stopPropagation()} // Prevent clicks inside the container from closing it
          >
            {/* Header */}
            <div className="flex justify-between items-center p-4 bg-gradient-to-r from-purple-900/80 to-cyan-900/80 border-b border-cyan-500">
              <h2 className="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-400">
                AI Task Manager
              </h2>
              <button
                onClick={handleClose}
                className="text-gray-300 hover:text-white transition-colors"
                aria-label="Close chat"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>

            {/* Chat Interface */}
            <div className="flex-1 p-4">
              <ChatInterface
                onTasksChanged={onTasksChanged}
                onAddTask={onAddTask}
                onUpdateTask={onUpdateTask}
                onDeleteTask={onDeleteTask}
                onToggleComplete={onToggleComplete}
              />
            </div>

            {/* Footer */}
            <div className="p-3 bg-gray-900/50 border-t border-cyan-500/30 text-center">
              <p className="text-xs text-cyan-400/70">
                Powered by Cohere AI • Your tasks are securely managed
              </p>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};

export default ChatContainer;