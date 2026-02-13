import React, { useState, useEffect } from 'react';
import { Task } from '@/lib/types';

interface EditTaskModalProps {
  task: Task;
  onClose: () => void;
  onSave: (title: string, description?: string) => void;
}

const EditTaskModal: React.FC<EditTaskModalProps> = ({ task, onClose, onSave }) => {
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description || '');
  const [isLoading, setIsLoading] = useState(false);
  const [errors, setErrors] = useState<{ title?: string; description?: string }>({});

  useEffect(() => {
    setTitle(task.title);
    setDescription(task.description || '');
    // Clear errors when task changes
    setErrors({});
  }, [task]);

  const validateInputs = (): boolean => {
    const newErrors: { title?: string; description?: string } = {};

    if (!title.trim()) {
      newErrors.title = 'Title is required';
    } else if (title.length < 1 || title.length > 200) {
      newErrors.title = 'Title must be between 1 and 200 characters';
    }

    if (description && description.length > 1000) {
      newErrors.description = 'Description must be less than 1000 characters';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateInputs()) {
      return;
    }

    setIsLoading(true);
    try {
      await onSave(title, description || undefined);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto">
      <div className="flex min-h-screen items-center justify-center p-4">
        <div className="fixed inset-0 bg-black opacity-70" onClick={onClose}></div>
        <div className="relative bg-gray-900 rounded-lg max-w-md w-full mx-auto p-6 shadow-xl border border-green-500" role="dialog" aria-modal="true" aria-labelledby="modal-title">
          <div className="absolute top-0 right-0 pt-4 pr-4">
            <button
              type="button"
              className="text-green-400 hover:text-green-300 focus:outline-none focus:ring-2 focus:ring-green-500 rounded-full p-1"
              onClick={onClose}
              aria-label="Close"
            >
              <span className="sr-only">Close</span>
              <svg className="h-6 w-6" fill="none" stroke="#00ff41" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div className="mt-2">
            <h3 className="text-lg font-medium neon-text" id="modal-title">
              EDIT_TASK
            </h3>
            <form onSubmit={handleSubmit} className="mt-4 space-y-4 font-mono">
              <div>
                <label htmlFor="edit-title-input" className="block text-sm font-medium text-green-400">
                  TITLE *
                </label>
                <input
                  type="text"
                  id="edit-title-input"
                  required
                  value={title}
                  onChange={(e) => {
                    setTitle(e.target.value);
                    // Clear error when user types
                    if (errors.title) {
                      setErrors(prev => ({ ...prev, title: undefined }));
                    }
                  }}
                  disabled={isLoading}
                  className={`mt-1 block w-full rounded border border-green-500 bg-black text-green-400 px-3 py-2 focus:border-green-400 focus:outline-none focus:ring-1 focus:ring-green-500 sm:text-sm font-mono ${
                    errors.title ? 'border-red-500 focus:ring-red-500 focus:border-red-500' : 'border-green-500'
                  } ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
                  maxLength={200}
                  aria-invalid={!!errors.title}
                  aria-describedby={errors.title ? 'edit-title-error' : undefined}
                />
                {errors.title && (
                  <p id="edit-title-error" className="mt-1 text-sm text-red-400">
                    {errors.title}
                  </p>
                )}
                <p className="mt-1 text-xs text-green-600">BETWEEN 1 AND 200 CHARACTERS</p>
              </div>
              <div>
                <label htmlFor="edit-description-input" className="block text-sm font-medium text-green-400">
                  DESCRIPTION
                </label>
                <textarea
                  id="edit-description-input"
                  rows={3}
                  value={description}
                  onChange={(e) => {
                    setDescription(e.target.value);
                    // Clear error when user types
                    if (errors.description) {
                      setErrors(prev => ({ ...prev, description: undefined }));
                    }
                  }}
                  disabled={isLoading}
                  className={`mt-1 block w-full rounded border border-green-500 bg-black text-green-400 px-3 py-2 focus:border-green-400 focus:outline-none focus:ring-1 focus:ring-green-500 sm:text-sm font-mono ${
                    errors.description ? 'border-red-500 focus:ring-red-500 focus:border-red-500' : 'border-green-500'
                  } ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
                  maxLength={1000}
                  aria-invalid={!!errors.description}
                  aria-describedby={errors.description ? 'edit-description-error' : undefined}
                ></textarea>
                {errors.description && (
                  <p id="edit-description-error" className="mt-1 text-sm text-red-400">
                    {errors.description}
                  </p>
                )}
                <p className="mt-1 text-xs text-green-600">OPTIONAL, MAXIMUM 1000 CHARACTERS</p>
              </div>
              <div className="flex justify-end space-x-3">
                <button
                  type="button"
                  onClick={onClose}
                  disabled={isLoading}
                  className="inline-flex justify-center rounded border border-green-500 bg-black px-4 py-2 text-sm font-mono text-green-400 shadow-sm hover:bg-gray-800 focus:outline-none focus:ring-1 focus:ring-green-500 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  CANCEL
                </button>
                <button
                  type="submit"
                  disabled={isLoading}
<<<<<<< HEAD
                  className="inline-flex justify-center rounded border border-green-500 bg-black px-4 py-2 text-sm font-mono text-green-400 shadow-[0_0_5px_#00ff41,_0_0_10px_#00ff41] transition-all duration-300 hover:bg-black/100 hover:shadow-[0_0_10px_#00ff41,_0_0_20px_#00ff41] focus:outline-none focus:ring-1 focus:ring-green-500 disabled:opacity-50 disabled:cursor-not-allowed"
=======
                  className="inline-flex justify-center rounded border border-transparent bg-black px-4 py-2 text-sm font-mono text-green-400 shadow-sm neon-button hover:bg-gray-800 focus:outline-none focus:ring-1 focus:ring-green-500 disabled:opacity-50 disabled:cursor-not-allowed"
>>>>>>> be27deab3d3f566b1231b8e6365d105beb813b09
                >
                  {isLoading ? (
                    <span className="flex items-center">
                      <svg className="animate-spin -ml-1 mr-2 h-4 w-4" stroke="#00ff41" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="#00ff41" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="#00ff41" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      SAVING...
                    </span>
                  ) : (
                    'SAVE_CHANGES'
                  )}
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EditTaskModal;