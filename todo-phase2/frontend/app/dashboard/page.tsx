'use client';

import { useState, useEffect, Suspense } from 'react';
import { authService } from '../../lib/auth';
import { apiClient } from '../../lib/api-client';
import { Task } from '../../lib/types';
import TaskList from '../../components/TaskList';
import AddTaskModal from '../../components/AddTaskModal';
import Navbar from '../../components/Navbar';

function TaskContent() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddModal, setShowAddModal] = useState(false);
  const [userId, setUserId] = useState<string | null>(null);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean | null>(null);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const authStatus = authService.isAuthenticated();
      setIsAuthenticated(authStatus);

      if (authStatus) {
        setUserId(authService.getUserId());
      }
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (userId) {
      fetchTasks();
    }
  }, [userId]);

  // Show auth error if not authenticated
  if (isAuthenticated === false) {
    return (
      <div className="flex flex-col items-center justify-center min-h-screen bg-black">
        <h1 className="text-2xl font-bold text-red-500 neon-text">AUTHENTICATION REQUIRED</h1>
        <p className="text-green-400 font-mono">Please log in to access your dashboard.</p>
        <button
          onClick={() => window.location.href = '/auth/signup'}
          className="mt-4 border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] py-2 px-4 rounded font-mono"
        >
          GO TO SIGNUP
        </button>
      </div>
    );
  }

  const fetchTasks = async () => {
    setLoading(true);
    const response = await apiClient.getTasks();

    if (response.data) {
      setTasks(response.data);
    } else if (response.error) {
      console.error('Error fetching tasks:', response.error);
      // In a real app, you might want to show an error message to the user
    }

    setLoading(false);
  };

  const handleAddTask = async (title: string, description?: string) => {
    const response = await apiClient.createTask({ title, description });

    if (response.data) {
      setTasks([...tasks, response.data]);
      setShowAddModal(false);
    } else if (response.error) {
      console.error('Error creating task:', response.error);
    }
  };

  const handleUpdateTask = async (taskId: number, title: string, description?: string) => {
    const response = await apiClient.updateTask(taskId, { title, description });

    if (response.data) {
      setTasks(tasks.map(task => task.id === taskId ? response.data! : task));
    } else if (response.error) {
      console.error('Error updating task:', response.error);
    }
  };

  const handleToggleComplete = async (taskId: number, completed: boolean) => {
    const response = await apiClient.toggleTaskCompletion(taskId, completed);

    if (response.data) {
      setTasks(tasks.map(task => task.id === taskId ? response.data! : task));
    } else if (response.error) {
      console.error('Error toggling task completion:', response.error);
    }
  };

  const handleDeleteTask = async (taskId: number) => {
    const response = await apiClient.deleteTask(taskId);

    if (!response.error) {
      setTasks(tasks.filter(task => task.id !== taskId));
    } else {
      console.error('Error deleting task:', response.error);
    }
  };

  return (
    <>
      {loading ? (
        <div className="flex flex-col items-center justify-center min-h-screen bg-black">
          <h1 className="text-4xl font-bold neon-text mb-4">TASK.DASHBOARD</h1>
          <p className="text-lg text-green-400 font-mono">LOADING SYSTEM...</p>
        </div>
      ) : (
        <div className="bg-gray-900 rounded-lg border border-green-500 p-6 mb-8">
          <div className="flex flex-col sm:flex-row justify-between items-center gap-4">
            <div>
              <h2 className="text-2xl font-bold neon-text">ACTIVE_TASKS</h2>
              <p className="text-green-400 mt-1 font-mono">
                COUNT: {tasks.length} {tasks.length === 1 ? 'task' : 'tasks'} online
              </p>
            </div>
            <button
              onClick={() => setShowAddModal(true)}
              className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41]  hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] py-3 px-6 rounded font-mono flex items-center gap-2 hover:scale-105 transition-all duration-300 "
            >
              <svg className="w-5 h-5" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
              </svg>
              ADD_TASK
            </button>
          </div>
        </div>
      )}

      <div className="bg-gray-900 rounded-lg border border-green-500 p-6">
        {tasks.length === 0 ? (
          <div className="text-center py-16">
            <div className="mx-auto w-24 h-24 bg-gray-800 rounded-full flex items-center justify-center mb-6 border border-green-500">
              <svg className="w-12 h-12 text-green-400" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h3 className="text-2xl font-semibold neon-text mb-2">NO_TASKS_FOUND</h3>
            <p className="text-green-400 mb-6 font-mono">INITIALIZE YOUR FIRST TASK</p>
            <button
              onClick={() => setShowAddModal(true)}
              className="border border-green-500 bg-black text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] py-3 px-6 rounded font-mono"
            >
              CREATE_FIRST_TASK
            </button>
          </div>
        ) : (
          <TaskList
            tasks={tasks}
            onUpdateTask={handleUpdateTask}
            onToggleComplete={handleToggleComplete}
            onDeleteTask={handleDeleteTask}
          />
        )}
      </div>

      {showAddModal && (
        <AddTaskModal
          onClose={() => setShowAddModal(false)}
          onAddTask={handleAddTask}
        />
      )}
    </>
  );
}

export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-black matrix-bg pt-16"> {/* Added pt-16 to account for fixed navbar */}
      <Navbar onLogout={() => {
        // Force a refresh to update the UI after logout
        window.location.href = '/';
      }} />

      <div className="max-w-5xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        <div className="text-center mb-10">
          <h1 className="text-4xl font-extrabold neon-text sm:text-5xl">
            TASK.DASHBOARD
          </h1>
          <p className="mt-3 text-xl text-green-400 font-mono">
            SYSTEM.ACTIVE - ORGANIZE.YOUR.TASKS
          </p>
        </div>

        <Suspense fallback={
          <div className="bg-gray-900 rounded-lg border border-green-500 p-6">
            <div className="flex flex-col items-center justify-center py-12">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-green-500 mb-4"></div>
              <p className="text-green-400 font-mono">LOADING_TASKS...</p>
            </div>
          </div>
        }>
          <TaskContent />
        </Suspense>
      </div>
    </div>
  );
}