"""
Unit tests for analyze_facility_health() in facility_scada.py

Run with: pytest test_facility_scada.py
"""

from facility_scada import analyze_facility_health


def make_telemetry(vibration=3.0, displacement=0.3, wall_thickness=8.0,
                    particle_count=30, water_content=0.02,
                    pressure_drop=10.0, acoustic_emission=40.0,
                    current_imbalance=1.0, hotspot_temp=50.0):
    """Builds a full telemetry dict with sensible healthy defaults,
    so each test only needs to override the values it cares about."""
    return {
        "ROTATING_MACHINERY": {"vibration": vibration, "displacement": displacement},
        "PROCESS_FLUIDS": {"pressure_drop": pressure_drop, "flow_speed": 30.0, "acoustic_emission": acoustic_emission},
        "TRIBOLOGY_SUMP": {"dielectric_change": 1.0, "particle_count": particle_count, "water_content": water_content},
        "ELECTRICAL_DRIVE": {"current_imbalance": current_imbalance, "harmonic_distortion": 3.0, "hotspot_temp": hotspot_temp},
        "STATIC_VESSEL": {"wall_thickness": wall_thickness},
    }


def test_healthy_system_raises_no_alerts():
    telemetry = make_telemetry()
    alerts = analyze_facility_health(telemetry)
    assert alerts == []


def test_rotating_alert_needs_both_conditions():
    # High vibration alone should NOT trigger the rotating alert
    telemetry = make_telemetry(vibration=9.0, displacement=0.3)
    alerts = analyze_facility_health(telemetry)
    assert not any("ROTATING CRITICAL" in a for a in alerts)

    # High vibration AND high displacement together SHOULD trigger it
    telemetry = make_telemetry(vibration=9.0, displacement=1.5)
    alerts = analyze_facility_health(telemetry)
    assert any("ROTATING CRITICAL" in a for a in alerts)


def test_cavitation_alert_needs_both_conditions():
    telemetry = make_telemetry(acoustic_emission=70.0, pressure_drop=5.0)
    alerts = analyze_facility_health(telemetry)
    assert not any("FLUID CRITICAL" in a for a in alerts)

    telemetry = make_telemetry(acoustic_emission=70.0, pressure_drop=20.0)
    alerts = analyze_facility_health(telemetry)
    assert any("FLUID CRITICAL" in a for a in alerts)


def test_static_wall_thinning_alert():
    telemetry = make_telemetry(wall_thickness=3.5)
    alerts = analyze_facility_health(telemetry)
    assert any("STATIC CRITICAL" in a for a in alerts)


def test_electrical_alert_triggers_on_either_condition():
    # Only current imbalance high
    telemetry = make_telemetry(current_imbalance=6.0, hotspot_temp=50.0)
    alerts = analyze_facility_health(telemetry)
    assert any("ELECTRICAL WARNING" in a for a in alerts)

    # Only hotspot temp high
    telemetry = make_telemetry(current_imbalance=1.0, hotspot_temp=85.0)
    alerts = analyze_facility_health(telemetry)
    assert any("ELECTRICAL WARNING" in a for a in alerts)
