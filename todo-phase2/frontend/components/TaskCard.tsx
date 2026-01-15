import React, { useState, useCallback } from 'react';
import { Task } from '../lib/types';
import EditTaskModal from './EditTaskModal';

interface TaskCardProps {
  task: Task;
  onUpdate: (taskId: number, title: string, description?: string) => void;
  onToggleComplete: (taskId: number, completed: boolean) => void;
  onDelete: (taskId: number) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onUpdate, onToggleComplete, onDelete }) => {
  const [showEditModal, setShowEditModal] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleToggleComplete = useCallback(() => {
    if (isLoading) return; // Prevent multiple clicks during loading
    setIsLoading(true);
    try {
      onToggleComplete(task.id, !task.completed);
    } finally {
      setIsLoading(false);
    }
  }, [task.id, task.completed, onToggleComplete, isLoading]);

  const handleUpdateTask = (title: string, description?: string) => {
    onUpdate(task.id, title, description);
    setShowEditModal(false);
  };

  const handleDelete = useCallback(() => {
    if (isLoading) return; // Prevent multiple clicks during loading
    if (window.confirm(`Are you sure you want to delete task "${task.title}"?`)) {
      setIsLoading(true);
      try {
        onDelete(task.id);
      } finally {
        setIsLoading(false);
      }
    }
  }, [task.id, task.title, onDelete, isLoading]);

  return (
    <li
      className={`bg-gray-900 rounded border border-green-500 p-5 transition-all duration-200 hover:shadow-lg ${isLoading ? 'opacity-75 cursor-not-allowed' : ''}`}
      aria-busy={isLoading}
    >
      <div className="flex items-start justify-between">
        <div className="flex items-start space-x-3">
          <input
            type="checkbox"
            checked={task.completed}
            onChange={handleToggleComplete}
            disabled={isLoading}
            className="mt-1 h-5 w-5 rounded bg-black border-green-500 text-green-400 checked:bg-black checked:border-green-500 focus:ring-green-500 focus:ring-2 focus:ring-offset-2 focus:ring-offset-black accent-green-500 disabled:opacity-50 cursor-pointer"
            aria-label={`Mark task ${task.title} as ${task.completed ? 'incomplete' : 'complete'}`}
          />
          <div className="min-w-0 flex-1">
            <p
              className={`text-base font-medium ${task.completed ? 'line-through text-green-600' : 'text-green-400'}`}
              aria-label={task.completed ? `${task.title}, completed` : `${task.title}, not completed`}
            >
              {task.title}
            </p>
            {task.description && (
              <p className={`mt-1 text-sm ${task.completed ? 'text-green-700' : 'text-green-500'}`} title={task.description}>
                {task.description}
              </p>
            )}
            <div className="mt-2 flex items-center text-xs text-green-600 font-mono">
              <svg className="mr-1 w-3 h-3" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <span>TIMESTAMP: {new Date(task.created_at).toLocaleString()}</span>
            </div>
          </div>
        </div>
        <div className="flex space-x-2 ml-4">
          <button
            onClick={() => setShowEditModal(true)}
            disabled={isLoading}
            className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] px-3 py-1.5 text-sm font-mono transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            aria-label={`Edit task ${task.title}`}
          >
            <svg className="w-4 h-4 mr-1 inline" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
            </svg>
            EDIT
          </button>
          <button
            onClick={handleDelete}
            disabled={isLoading}
            className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] px-3 py-1.5 text-sm font-mono transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
            aria-label={`Delete task ${task.title}`}
          >
            <svg className="w-4 h-4 mr-1 inline" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
            DEL
          </button>
        </div>
      </div>

      {showEditModal && (
        <EditTaskModal
          task={task}
          onClose={() => setShowEditModal(false)}
          onSave={handleUpdateTask}
        />
      )}
    </li>
  );
};

export default TaskCard;