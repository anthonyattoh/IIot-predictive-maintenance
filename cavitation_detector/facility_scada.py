import time
import random
import requests

# 1. FACILITY THRESHOLDS (Our Safety Limits)
THRESHOLDS = {
    "ROTATING": {"vibration_limit": 7.5, "displacement_limit": 1.2},
    "FLUID": {"pressure_drop_limit": 15.0, "acoustic_limit": 65.0},
    "TRIBOLOGY": {"particle_count_limit": 120, "water_content_limit": 0.05},
    "ELECTRICAL": {"current_imbalance_limit": 5.0, "hotspot_temp_limit": 80.0},
    "STATIC": {"min_wall_thickness_mm": 4.0} # If metal gets thinner than 4mm, it's a hazard
}

# Webhook for automation routing
WEBHOOK_URL = "import time"
import random
import requests

# 1. FACILITY THRESHOLDS (Our Safety Limits)
THRESHOLDS = {
    "ROTATING": {"vibration_limit": 7.5, "displacement_limit": 1.2},
    "FLUID": {"pressure_drop_limit": 15.0, "acoustic_limit": 65.0},
    "TRIBOLOGY": {"particle_count_limit": 120, "water_content_limit": 0.05},
    "ELECTRICAL": {"current_imbalance_limit": 5.0, "hotspot_temp_limit": 80.0},
    "STATIC": {"min_wall_thickness_mm": 4.0} # If metal gets thinner than 4mm, it's a hazard
}

import os

# Securely pull the webhook URL from the environment; fallback to a dummy string if missing
WEBHOOK_URL = os.environ.get("MAKE_WEBHOOK_URL", "https://fallback.local/no-key-provided")

# 2. MULTI-VARIABLE DIAGNOSTIC ENGINE
def analyze_facility_health(telemetry):
    """
    Accepts a dictionary of all facility assets, applies specific cross-sensor 
    logic for each, and compiles an array of active failure alerts.
    """
    active_alerts = []

    # Subsystem A: Rotating Machinery
    rot = telemetry["ROTATING_MACHINERY"]
    if rot["vibration"] > THRESHOLDS["ROTATING"]["vibration_limit"] and rot["displacement"] > THRESHOLDS["ROTATING"]["displacement_limit"]:
        active_alerts.append(f"ROTATING CRITICAL: Shaft Misalignment & Bearing Wear detected (Vib: {rot['vibration']:.1f}mm/s)")

    # Subsystem B: Process & Fluid Dynamics
    fluid = telemetry["PROCESS_FLUIDS"]
    if fluid["acoustic_emission"] > THRESHOLDS["FLUID"]["acoustic_limit"] and fluid["pressure_drop"] > THRESHOLDS["FLUID"]["pressure_drop_limit"]:
        active_alerts.append("FLUID CRITICAL: Pipeline Integrity Breach / Severe Cavitation suspected!")

    # Subsystem C: Tribology (Lubrication Sumps)
    oil = telemetry["TRIBOLOGY_SUMP"]
    if oil["particle_count"] > THRESHOLDS["TRIBOLOGY"]["particle_count_limit"] and oil["water_content"] > THRESHOLDS["TRIBOLOGY"]["water_content_limit"]:
        active_alerts.append("LUBRICATION CRITICAL: Seal Breach resulting in internal gear grinding.")

    # Subsystem D: Electrical Drives
    elec = telemetry["ELECTRICAL_DRIVE"]
    if elec["current_imbalance"] > THRESHOLDS["ELECTRICAL"]["current_imbalance_limit"] or elec["hotspot_temp"] > THRESHOLDS["ELECTRICAL"]["hotspot_temp_limit"]:
        active_alerts.append(f"ELECTRICAL WARNING: Motor phase imbalance or Switchgear Overheating ({elec['hotspot_temp']:.1f}°C)")

    # Subsystem E: Static Equipment (Vessels/Tanks)
    static = telemetry["STATIC_VESSEL"]
    if static["wall_thickness"] < THRESHOLDS["STATIC"]["min_wall_thickness_mm"]:
        active_alerts.append(f"STATIC CRITICAL: Severe Wall Thinning detected via Ultrasonic Gauge ({static['wall_thickness']:.2f}mm)")

    return active_alerts

