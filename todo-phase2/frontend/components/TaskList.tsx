import React from 'react';
import { Task } from '@/lib/types';
import TaskCard from './TaskCard';

interface TaskListProps {
  tasks: Task[];
  onUpdateTask: (taskId: number, title: string, description?: string) => void;
  onToggleComplete: (taskId: number, completed: boolean) => void;
  onDeleteTask: (taskId: number) => void;
}

const TaskList: React.FC<TaskListProps> = ({ tasks, onUpdateTask, onToggleComplete, onDeleteTask }) => {
  if (tasks.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="mx-auto w-24 h-24 bg-gray-800 rounded-full flex items-center justify-center mb-6 border border-green-500">
          <svg className="w-12 h-12 text-green-400" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
        </div>
        <h3 className="mt-4 text-xl font-medium neon-text">NO TASKS INITIALIZED</h3>
        <p className="mt-2 text-green-400 font-mono">SYSTEM READY FOR INPUT</p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {tasks.map((task) => (
        <TaskCard
          key={task.id}
          task={task}
          onUpdate={onUpdateTask}
          onToggleComplete={onToggleComplete}
          onDelete={onDeleteTask}
        />
      ))}
    </div>
  );
};

export default TaskList;