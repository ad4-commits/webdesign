import os
import sys

print("=== DEBUG START ===")
print("Current directory:", os.getcwd())
print("Python version:", sys.version)
print("Arguments:", sys.argv)

# Try to import and run the main function
try:
    from main import main
    print("Main function imported successfully")
    main()
except Exception as e:
    print("ERROR:", e)
    import traceback
    traceback.print_exc()

print("=== DEBUG END ===")