# 3. FACILITY DATA SIMULATOR
def generate_facility_telemetry():
    """Generates an organized data structure matching the sensor matrix."""
    return {
        "ROTATING_MACHINERY": {
            "vibration": random.uniform(2.0, 9.0),
            "displacement": random.uniform(0.1, 1.5)
        },
        "PROCESS_FLUIDS": {
            "pressure_drop": random.uniform(5.0, 25.0),
            "flow_speed": random.uniform(10.0, 50.0),
            "acoustic_emission": random.uniform(30.0, 80.0)
        },
        "TRIBOLOGY_SUMP": {
            "dielectric_change": random.uniform(0.0, 2.0),
            "particle_count": random.randint(20, 150),
            "water_content": random.uniform(0.01, 0.08)
        },
        "ELECTRICAL_DRIVE": {
            "current_imbalance": random.uniform(0.5, 6.0),
            "harmonic_distortion": random.uniform(1.0, 8.0),
            "hotspot_temp": random.uniform(40.0, 90.0)
        },
        "STATIC_VESSEL": {
            "wall_thickness": random.uniform(3.5, 8.0) # Gradually eroding down
        }
    }

# 4. MAIN EXECUTIVE LOOP
print("=========================================================")
print("   INITIALIZING SCADA PREDICTIVE MAINTENANCE MONITOR     ")
print("=========================================================\n")

try:
    while True:
        # 1. Scrape data from all "field sensors"
        live_data = generate_facility_telemetry()
        
        # 2. Run diagnostics
        faults_found = analyze_facility_health(live_data)
        
        # 3. Log results to screen
        print(f"--- [SCAN TIMESTAMP: {time.strftime('%H:%M:%S')}] ---")
        print(f" Rotating Vib: {live_data['ROTATING_MACHINERY']['vibration']:.1f} mm/s | Static Wall: {live_data['STATIC_VESSEL']['wall_thickness']:.2f} mm")
        print(f" Fluid Acoustic: {live_data['PROCESS_FLUIDS']['acoustic_emission']:.1f} dB | Oil Water Content: {live_data['TRIBOLOGY_SUMP']['water_content']*100:.1f}%")
        
        if faults_found:
            print("\n🚨 SYSTEM ALERTS DETECTED:")
            for fault in faults_found:
                print(f" -> {fault}")
            
            # Send the complete nested payload to Make.com
            try:
                requests.post(WEBHOOK_URL, json={"facility_status": "ANOMALY", "alerts": faults_found, "raw_data": live_data}, timeout=5)
                print("⚡ Cloud Sync: Transmitted multi-asset diagnostic payload to Make.com pipeline.")
            except requests.exceptions.RequestException:
                pass
        else:
            print("✅ All subsystems operating within safe baselines.")
            
        print("-" * 57 + "\n")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[INFO] Facility SCADA Monitor offline.")

# 2. MULTI-VARIABLE DIAGNOSTIC ENGINE
def analyze_facility_health(telemetry):
    """
    Accepts a dictionary of all facility assets, applies specific cross-sensor 
    logic for each, and compiles an array of active failure alerts.
    """
    active_alerts = []

    # Subsystem A: Rotating Machinery
    rot = telemetry["ROTATING_MACHINERY"]
    if rot["vibration"] > THRESHOLDS["ROTATING"]["vibration_limit"] and rot["displacement"] > THRESHOLDS["ROTATING"]["displacement_limit"]:
        active_alerts.append(f"ROTATING CRITICAL: Shaft Misalignment & Bearing Wear detected (Vib: {rot['vibration']:.1f}mm/s)")

    # Subsystem B: Process & Fluid Dynamics
    fluid = telemetry["PROCESS_FLUIDS"]
    if fluid["acoustic_emission"] > THRESHOLDS["FLUID"]["acoustic_limit"] and fluid["pressure_drop"] > THRESHOLDS["FLUID"]["pressure_drop_limit"]:
        active_alerts.append("FLUID CRITICAL: Pipeline Integrity Breach / Severe Cavitation suspected!")

    # Subsystem C: Tribology (Lubrication Sumps)
    oil = telemetry["TRIBOLOGY_SUMP"]
    if oil["particle_count"] > THRESHOLDS["TRIBOLOGY"]["particle_count_limit"] and oil["water_content"] > THRESHOLDS["TRIBOLOGY"]["water_content_limit"]:
        active_alerts.append("LUBRICATION CRITICAL: Seal Breach resulting in internal gear grinding.")

    # Subsystem D: Electrical Drives
    elec = telemetry["ELECTRICAL_DRIVE"]
    if elec["current_imbalance"] > THRESHOLDS["ELECTRICAL"]["current_imbalance_limit"] or elec["hotspot_temp"] > THRESHOLDS["ELECTRICAL"]["hotspot_temp_limit"]:
        active_alerts.append(f"ELECTRICAL WARNING: Motor phase imbalance or Switchgear Overheating ({elec['hotspot_temp']:.1f}°C)")

    # Subsystem E: Static Equipment (Vessels/Tanks)
    static = telemetry["STATIC_VESSEL"]
    if static["wall_thickness"] < THRESHOLDS["STATIC"]["min_wall_thickness_mm"]:
        active_alerts.append(f"STATIC CRITICAL: Severe Wall Thinning detected via Ultrasonic Gauge ({static['wall_thickness']:.2f}mm)")

    return active_alerts

