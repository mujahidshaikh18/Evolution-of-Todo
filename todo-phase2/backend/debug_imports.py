import sys
sys.path.insert(0, r'W:\Hackathon Cli\Evolution-of-Todo\todo-phase2\backend')

try:
    import routes.auth
    print("[OK] Successfully imported routes.auth")
    print(f"  Router: {hasattr(routes.auth, 'router')}")
    print(f"  Router type: {type(getattr(routes.auth, 'router', None))}")
    if hasattr(routes.auth, 'router'):
        print(f"  Router routes: {[route.path for route in routes.auth.router.routes]}")
except Exception as e:
    print(f"[ERROR] Failed to import routes.auth: {e}")

try:
    import routes.tasks
    print("[OK] Successfully imported routes.tasks")
    print(f"  Router: {hasattr(routes.tasks, 'router')}")
    print(f"  Router type: {type(getattr(routes.tasks, 'router', None))}")
    if hasattr(routes.tasks, 'router'):
        print(f"  Router routes: {[route.path for route in routes.tasks.router.routes]}")
except Exception as e:
    print(f"[ERROR] Failed to import routes.tasks: {e}")

# Now test main app
try:
    import main
    print("[OK] Successfully imported main")
    print(f"  App routes: {[route.path for route in main.app.routes]}")
except Exception as e:
    print(f"[ERROR] Failed to import main: {e}")