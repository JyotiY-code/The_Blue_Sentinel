# main.py
import acoustic_engine
import alerts

def sentinel_surveillance():
    print("--- The Blue Sentinel System Online ---")
    
    # 1.Taking information from engine 
    vessel, life, count, risk, pollution = acoustic_engine.analyze_full_environment()

    # 2. Security Check (Spying/Terrorism)
    if vessel == "Foreign Spy Vessel":
        alerts.send_coast_guard_alert(f"URGENT: {vessel} detected in sensitive zone!")

    # 3. Ecology Check (Pollution)
    if pollution == "High":
        alerts.send_coast_guard_alert(f"ECO-DANGER: Pollution detected near {count} {life}s!")

    # 4. Safety Check (Ship Sinking Risk)
    if risk:
        alerts.send_coast_guard_alert("SAFETY: Ship moving towards dangerous rocks/shallow waters.")

#  To run the system 
if __name__ == "__main__":
    sentinel_surveillance()
