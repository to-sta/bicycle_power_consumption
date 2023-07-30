from src.power_consumption import power_consumption
from cutecharts.charts import Line

def main():
    
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


    # Plot
    chart = Line(title="Power consumption over velocity")
    chart.set_options(
        x_label="Velocity [m/s]",
        y_label="Power [W]"
    )
    


    chart.add_series("series-A", [57, 134, 137, 129, 145, 60, 49])
    chart.add_series("series-B", [114, 55, 27, 101, 125, 27, 105])

if __name__ == "__main__":
    main()