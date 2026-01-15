try:
    import routes.auth
    print("Successfully imported routes.auth")
    print("Available endpoints:", [attr for attr in dir(routes.auth) if hasattr(getattr(routes.auth, attr), '__dict__')])
except Exception as e:
    print(f"Error importing routes.auth: {e}")

try:
    import routes.tasks
    print("Successfully imported routes.tasks")
    print("Router attribute exists:", hasattr(routes.tasks, 'router'))
except Exception as e:
    print(f"Error importing routes.tasks: {e}")

try:
    from main import app
    print("Successfully imported app from main")
    print("App routes:", [route.path for route in app.routes])
except Exception as e:
    print(f"Error importing app from main: {e}")