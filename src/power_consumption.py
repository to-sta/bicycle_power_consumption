""" power consumption module """

from math import sin, cos, atan, radians, degrees
from typing import Optional, List


def power_consumption(
    v_G: float,
    m_T: float,
    G_R: float,
    C_D: float,
    A: float,
    E_C: float,
    C_RR: float,
    v_W: float,
    D_B: int,
    D_W: int,
    I: float,
    F_W: float,
    r: float,
    v_Gi: float,
    v_Gf: float,
    t_i: float,
    t_f: float,
) -> List[float]:
    """power consumption of a bicycle
    ------------------------------

    This function calculates the power consumption of a bicycle based on the paper "Validation of a Mathematical Model for Road Cycling Power".
    A wind direction is assumed to be only in the direction that the bike is traveling. That leaves two options tail- or headwind. Tail wind is positive.

    Source:
        Martin, James & Milliken, Douglas & Cobb, John & McFadden, Kevin & Coggan, Andrew. (1998).
        Validation of a Mathematical Model for Road Cycling Power. Journal of Applied Biomechanics.
        14. 276-291. 10.1123/jab.14.3.276.

    Link to the full paper:
        https://www.researchgate.net/publication/279937184_Validation_of_a_Mathematical_Model_for_Road_Cycling_Power


    Paremeters
    ----------
    v_G: float
        ground velocity [m/s]
    m: float
        total mass of the cyclist and bike [kg]

    Optinal Paremeters:

    C_D: float default = 1.1
        drag coeffient for the bike and cyclist [-]
        default: Upright position
    A: float default = 0.5
        frontal area of the bike and cyclist [m²]

    Source for C_D and A default values:
    https://www.princeton.edu/~maelabs/hpt/mechanics/mecha_55.htm#:~:text=The%20upright%20position%20frequently%20used,that%20for%20a%20flat%20plate!

    eta: float default = 0.976
        mechanical efficiency of the drivetrain [-]

    C_RR: float default = 0.0032
        rolling resistance coeffiecent [-]
    v_W: float default = 0
        wind velocity [m/s] (tailwind is a positive number)
    D_B: float default = 0
        direction of the bike [0...360°]
    D_W: float = 0
        direction of the wind [0...360°]
    G_R: float, default = 10
        Gradient also called (slope, grade, incline,...) | Gradient = (vertical_distance/horizontal_distance)*100 [-]
    I: float
        moment of inertia of the bicycle wheel [kgm²]
    r: float
        radius of the bicycle wheel [m]


    Returns
    -------
    P_total: float
        total power consumption for the given parameters [W]
    P_AT: float
        power for aerodynamic drag by rider and bicycle [W]
    P_WR: float
        power for aerodyamic drag for the wheel rotating [W]
    P_RR: float
        power for rolling resistance [W]
    P_WB: float
        power for wheel bearing friction [W]
    P_PE: float
        power for the potential energie incl. grade [W]
    P_KE: float
        power for kinetic energie (velocity change) [W]

    Raises
    ------
    None

    """

    rho = 1.2234  # Air density [kg/m³]
    g = 9.81  # Force of gravity [N]

    D_W = radians(D_W)
    D_B = radians(D_B)
    v_WTAN = v_W * cos(D_W - D_B)
    v_A = v_G + v_WTAN

    P_AT = (1 / 2) * rho * (C_D * A + F_W) * v_A**2 * v_G
    P_RR = v_G * cos(atan(G_R)) * C_RR * m_T * g
    P_WB = v_G * (90 + 8.7 * v_G) * 10 ** (-3)
    P_PE = v_G * m_T * g * sin(atan(G_R))
    P_KE = (1 / 2) * (m_T + (I / r**2)) * ((v_Gf**2 - v_Gi**2) / (t_f - t_i))

    P_Total = (P_AT + P_RR + P_WB + P_PE + P_KE) / (E_C)
    results = [P_Total, P_AT, P_RR, P_WB, P_PE, P_KE]

    return results
