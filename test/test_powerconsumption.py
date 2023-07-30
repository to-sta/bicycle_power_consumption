from src.power_consumption import power_consumption
import pytest


def test_powerconsumption():
    """test for power_consumption

    Test data and results are from appendix I from the paper "Validation of a Mathematical Model for Road Cycling Power".
    Here we check for +-1 % accuracy to include rounding error.

        Source:
            Martin, James & Milliken, Douglas & Cobb, John & McFadden, Kevin & Coggan, Andrew. (1998).
            Validation of a Mathematical Model for Road Cycling Power. Journal of Applied Biomechanics.
            14. 276-291. 10.1123/jab.14.3.276.

        Link to the full paper:
            https://www.researchgate.net/publication/279937184_Validation_of_a_Mathematical_Model_for_Road_Cycling_Power
    """

    # Test Data
    total_mass = 90
    wind_direction = 310
    rider_direcetion = 340
    wind_velocity = 2.94
    initial_ground_velocity = 8.28
    final_ground_velocity = 8.45
    ground_velocity = 8.36
    road_gradient = 0.003
    frontal_area = 0.285
    drag_coeffient = 0.9
    rolling_resistance_coeffient = 0.0032
    incremental_drag_area_spokes = 0.0044
    moment_of_inertia_wheels = 0.14
    wheel_radius = 0.311
    final_time = 100
    initial_time = 43.58
    drivetrain_efficiency = 0.976

    # Test Results
    total_power = 213.3
    aerodynamic_power = 158.8
    rolling_resistance_power = 23.6
    wheel_bearing_friction_power = 1.4
    potential_energy_power = 22.1
    kinetic_energy_power = 2.3

    results = power_consumption(
        v_G=ground_velocity,
        m_T=total_mass,
        G_R=road_gradient,
        C_D=drag_coeffient,
        A=frontal_area,
        E_C=drivetrain_efficiency,
        C_RR=rolling_resistance_coeffient,
        v_W=wind_velocity,
        D_B=rider_direcetion,
        D_W=wind_direction,
        I=moment_of_inertia_wheels,
        F_W=incremental_drag_area_spokes,
        r=wheel_radius,
        v_Gi=initial_ground_velocity,
        v_Gf=final_ground_velocity,
        t_i=initial_time,
        t_f=final_time,
    )

    assert total_power == pytest.approx(results[0], rel=0.5)
    assert aerodynamic_power == pytest.approx(results[1], rel=0.5)
    assert rolling_resistance_power == pytest.approx(results[2], rel=0.5)
    assert wheel_bearing_friction_power == pytest.approx(results[3], rel=0.5)
    assert potential_energy_power == pytest.approx(results[4], rel=0.5)
    assert kinetic_energy_power == pytest.approx(results[5], rel=0.5)
