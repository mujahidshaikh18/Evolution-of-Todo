import sys
import os
sys.path.insert(0, r'W:\Hackathon Cli\Evolution-of-Todo\todo-phase2\backend')

# Test if we can import the routes
try:
    import routes.auth
    print("[OK] Successfully imported routes.auth")
    print(f"  Router object exists: {hasattr(routes.auth, 'router')}")
    if hasattr(routes.auth, 'router'):
        print(f"  Auth routes: {[route.path for route in routes.auth.router.routes]}")
except Exception as e:
    print(f"[ERROR] Error importing routes.auth: {e}")

try:
    import routes.tasks
    print("[OK] Successfully imported routes.tasks")
except Exception as e:
    print(f"[ERROR] Error importing routes.tasks: {e}")

# Now test the main app
try:
    import main
    print("\n[OK] Successfully imported main module")
    print(f"  App object exists: {hasattr(main, 'app')}")
    if hasattr(main, 'app'):
        print("  All registered routes:")
        for route in main.app.routes:
            if hasattr(route, 'path'):
                print(f"    {route.path}")
except Exception as e:
    print(f"[ERROR] Error importing main module: {e}")