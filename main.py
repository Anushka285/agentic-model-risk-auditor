from src.monitoring import run_monitoring
import json

if __name__ == "__main__":
    incident = run_monitoring()
    print("\n=== Monitoring Run Completed ===\n")
    print(json.dumps(incident, indent=2))