# 3. FACILITY DATA SIMULATOR
def generate_facility_telemetry():
    """Generates an organized data structure matching the sensor matrix."""
    return {
        "ROTATING_MACHINERY": {
            "vibration": random.uniform(2.0, 9.0),
            "displacement": random.uniform(0.1, 1.5)
        },
        "PROCESS_FLUIDS": {
            "pressure_drop": random.uniform(5.0, 25.0),
            "flow_speed": random.uniform(10.0, 50.0),
            "acoustic_emission": random.uniform(30.0, 80.0)
        },
        "TRIBOLOGY_SUMP": {
            "dielectric_change": random.uniform(0.0, 2.0),
            "particle_count": random.randint(20, 150),
            "water_content": random.uniform(0.01, 0.08)
        },
        "ELECTRICAL_DRIVE": {
            "current_imbalance": random.uniform(0.5, 6.0),
            "harmonic_distortion": random.uniform(1.0, 8.0),
            "hotspot_temp": random.uniform(40.0, 90.0)
        },
        "STATIC_VESSEL": {
            "wall_thickness": random.uniform(3.5, 8.0) # Gradually eroding down
        }
    }

# 4. MAIN EXECUTIVE LOOP
print("=========================================================")
print("   INITIALIZING SCADA PREDICTIVE MAINTENANCE MONITOR     ")
print("=========================================================\n")

try:
    while True:
        # 1. Scrape data from all "field sensors"
        live_data = generate_facility_telemetry()
        
        # 2. Run diagnostics
        faults_found = analyze_facility_health(live_data)
        
        # 3. Log results to screen
        print(f"--- [SCAN TIMESTAMP: {time.strftime('%H:%M:%S')}] ---")
        print(f" Rotating Vib: {live_data['ROTATING_MACHINERY']['vibration']:.1f} mm/s | Static Wall: {live_data['STATIC_VESSEL']['wall_thickness']:.2f} mm")
        print(f" Fluid Acoustic: {live_data['PROCESS_FLUIDS']['acoustic_emission']:.1f} dB | Oil Water Content: {live_data['TRIBOLOGY_SUMP']['water_content']*100:.1f}%")
        
        if faults_found:
            print("\n🚨 SYSTEM ALERTS DETECTED:")
            for fault in faults_found:
                print(f" -> {fault}")
            
            # Send the complete nested payload to Make.com
            try:
                requests.post(WEBHOOK_URL, json={"facility_status": "ANOMALY", "alerts": faults_found, "raw_data": live_data}, timeout=5)
                print("⚡ Cloud Sync: Transmitted multi-asset diagnostic payload to Make.com pipeline.")
            except requests.exceptions.RequestException:
                pass
        else:
            print("✅ All subsystems operating within safe baselines.")
            
        print("-" * 57 + "\n")
        time.sleep(3)

except KeyboardInterrupt:
    print("\n[INFO] Facility SCADA Monitor offline.")