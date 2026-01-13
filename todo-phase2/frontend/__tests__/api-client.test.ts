/**
 * Basic tests for the API client
 */

import { apiClient } from '../lib/api-client';
import { Task } from '../lib/types';

// Mock fetch globally
global.fetch = jest.fn();

describe('API Client', () => {
  beforeEach(() => {
    (global.fetch as jest.MockedFunction<typeof fetch>).mockClear();
  });

  it('should make a GET request to fetch tasks', async () => {
    const mockTasks: Task[] = [
      {
        id: 1,
        user_id: 'user123',
        title: 'Test Task',
        description: 'Test Description',
        completed: false,
        created_at: '2023-01-01T00:00:00Z',
        updated_at: '2023-01-01T00:00:00Z',
      }
    ];

    (global.fetch as jest.MockedFunction<typeof fetch>).mockResolvedValueOnce({
      json: () => Promise.resolve(mockTasks),
      ok: true,
    } as Response);

    const result = await apiClient.getTasks('user123');

    expect(result.data).toEqual(mockTasks);
    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:8000/api/user123/tasks',
      expect.objectContaining({
        headers: expect.objectContaining({
          'Content-Type': 'application/json',
        }),
      })
    );
  });

  it('should handle network errors gracefully', async () => {
    (global.fetch as jest.MockedFunction<typeof fetch>).mockRejectedValueOnce(
      new Error('Network error')
    );

    const result = await apiClient.getTasks('user123');

    expect(result.error).toContain('Network error');
  });
});